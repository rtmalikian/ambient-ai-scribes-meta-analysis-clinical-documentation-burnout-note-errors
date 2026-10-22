# PRISMA 2020 flow, Stage 3 update (full text stage)

Counts from retrieval-log.csv, fulltext-screening.csv and the files on disk, 22 October 2026. Stage 2 ended with 157 reports marked for full text retrieval (screening-stage2.csv strict includes).

## Flow

- Reports sought for retrieval: 157
- Reports not retrieved: 74
  - 65 records yielded no file at all: no free full text found through Europe PMC or PubMed Central full text, Unpaywall open access locations, publisher open access pages, or medRxiv full text, across three retrieval waves.
  - 9 more files first counted as retrieved turned out to hold no article text (7 Europe PMC JavaScript stub pages, 1 paywall landing page, 1 publisher abstract page) and were moved to not retrieved in substance. Record IDs and the reason for each sit in fulltext-screening.csv (decision: not_assessed) and retrieval-log.csv.
- Reports assessed for eligibility: 83 (157 sought, minus 74 not retrieved)
- Reports excluded at full text: 8
  - Qualitative study only, no quantitative protocol outcome: 1 (R0003)
  - No protocol outcome as defined (edit content analysis, edits not graded as errors): 1 (R0146)
  - Simulation study, outcomes measured in simulated encounters, no graded note outcome: 1 (R0185)
  - Wrong intervention (general purpose LLM on transcripts, not an ambient scribe product): 1 (R0379)
  - Duplicate report of a study already in the set, published version used: 4 (R0323 preprint of R0257; R0332 preprint of R0245; R0407 preprint of R0030; R0424 preprint of R0206)
- Reports awaiting classification: 1 (R0506, conference abstract in a journal supplement, no notes denominator or extractable outcome data in protocol form)
- Studies included: 74
- Reports of included studies: 74 (one report per study in the assessed set)

## Reports and studies

The 157 sought were reports. Four assessed reports were earlier versions of a study whose published report is also in the set, so they add no study. One further pair sits outside the assessed set: R0516 is the JMIR preprint of R0363 (see flagged resolutions). R0363, the published report, is included, so that study is counted once through R0363.

## Interpretation note recorded at this stage

Protocol section 3.2 admits note audit studies that grade a defined sample of generated notes against a reference and report a denominator in notes. This stage applied that test to simulated and standardised studies: a simulated study was included only where the graded unit was the generated note (quality score or error counts against a reference transcript or record), and excluded where its extractable outcomes were clinician time or workload measured inside simulated encounters. The affected calls, with reasons, sit in fulltext-screening.csv.

## What did not happen

No record was retrieved from a pirated source. No paywalled record was counted as assessed on the basis of its abstract, except the flagged records resolved in flagged-resolutions-stage3.md, where the basis is stated per record.
