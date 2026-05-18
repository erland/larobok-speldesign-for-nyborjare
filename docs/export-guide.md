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

## EPUB
EPUB ska ha luftig layout, riktig navigering och ingen innehållsförteckning som separat textkapitel.

## PDF
PDF ska ha innehållsförteckning före inledningen, genererad från rubrikerna.

## DOCX
DOCX ska rendera rubriker, listor, tabeller, kodblock, fetstil och kursiv stil som riktig formatering.
