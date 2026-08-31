#!/usr/bin/env python3
"""Structural validator for HTML reports produced by this skill."""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path


class TagValidator(HTMLParser):
    VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}

    def __init__(self) -> None:
        super().__init__()
        self.stack: list[str] = []
        self.errors: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag not in self.VOID:
            self.stack.append(tag)

    def handle_endtag(self, tag: str) -> None:
        if tag not in self.stack:
            self.errors.append(f"unexpected closing tag: {tag}")
            return
        while self.stack:
            if self.stack.pop() == tag:
                return


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_report.py /absolute/path/to/report.html", file=sys.stderr)
        return 2

    path = Path(sys.argv[1]).expanduser()
    if not path.is_absolute():
        print("ERROR: report path must be absolute", file=sys.stderr)
        return 2
    if not path.is_file():
        print(f"ERROR: file not found: {path}", file=sys.stderr)
        return 2

    text = path.read_text(encoding="utf-8")
    validator = TagValidator()
    validator.feed(text)

    errors = list(validator.errors)
    if validator.stack:
        errors.append("unclosed tags: " + ", ".join(validator.stack))
    if not text.lstrip().lower().startswith("<!doctype html>"):
        errors.append("missing HTML doctype")
    if not text.rstrip().lower().endswith("</html>"):
        errors.append("missing closing html tag")
    if "<nav" not in text:
        errors.append("missing navigation")

    for label in ("【页面/代码事实】", "【合理推断】", "【建议设计】", "【未知】"):
        if label not in text:
            errors.append(f"missing evidence label: {label}")

    for layer_id in ("user-layer", "technical-layer", "model-layer", "data-layer"):
        pattern = rf"<section\s+id=[\"']{re.escape(layer_id)}[\"']"
        if not re.search(pattern, text, re.I):
            errors.append(f"missing layer section: {layer_id}")

    placeholders = sorted(set(re.findall(r"\{\{[A-Z0-9_]+\}\}", text)))
    if placeholders:
        errors.append("unfinished placeholders: " + ", ".join(placeholders))

    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    section_count = len(re.findall(r"<section\b", text, re.I))
    mermaid_count = len(re.findall(r"class=[\"'][^\"']*\bmermaid\b", text, re.I))
    print("PASS")
    print(f"file={path}")
    print(f"bytes={len(text.encode('utf-8'))}")
    print(f"sections={section_count}")
    print(f"mermaid_blocks={mermaid_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
