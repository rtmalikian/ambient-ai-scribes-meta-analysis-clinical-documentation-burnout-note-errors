# LLM team log

This log is data for the finished review. The review reports these mechanics in its methods and results: how the LLM team was set up, where its members agreed, where they split, and what the splits cost. Tool: Muse (Meta), model Muse Spark, used through the author agent environment on 22 October 2026. Role prompts and decision procedures: prompts version 1, filed as prompts.md in this review folder.

## Roles at work so far
- Information specialist: built the strings in search-log.md, ran five source runs, logged two blocked sources with their errors, and prepared the pending strings in search-appendix-pending.md.
- Screener A (strict pass): separate decision procedure, title and abstract only. Calls: include 233, maybe 207, exclude 127.
- Screener B (sensitive pass): separate decision procedure, applied apart from A, no sight of A calls. Calls: include 339, maybe 122, exclude 106.
- Adjudicator: worked on disagreements only, under the rules in prompts version 1.
- Extractor and risk of bias pair: at work from Stage 3 on. Their Stage 4a mechanics sit in the Stage 4a section at the end of this log. Statistician, GRADE assessor, methods editor: not yet at work.

## Title and abstract screening mechanics, 22 October 2026
- Records screened: 567.
- Agreements: 439. Agreement rate: 0.7743.
- Cohen kappa: 0.6439.
- Disagreements: 128, by pair:
  - maybe vs include: 97
  - exclude vs maybe: 15
  - exclude vs include: 11
  - include vs exclude: 2
  - maybe vs exclude: 3
- Adjudication outcomes:
  - include/maybe settled as include: 97
  - maybe/exclude settled as maybe: 15
  - include/exclude settled as maybe, flagged for author: 13
  - maybe/exclude settled as exclude (hard bar): 3
- Final calls after adjudication: include 328, maybe 135, exclude 104.
- Flagged for the human author: 13 records, where one screener said include and the other exclude. They sit in the maybe group for full text, and the author settles each one at full text stage. Record IDs: R0128, R0136, R0198, R0201, R0339, R0401, R0493, R0509, R0520, R0527, R0528, R0534, R0547.

## Extraction mechanics
- Stage 3 produced a partial prose extraction sheet (extraction_data.py) covering all 74 included studies, with gaps the sheet itself named (values sitting in full text tables, supplement-only detail, figure-only values).
- Stage 4a (below) replaced that sheet with a line by line extraction from the converted full texts, in 12 parallel batches, and the Stage 3 sheet served as the comparison pass for the main text values. Discrepancies found between the Stage 3 sheet and the Stage 4a reading were kept visible in the batch files rather than silently resolved: examples are R0256 (neurology PDQI-9 summary 42.2 in Results text against 41.2 in Table 1), R0278 (Mini-Z direction reversed between abstract and Results), R0287 (Table 1 pajama time against the narrative claim), R0148 (Table 1 closure counts against Results text), R0414 (vital signs difference 86.6 in narrative against 71.8 in Table 3), and R0127 (the 70 second figure in the Stage 3 summary line was not found in the full text; 86 seconds is what the paper prints).

## Stage 4a: full extraction and risk of bias, 22 October 2026

Roles at work in this stage: extractor (12 parallel batch passes, one per group of 6 to 8 studies, each reading its converted full texts in full), risk of bias assessor pair (Pass A and an independent Pass B inside each batch, with adjudicated judgements), and the coordinating author pass that merged the batches, normalised the poolability vocabulary (batches 1 to 6 filed poolable or narrative-only; batches 7 to 12 filed yes or no with the same meaning; the merged file uses poolable or narrative-only throughout), and built the analysis datasets.

