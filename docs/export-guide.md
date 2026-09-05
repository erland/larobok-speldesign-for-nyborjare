# Exportguide

## Grundprincip
All export ska utgå från `docs/export-metadata.yaml` och kapitelordningen där.

## Före export
Kontrollera att:
- titel, författare, språk, datum, version och identifierare finns i metadata
- `chapters/00-inledning.md` ligger först
- alla kapitel använder H1–H3, inte H4 eller lägre
- rå markdown inte syns som vanlig text i exporten
- alla bildlänkar pekar på existerande filer

Projektet har en snabb validator som kan köras lokalt:

```bash
python3 scripts/validate_project.py .
```

## GitHub Actions
Tre workflows ligger i `.github/workflows/`:

1. **Validate** körs vid pull request och relevanta pushar till `main`.
2. **Build Preview** startas manuellt och bygger EPUB + PDF som ett gemensamt Actions-artifact med sju dagars retention.
3. **Release** triggas av taggar som matchar `v*` och publicerar EPUB och PDF som separata GitHub Release-assets.

Pandoc är låst till version `3.1.11.1` för reproducerbara byggen. PDF byggs med XeLaTeX och TeX Gyre-fontfamiljen.

## Lokal EPUB/PDF-export
När Pandoc 3.1.11.1 och XeLaTeX finns installerade:

```bash
python3 scripts/build_book.py --output-dir exports
```

Det skapar `speldesign-for-nyborjare.epub` och `speldesign-for-nyborjare.pdf`.

## EPUB
EPUB ska ha luftig layout, riktig navigering och omslaget från `assets/cover/cover.png`.

## PDF
PDF ska ha omslag, titelsida och innehållsförteckning före inledningen, genererad från rubrikerna.

## DOCX
DOCX ska rendera rubriker, listor, tabeller, kodblock, fetstil och kursiv stil som riktig formatering.
