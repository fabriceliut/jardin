# frozen_string_literal: true

require 'cgi'
require 'nokogiri'
require 'uri'

class BidirectionalLinksGenerator < Jekyll::Generator
  WIKILINK = /(!?)\[\[([^\]\n]+)\]\]/
  CODE = /^\s{0,3}(`{3,}|~{3,})[^\n]*\n.*?^\s{0,3}\1[\t ]*$|`+[^`\n]+`+/m
  BLOCK_ID = /\A\^([a-zA-Z0-9-]+)\z/
  IMAGE = /\.(png|jpe?g|gif|svg|webp|bmp)\z/i

  def generate(site)
    notes = site.collections.fetch('notes').docs
    pages = site.pages.select { |page| page.path.start_with?('_pages/') }
    @baseurl = site.baseurl.to_s
    @host = URI.parse(site.config['url'].to_s).host
    @extension = site.config['use_html_extension'] ? '.html' : ''
    @markdown = site.find_converter_instance(Jekyll::Converters::Markdown)
    @filenames = {}
    @titles = {}
    @aliases = {}
    @blocks = {}

    (notes + pages).each do |doc|
      @filenames[key(File.basename(doc.basename, '.md'))] ||= doc
      @filenames[key(doc.path.sub(/\.md\z/, ''))] ||= doc
      @titles[key(doc.data['title'])] ||= doc if doc.data['title']
      Array(doc.data['aliases']).each { |name| @aliases[key(name)] ||= doc }
      doc.content = outside_code(doc.content) { |text| register_blocks(doc, text) }
    end

    (notes + pages).each do |doc|
      doc.content = outside_code(doc.content) do |text|
        text.gsub(WIKILINK) { render_link(doc, Regexp.last_match(1), Regexp.last_match(2)) }
      end
    end

    notes_by_path = notes.to_h { |note| [canonical_path(href(note)), note] }
    notes.each { |note| note.data['backlinks'] = [] }
    edges = notes.flat_map do |note|
      html = Nokogiri::HTML::DocumentFragment.parse(@markdown.convert(note.content))
      targets = html.css('a[href]').filter_map do |anchor|
        notes_by_path[canonical_path(anchor['href'])]
      end
      targets.uniq.reject { |target| target == note }.map do |target|
        target.data['backlinks'] << note
        { source: note.url, target: target.url }
      end
    end

    nodes = notes.map do |note|
      { id: note.url, path: href(note), label: note.data['title'] }
    end
    File.write(File.join(site.source, '_includes/notes_graph.json'), JSON.dump({ edges: edges, nodes: nodes }))
  end

  private

  def key(value)
    value.to_s.strip.unicode_normalize(:nfc).downcase
  end

  def href(doc)
    "#{@baseurl}#{doc.url}#{@extension}"
  end

  def canonical_path(value)
    if (absolute = value.match(%r{\A(?:https?:)?//([^/?#]+)(/[^?#]*)?}i))
      return unless absolute[1].casecmp?(@host.to_s)

      value = absolute[2] || '/'
    end
    return unless value.start_with?('/')

    URI::DEFAULT_PARSER.unescape(value.split(/[?#]/, 2).first).unicode_normalize(:nfc)
       .sub(/\.html\z/i, '').sub(%r{/\z}, '')
  end

  def outside_code(content)
    offset = 0
    rendered = content.to_enum(:scan, CODE).map do
      match = Regexp.last_match
      preceding = yield(content[offset...match.begin(0)])
      offset = match.end(0)
      preceding + match[0]
    end
    rendered.join + yield(content[offset..])
  end

  def register_blocks(doc, text)
    paragraphs = text.split(/(\n[\t ]*\n)/)
    paragraphs.each_with_index do |paragraph, index|
      marker = paragraph.lines.last.to_s.strip.match(BLOCK_ID)
      next unless marker

      id = marker[1]
      preceding = paragraph.lines[0...-1].join.rstrip
      block_index = preceding.empty? ? index - 2 : index
      next if block_index.negative?

      block = preceding.empty? ? paragraphs[block_index] : preceding
      @blocks[[doc, id]] = block
      paragraphs[index] = preceding
      paragraphs[block_index] = %(<span id="block-#{id}"></span>\n\n#{block})
    end
    paragraphs.join
  end

  def render_link(doc, embed, raw, allow_embed: true)
    reference, label = raw.split(/\\?\|/, 2)
    name, fragment = reference.strip.split('#', 2)
    name = name.to_s.strip
    if embed == '!' && name.match?(IMAGE)
      asset = name.split('/').map { |segment| ERB::Util.url_encode(segment) }.join('/')
      width = label&.match?(/\A[1-9][0-9]{0,3}\z/) ? %( width="#{label}") : ''
      alt = label && width.empty? ? label.strip : File.basename(name)
      return %(<img src="#{escape(@baseurl)}/assets/#{asset}" alt="#{escape(alt)}"#{width} loading="lazy" />)
    end

    filename = key(name.sub(/\.md\z/i, ''))
    target = name.empty? ? doc : (@filenames[filename] || @titles[key(name)] || @aliases[key(name)])
    target ||= @filenames.values.find do |candidate|
      key(File.basename(candidate.basename, '.md')).tr('_-', '  ') == filename.tr('_-', '  ')
    end
    unless target
      return %(<span title="Note en attente" class="invalid-link"><span class="invalid-link-brackets">[[</span>#{escape(label || raw)}<span class="invalid-link-brackets">]]</span></span>)
    end

    block_id = fragment&.match(BLOCK_ID)&.[](1)
    anchor = if block_id && @blocks.key?([target, block_id])
               "block-#{block_id}"
             elsif fragment && !block_id
               heading_id(fragment)
             end
    url = href(target)
    url += "##{ERB::Util.url_encode(anchor)}" if anchor
    link = %(<a class="internal-link" href="#{escape(url)}">#{escape(label || (name.empty? ? fragment : name))}</a>)
    return link unless embed == '!' && allow_embed

    block = @blocks[[target, block_id]] if block_id
    if fragment && !block
      return link
    elsif block
      block = outside_code(block) do |text|
        text.gsub(WIKILINK) { render_link(target, Regexp.last_match(1), Regexp.last_match(2), allow_embed: false) }
      end
      excerpt = @markdown.convert(block)
    else
      excerpt = target.content.gsub(WIKILINK) { Regexp.last_match(2).split('|').last }
      excerpt = %(<p class="transclusion-content">#{escape(Nokogiri::HTML::DocumentFragment.parse(excerpt).text.strip.slice(0, 300))}…</p>)
    end
    %(<blockquote class="transclusion">#{excerpt}<footer>↗ #{link}</footer></blockquote>)
  end

  def heading_id(fragment)
    heading = Nokogiri::HTML::DocumentFragment.parse(@markdown.convert("# #{fragment}")).at_css('h1')
    heading&.[]('id')
  end

  def escape(text)
    CGI.escapeHTML(text.to_s)
  end
end
