#!/usr/bin/env python3
"""Check first-party routes, fragments and assets in the generated Jekyll site."""

import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.ids = set()
        self.references = set()
        self.feed(path.read_text(encoding="utf-8"))

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "a" and attrs.get("name"):
            self.ids.add(attrs["name"])
        if tag in {"a", "link"} and attrs.get("href"):
            self.references.add(attrs["href"])
        if tag in {"img", "script", "source", "audio", "video"} and attrs.get("src"):
            self.references.add(attrs["src"])
        if tag == "meta" and (attrs.get("property") == "og:image" or attrs.get("name") == "twitter:image"):
            if attrs.get("content"):
                self.references.add(attrs["content"])


def resolve(root, route):
    target = root.joinpath(*route.strip("/").split("/"))
    candidates = [target, target / "index.html", Path(str(target) + ".html")]
    return next((candidate for candidate in candidates if candidate.is_file()), None)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site", nargs="?", type=Path, default=Path("_site"))
    parser.add_argument("--url", default="https://jardin.liut.me")
    args = parser.parse_args()
    root = args.site
    host = urlsplit(args.url).netloc
    pages = {path: Page(path) for path in root.rglob("*.html")}
    if not pages:
        parser.error(f"No rendered HTML in {root}. Run Jekyll first.")
    errors = []
    for path, page in pages.items():
        relative = path.relative_to(root).as_posix()
        url = args.url.rstrip("/") + "/" + relative
        for reference in sorted(page.references):
            parsed = urlsplit(urljoin(url, reference))
            if parsed.scheme not in {"http", "https"} or parsed.netloc != host:
                continue
            destination = resolve(root, unquote(parsed.path))
            if destination is None:
                errors.append((relative, reference, "route or asset missing"))
            elif parsed.fragment and destination in pages and unquote(parsed.fragment) not in pages[destination].ids:
                errors.append((relative, reference, "anchor missing"))

    for page, reference, reason in sorted(errors):
        print(f"{page} → {reference} ({reason})")
    print(f"Checked {len(pages)} HTML pages, {len(errors)} unresolved references.")
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
