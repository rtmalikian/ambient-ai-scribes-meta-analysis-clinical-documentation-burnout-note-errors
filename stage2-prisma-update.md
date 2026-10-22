# PRISMA update, Stage 2 strict screening, 22 October 2026

Stage 1 passed 463 of 567 records as include or maybe. That pass used two rule-based decision procedures and was too loose. Stage 2 read the abstract of each of those 463 records and applied the protocol eligibility rules strictly: primary empirical studies only, documenting clinicians or their real notes, an ambient scribe that listens to an encounter and drafts the note, and at least one protocol outcome measured or auditable.

## New flow counts

- Records identified in the search: 1,049
- Duplicates removed before screening: 482
- Records screened at Stage 1: 567
- Records excluded at Stage 1: 104
- Records passed to Stage 2: 463
- Records excluded at Stage 2: 306
- Reports to seek for full text retrieval: 157
- Reports not retrieved: not yet known. Retrieval is the next step.
- Studies finally included: not yet known. Full text screening comes next, and this count will fall again there.

## Stage 2 exclusions by main reason

Each excluded record was given one main group, taken from the reason and design recorded for it in screening-stage2.csv.

- Non-primary publication type, such as a review, editorial, commentary, viewpoint, framework or guideline paper: 136
- No abstract in the search record, and the title did not show a primary ambient scribe evaluation: 65
- Descriptive or implementation report with no measured protocol outcome, or a non-study record such as a correction or a supplement file: 28
- Primary study design but no protocol outcome measured: 17
- Qualitative attitudes only: 14. These sit in background-studies-stage2.md for the background and discussion. They are not pooled.
- Attitudes survey, no protocol outcome: 13
- Wrong intervention, not an ambient scribe: 9
- Patient attitudes only: 8
- Simulation or vignette study with no eligible note audit: 7
- Wrong population, such as students only or non-clinical settings: 5
- Protocol or trial registration with no results: 4
- Total excluded: 306

## Notes on the 463

- 128 of the 463 records had no abstract in the search export. Those were decided on the title alone. 119 were excluded and 9 were included, each one only where the title on its own showed a primary ambient evaluation with a named protocol outcome, such as burnout, note quality, accuracy or a hallucination audit. Every one of these rows is marked in screening-stage2.csv.
- 21 records were genuinely ambiguous at abstract level. They are listed in flagged-for-author-v2.md with the Stage 2 call and the open question for each.
- Two included records, R0363 and R0516, carry the same title. Full text retrieval must settle whether they are two reports of one study. Study counts later in this review count studies, not reports.
- The 157 is larger than the 25 to 60 primary studies expected when the protocol was written. The abstract reading shows why: the 2024 to 2026 literature holds a long tail of small single-site pilot evaluations, most of them uncontrolled before-and-after studies (44 with that design label alone), plus 35 standardised encounter audits and 10 error audits of generated notes. Whether all 157 hold enough data to extract is a full text question, and the protocol already lists conference abstracts with too little data as awaiting classification rather than included.

## Design mix of the 157 reports sought

Design labels as recorded at abstract level: before-and-after and pre-post evaluations are the largest group, followed by standardised audits (35), cohort studies (17 across cohort labels), error audits (10), cross-sectional survey evaluations of actual scribe use (about 10), and randomised designs (9 across RCT, stepped wedge and phased randomised labels). The rest are mixed methods evaluations, controlled comparisons and single note audits.

## Files from this stage

- screening-stage2.csv, one row for each of the 463 records, with decision, reason grounded in the abstract, design, and flags for ambiguous and no-abstract records. Part files sit in the stage2 folder.
- full-text-list-v2.md, the 157 strict includes only, with identifier, URL and open access status where recorded.
- flagged-for-author-v2.md, 21 records.
- background-studies-stage2.md, the 14 qualitative attitudes studies kept for background.
