#!/usr/bin/env python3
"""
Apply taxonomy tags to all notes in the _notes directory.

Tag taxonomy:
  Maturity:  seed | wip | v1 | updated | evergreen
  Type:      note | article | moc | log | ressource
  Workflow:  to_update | candidate_post

Heuristics based on existing tags + word count.
"""

import os
import re
import sys

NOTES_DIR = "_notes"
DRY_RUN = "--dry-run" in sys.argv

# Tags that should not be duplicated
MATURITY_TAGS = {"seed", "wip", "v1", "updated", "evergreen", "stale"}
TYPE_TAGS = {"note", "article", "moc", "log", "ressource"}
WORKFLOW_TAGS = {"to_update", "to_refactor", "to_publish", "candidate_post"}
ALL_TAXONOMY = MATURITY_TAGS | TYPE_TAGS | WORKFLOW_TAGS


def extract_front_matter(content):
    """Return (fm_string, body_start_index) or (None, 0)."""
    if not content.startswith("---\n"):
        return None, 0
    end = content.find("\n---", 4)
    if end == -1:
        return None, 0
    return content[4:end], end + 4


def parse_tags(fm):
    """Extract list of exact tags from front matter string."""
    m = re.search(r"^tags:\s*\n((?:[ \t]*-[^\n]*\n?)+)", fm, re.MULTILINE)
    if m:
        tags = []
        for line in m.group(1).splitlines():
            tag = line.strip().lstrip("- ").strip()
            if tag:
                tags.append(tag)
        return tags
    # Inline: tags: [a, b]
    m2 = re.search(r"^tags:\s*\[([^\]]+)\]", fm, re.MULTILINE)
    if m2:
        return [t.strip().strip('"').strip("'") for t in m2.group(1).split(",") if t.strip()]
    return []


def word_count(content):
    text = re.sub(r"---.*?---", "", content, flags=re.DOTALL)
    text = re.sub(r"[-*#>`\[\]!|]", " ", text)
    return len(text.split())


def wikilink_count(content):
    return len(re.findall(r"\[\[.+?\]\]", content))


def external_link_count(content):
    return len(re.findall(r"\(https?://", content))


def determine_type(existing_tags, wc, wlc, elc):
    tl = [t.lower() for t in existing_tags]
    if "index" in tl or "meta-analyse" in tl:
        return "moc"
    if "article" in tl or "designs" in tl:
        return "article"
    if "guidebook" in tl:
        return "ressource"
    if "logs" in tl or "log" in tl:
        return "log"
    # Heuristic: hub note with many wikilinks
    if wlc >= 8 and wc < 600:
        return "moc"
    # Heuristic: curation/resource note
    if elc >= 4 and wc < 500:
        return "ressource"
    return "note"


def determine_maturity(existing_tags, wc, type_tag):
    tl = [t.lower() for t in existing_tags]
    if "afairepousser" in tl:
        return "wip"
    if type_tag == "moc" and wc >= 150:
        return "evergreen"
    if not existing_tags or wc < 150:
        return "seed"
    if wc >= 700:
        return "updated"
    if wc >= 250:
        return "v1"
    return "seed"


def determine_workflow(existing_tags, wc, type_tag):
    tl = [t.lower() for t in existing_tags]
    workflow = []
    if "afairepousser" in tl:
        workflow.append("to_update")
    if ("article" in tl or "designs" in tl) and wc >= 400:
        workflow.append("candidate_post")
    return workflow


