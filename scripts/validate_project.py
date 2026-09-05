#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

CHAPTER_FILE_RE = re.compile(r"^(\d{2})-[a-z0-9-]+\.md$")
NUMBERED_H1_RE = re.compile(r"^#\s+Kapitel\s+(\d+):\s+.+$")
MARKERS = ("TODO", "FIXME", "[PLACEHOLDER]")
REQUIRED = (
    "README.md",
    "docs/export-metadata.yaml",
    "chapters",
    "assets/cover/cover.png",
    "scripts/build_book.py",
    "scripts/validate_project.py",
    "publishing/epub.css",
    "publishing/pdf-header.tex",
)


def parse_metadata(path: Path) -> tuple[dict[str, str], list[str]]:
    scalars: dict[str, str] = {}
    chapters: list[str] = []
    in_chapters = False
    for raw in path.read_text(encoding="utf-8").splitlines():
        if re.match(r"^chapters:\s*$", raw):
            in_chapters = True
            continue
        if in_chapters:
            match = re.match(r"^\s*-\s+(.+?)\s*$", raw)
            if match:
                chapters.append(match.group(1).strip().strip("'\""))
                continue
            if raw and not raw[0].isspace():
                in_chapters = False
        if raw and not raw[0].isspace() and ":" in raw:
            key, value = raw.split(":", 1)
            value = value.strip().strip("'\"")
            scalars[key.strip()] = value
    return scalars, chapters


def validate_links(root: Path, errors: list[str]) -> None:
    pattern = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
    for md in sorted(root.rglob("*.md")):
        if ".git" in md.parts:
            continue
        for target in pattern.findall(md.read_text(encoding="utf-8")):
            target = target.strip().strip("<>")
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not target:
                continue
            candidate = (md.parent / target).resolve()
            try:
                candidate.relative_to(root)
            except ValueError:
                continue
            if not candidate.exists():
                errors.append(f"Trasig intern Markdown-länk i {md.relative_to(root)}: {target}")


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    errors: list[str] = []

    for rel in REQUIRED:
        if not (root / rel).exists():
            errors.append(f"Obligatorisk sökväg saknas: {rel}")

    metadata_path = root / "docs/export-metadata.yaml"
    if not metadata_path.exists():
        for item in errors:
            print(f"ERROR: {item}", file=sys.stderr)
        return 1

    metadata, configured_chapters = parse_metadata(metadata_path)
    for key in ("title", "author", "language", "project_slug", "cover_image"):
        if not metadata.get(key):
            errors.append(f"docs/export-metadata.yaml saknar '{key}'.")

    if metadata.get("cover_image") and not (root / metadata["cover_image"]).is_file():
        errors.append(f"Omslagsfilen i metadata finns inte: {metadata['cover_image']}")

    chapter_files = sorted((root / "chapters").glob("[0-9][0-9]-*.md"))
    actual = [p.relative_to(root).as_posix() for p in chapter_files]
    if configured_chapters != actual:
        errors.append("Kapitelordningen i docs/export-metadata.yaml matchar inte chapters/-katalogen.")

    expected_numbers = list(range(len(chapter_files)))
    actual_numbers: list[int] = []
    for path in chapter_files:
        match = CHAPTER_FILE_RE.match(path.name)
        if not match:
            errors.append(f"Ogiltigt kapitelfilnamn: {path.name}")
            continue
        number = int(match.group(1))
        actual_numbers.append(number)
        text = path.read_text(encoding="utf-8")
        if not text.strip():
            errors.append(f"Tom kapitelfil: {path.relative_to(root)}")
            continue
        first = text.lstrip().splitlines()[0].strip()
        if number == 0:
            if first != "# Inledning":
                errors.append("chapters/00-inledning.md ska börja med '# Inledning'.")
        else:
            h1 = NUMBERED_H1_RE.match(first)
            if not h1 or int(h1.group(1)) != number:
                errors.append(
                    f"{path.relative_to(root)} ska börja med '# Kapitel {number}: <rubrik>'."
                )
        for marker in MARKERS:
            if marker in text:
                errors.append(f"{path.relative_to(root)} innehåller arbetsmarkören {marker}.")

    if actual_numbers != expected_numbers:
        errors.append(
            f"Kapitelfilerna ska vara en obruten serie 00..{len(chapter_files)-1:02d}; "
            f"hittade {actual_numbers}."
        )

    validate_links(root, errors)

    if errors:
        for item in errors:
            print(f"ERROR: {item}", file=sys.stderr)
        print(f"Validation failed: {len(errors)} error(s).", file=sys.stderr)
        return 1

    print(
        f"OK: {metadata.get('title')} – {len(chapter_files)} manusfiler, "
        f"metadata, omslag och interna länkar verifierade."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
