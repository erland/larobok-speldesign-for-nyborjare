#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

PANDOC_VERSION = "3.1.11.1"


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
            scalars[key.strip()] = value.strip().strip("'\"")
    return scalars, chapters


def pandoc_version() -> str:
    result = subprocess.run(["pandoc", "--version"], text=True, capture_output=True)
    if result.returncode != 0:
        raise RuntimeError("Pandoc finns inte i PATH.")
    match = re.search(r"pandoc\s+([^\s]+)", result.stdout.splitlines()[0])
    return match.group(1) if match else "unknown"


def run(command: list[str], cwd: Path) -> None:
    print("+", " ".join(command))
    subprocess.run(command, cwd=cwd, check=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--formats", default="epub,pdf")
    parser.add_argument("--name", default="")
    parser.add_argument("--allow-pandoc-version-mismatch", action="store_true")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    output_dir = Path(args.output_dir).resolve()
    run([sys.executable, "scripts/validate_project.py", "."], root)

    version = pandoc_version()
    if version != PANDOC_VERSION and not args.allow_pandoc_version_mismatch:
        print(f"ERROR: Pandoc {PANDOC_VERSION} krävs; hittade {version}.", file=sys.stderr)
        return 2

    metadata_path = root / "docs/export-metadata.yaml"
    metadata, chapter_refs = parse_metadata(metadata_path)
    chapters = [root / rel for rel in chapter_refs]
    output_dir.mkdir(parents=True, exist_ok=True)
    base_name = args.name or metadata.get("project_slug", "book")
    formats = {part.strip().lower() for part in args.formats.split(",") if part.strip()}
    if not formats or not formats <= {"epub", "pdf"}:
        print("ERROR: --formats måste vara epub och/eller pdf.", file=sys.stderr)
        return 2

    # Chapter Markdown files use image paths such as ../assets/images/....
    # Include both the repository root and chapters/ in Pandoc's resource path
    # so those references resolve correctly regardless of the process cwd.
    resource_path = f"{root}:{root / 'chapters'}"
    chapter_filter = root / "publishing/chapter-headings.lua"
    common = [
        "--metadata-file", str(metadata_path),
        "--resource-path", resource_path,
        "--lua-filter", str(chapter_filter),
        "--toc-depth=1",
    ]

    if "epub" in formats:
        epub = output_dir / f"{base_name}.epub"
        run([
            "pandoc", *map(str, chapters),
            "--from=markdown", "--to=epub3",
            "--output", str(epub),
            *common,
            # EPUB readers already expose the generated navigation document as
            # their contents/index. Do not add a second visible TOC chapter.
            "--css", str(root / "publishing/epub.css"),
            "--epub-cover-image", str(root / metadata["cover_image"]),
        ], root)
        print(f"OK: EPUB skapad: {epub}")

    if "pdf" in formats:
        if shutil.which("xelatex") is None:
            print("ERROR: xelatex krävs för PDF-bygget.", file=sys.stderr)
            return 2
        pdf = output_dir / f"{base_name}.pdf"
        with tempfile.TemporaryDirectory(prefix="speldesign-pdf-") as tmp:
            frontmatter = Path(tmp) / "frontmatter.tex"
            cover = (root / metadata["cover_image"]).as_posix()
            title = metadata.get("title", "")
            subtitle = metadata.get("subtitle", "")
            author = metadata.get("author", "")
            frontmatter.write_text(
                "\\thispagestyle{empty}\n"
                "\\newgeometry{margin=0pt}\n"
                f"\\noindent\\includegraphics[width=\\paperwidth,height=\\paperheight]{{{cover}}}\n"
                "\\restoregeometry\\clearpage\n"
                "\\thispagestyle{empty}\n"
                "\\vspace*{0.18\\textheight}\n"
                "\\begin{center}\n"
                f"{{\\Huge\\bfseries {title}}}\\par\n"
                f"\\vspace{{1em}}{{\\Large {subtitle}}}\\par\n"
                "\\vfill\n"
                f"{{\\Large {author}}}\\par\n"
                "\\end{center}\\clearpage\n",
                encoding="utf-8",
            )
            run([
                "pandoc", *map(str, chapters),
                "--from=markdown", "--to=pdf",
                "--pdf-engine=xelatex", "--output", str(pdf),
                *common,
                "--toc",
                # The metadata title would otherwise make Pandoc emit its own
                # title page before our explicit cover/title front matter.
                "--metadata", "title=",
                "--include-in-header", str(root / "publishing/pdf-header.tex"),
                "--include-before-body", str(frontmatter),
                "-V", "papersize=a4",
                "-V", "geometry:margin=22mm",
                "-V", "fontsize=11pt",
                "-V", "mainfont=TeX Gyre Pagella",
                "-V", "sansfont=TeX Gyre Heros",
                "-V", "colorlinks=true",
                "-V", "linkcolor=black",
                "-V", "urlcolor=blue",
            ], root)
        print(f"OK: PDF skapad: {pdf}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