def rebuild_front_matter(fm, tags_to_add):
    """Append new tags to the front matter's tags list (or create tags block)."""
    if not tags_to_add:
        return fm

    m = re.search(r"^(tags:\s*\n)((?:[ \t]*-[^\n]*\n?)+)", fm, re.MULTILINE)
    if m:
        existing_block = m.group(2)
        # Detect indentation from first item
        first_line = existing_block.splitlines()[0]
        indent = re.match(r"^([ \t]*)-", first_line)
        indent_str = indent.group(1) if indent else "  "
        new_lines = "".join(f"{indent_str}- {t}\n" for t in tags_to_add)
        new_block = existing_block.rstrip("\n") + "\n" + new_lines
        return fm[: m.start(2)] + new_block + fm[m.end(2):]

    # Inline tags: convert to block and add
    m2 = re.search(r"^tags:\s*\[([^\]]+)\]", fm, re.MULTILINE)
    if m2:
        existing = [t.strip() for t in m2.group(1).split(",") if t.strip()]
        all_tags = existing + tags_to_add
        block = "tags:\n" + "".join(f"  - {t}\n" for t in all_tags)
        return fm[: m2.start()] + block.rstrip("\n") + fm[m2.end():]

    # No tags at all: append before end of front matter
    new_block = "\ntags:\n" + "".join(f"  - {t}\n" for t in tags_to_add)
    return fm.rstrip("\n") + new_block


def process_note(path):
    with open(path, encoding="utf-8") as f:
        content = f.read()

    fm, body_start = extract_front_matter(content)
    if fm is None:
        # No front matter at all — create minimal one
        existing_tags = []
        fm = f'title: {os.path.splitext(os.path.basename(path))[0]}'
        body_start = 0
        body = content
    else:
        existing_tags = parse_tags(fm)
        body = content[body_start:]

    # Skip if all taxonomy categories already present
    tl = [t.lower() for t in existing_tags]
    has_maturity = any(t in MATURITY_TAGS for t in tl)
    has_type = any(t in TYPE_TAGS for t in tl)

    if has_maturity and has_type:
        return False, "already tagged"

    wc = word_count(content)
    wlc = wikilink_count(content)
    elc = external_link_count(content)

    new_tags = []

    if not has_type:
        new_tags.append(determine_type(existing_tags, wc, wlc, elc))

    if not has_maturity:
        new_tags.append(determine_maturity(existing_tags, wc, new_tags[0] if new_tags else determine_type(existing_tags, wc, wlc, elc)))

    # Always add workflow tags if not already present
    for wt in determine_workflow(existing_tags, wc, new_tags[0] if new_tags else ""):
        if wt not in tl:
            new_tags.append(wt)

    # Remove any that are already there
    new_tags = [t for t in new_tags if t.lower() not in tl]

    if not new_tags:
        return False, "no new tags needed"

    new_fm = rebuild_front_matter(fm, new_tags)

    if not DRY_RUN:
        if body_start == 0 and not content.startswith("---\n"):
            # Had no front matter
            new_content = f"---\n{new_fm}\n---\n{content}"
        else:
            new_content = f"---\n{new_fm}\n---{body}"
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)

    return True, new_tags


def main():
    if DRY_RUN:
        print("DRY RUN — no files will be modified\n")

    changed = 0
    skipped = 0
    errors = 0
    tag_distribution = {}

    notes = sorted(
        [f for f in os.listdir(NOTES_DIR) if f.endswith(".md")]
    )

    for fn in notes:
        path = os.path.join(NOTES_DIR, fn)
        try:
            modified, result = process_note(path)
            if modified:
                changed += 1
                for t in result:
                    tag_distribution[t] = tag_distribution.get(t, 0) + 1
                if DRY_RUN:
                    print(f"  + {fn}: {result}")
            else:
                skipped += 1
        except Exception as e:
            errors += 1
            print(f"  ERROR {fn}: {e}")

    print(f"\n{'[DRY RUN] ' if DRY_RUN else ''}Done.")
    print(f"  Modified: {changed}")
    print(f"  Skipped (already tagged or no change): {skipped}")
    print(f"  Errors: {errors}")
    print(f"\nTags added:")
    for t, cnt in sorted(tag_distribution.items(), key=lambda x: -x[1]):
        print(f"  {cnt:3d} | {t}")


if __name__ == "__main__":
    main()