### Extraction counts
- Studies extracted: 74 of 74.
- Outcome rows transcribed: 1,357 (extraction-outcomes.csv), each with values exactly as printed, a page or table reference, and a poolability call.
- Poolable rows: 527. Narrative-only rows: 830, each with its reason filed (commonest: percent change or group means with no variance printed, figure-only or supplement-only values, single item survey proportions with no poolable contrast).
- extraction_complete = yes: 31 studies. extraction_complete = no: 43 studies. In nearly every no case the main text is fully extracted and the gap is material the paper prints only in a supplement, an appendix, or a figure (named per study in the unparsed_or_thin_note field of extraction.csv). Six studies rest on a text that is not the full article: R0012 and R0131 (publisher abstract previews), R0265 and R0275 (subscription previews), R0277 and R0313 (abstract-length reports, as published), and R0209 (abstract only in the archived copy; the preprint licence does not permit archiving of the full text). R0209 yielded no outcome rows.
- Studies with no poolable row in any protocol outcome: 27. They enter the narrative synthesis only. List: R0012, R0029, R0030, R0077, R0078, R0131, R0155, R0165, R0173, R0179, R0191, R0209, R0255, R0256, R0265, R0273, R0278, R0281, R0312, R0313, R0316, R0331, R0353, R0355, R0373, R0426, R0548.

### Analysis datasets built from the poolable rows
- analysis-time.csv: 125 rows, 28 studies (documentation time 84 rows, after-hours time 41 rows).
- analysis-burnout.csv: 93 rows, 16 studies (workload 46, burnout 41, professional fulfillment 6).
- analysis-errors.csv: 63 rows, 10 studies (errors_other 25, errors_total 23, errors_omissions 9, errors_hallucinations 3, errors_wrong_inclusions 3; type-specific proportions with note denominators are scarce, most audits print counts per note or shares of errors).
- analysis-quality.csv: 79 rows, 17 studies (note quality scores, mostly PDQI-9 family instruments).
- Six further studies hold poolable rows only outside these four families (note length, time to closure, patient experience): R0048, R0112, R0232, R0240, R0245, R0287.

### Risk of bias mechanics
- Rows assessed: 138 study by outcome-group rows covering all 74 studies (RoB 2: 17 rows; ROBINS-I: 121 rows), filed in rob-assessments.csv with Pass A, Pass B and adjudicated judgements and a support line per domain.
- Domain disagreements between Pass A and Pass B: 185, counted field by field from rob-assessments.csv. 121 of 138 rows had at least one domain disagreement. By domain: D6 or RoB 2 D4 measurement 44, D5 missing data 39, D4 deviations (ROBINS-I) 24, D2 selection 26, D7 reported result 21, D1 confounding or randomisation 18, D3 classification 13. The commonest split was moderate against serious, 103 of the 185.
- Overall judgements differed between the passes in 32 rows. Adjudication moved the overall judgement away from Pass A in 8 rows and away from Pass B in 24 rows.
- Adjudicated overall, all rows: serious 94, moderate 24, some concerns 11, high 5, critical 3, low 1. Per study (worst group): serious 55, moderate 10, high 5, critical 2, some concerns 2, low 0. Full breakdown in rob-summary.md.
- Note on the batches' own disagreement fields: the free text disagreement notes in some batch files undercount the field by field comparison. The counts above come from the direct comparison of the filed Pass A and Pass B judgements, which is the count of record for the review.

## Prompt changes
- Version 1, 22 October 2026: first version, used for the search and title and abstract screening above. A mid-course fix to the screening procedures was made before the counted run and is part of version 1 as counted: publication type parts split on semicolons were checked as separate types, the words review and protocol in a title were treated as the review type bar, and a near-duplicate pass was added at deduplication. The counted run used the fixed procedures throughout, so the numbers above belong to one consistent pass.

## Disclosure line for the manuscript, RAISE 2025
A team of large language model roles (Muse Spark, Meta, October 2026) carried out the team tasks of this review under named roles and independence rules set in the protocol. The human author set the question and eligibility rules, and is accountable for every judgement, every checked number and the final text.
