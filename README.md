# Ambient AI Scribes Meta-Analysis: Documentation Time, After-Hours Work, Clinician Burnout, Note Quality, Note Errors and Hallucinations. A Cochrane-Level Systematic Review Built by an LLM Team

Author: Raphael Malikian, independent researcher, healthcare founder and operator, clinical AI builder.

Method in one line: Cochrane-level methods, a team of large language model roles in place of a human research team, and one human author who is accountable for every number in the finished review.

Repository: https://github.com/rtmalikian/ambient-ai-scribes-meta-analysis-clinical-documentation-burnout-note-errors

## Status

Stage 3 is complete as of 22 October 2026. This is a staged public release of work in progress, version 0.3.

- 157 reports were sought for retrieval.
- 83 full texts were assessed for eligibility.
- 74 studies are included.
- Data extraction is under way.
- Risk of bias assessment, synthesis and GRADE ratings are pending.

No pooled result exists yet, and this repository states none. No effect estimate, no summary of findings table and no GRADE rating will appear here until the extraction checks, risk of bias work and synthesis are done and signed off by the author.

Registration: the protocol was prepared for PROSPERO. The registration number is pending. The Zenodo DOI is pending. Neither number is stated here because neither exists yet.

## The question

Health systems have bought ambient AI scribes on the claim that the tools cut documentation work. This review asks whether that claim holds when the time and burnout outcomes are set against note error outcomes in the same review.

Research questions, from protocol.md:

- RQ1. What is the effect of ambient AI scribes on documentation time, measured from electronic health record audit logs or timed observation?
- RQ2. What is the effect on after-hours documentation time, often called pajama time?
- RQ3. What is the effect on clinician burnout, work exhaustion and professional fulfillment, measured on validated scales?
- RQ4. What is the effect on note quality, measured on a named instrument?
- RQ5. How often do ambient scribe notes contain omissions, hallucinations or fabrications, and wrong inclusions, per note audited?
- RQ6. Do effects differ by product, specialty, study design, vendor funding and follow-up length?

## PICO

| Element | Definition in the protocol |
| --- | --- |
| Population | Clinicians who document patient encounters in any specialty and any country: physicians, advanced practice clinicians such as nurse practitioners and physician assistants, and other documenting clinicians. Settings: outpatient, inpatient, emergency and virtual care, primary and secondary care. |
| Intervention | Ambient AI scribe: software that captures a clinical encounter by listening, with patient consent, and generates a draft clinical note for clinician review and signature, with no dictation step by the clinician. Named products in the protocol include Microsoft DAX Copilot and Dragon Ambient eXperience, Nabla, Abridge, and Ambience Healthcare products. Equivalent ambient products are eligible on the same test. |
| Comparator | Usual documentation, manual typing, dictation, speech recognition, human scribe, no scribe, or the same clinicians in a pre-implementation period. |
| Outcomes, critical | Documentation time. After-hours documentation time. Burnout and work exhaustion on validated scales. Note errors per note audited, in three types kept apart: omissions, hallucinations or fabrications, and wrong inclusions. |
| Outcomes, important | Note quality on a named instrument. Professional fulfillment. Time to note closure. Patient experience. Note length. |

Full eligibility rules, outcome definitions and time point rules sit in protocol.md, sections 3 and 4.

## PRISMA 2020 flow, Stage 3

Counts below are taken from prisma-stage3.md, which is built from retrieval-log.csv and fulltext-screening.csv. Counts from the earlier stages sit in search-log.md and screening.csv.

Identification and title and abstract screening, 22 October 2026:

- Records identified across all runs: 1049 (PubMed 385, Europe PMC 299, OpenAIRE run 1: 145, OpenAIRE run 2: 201, ClinicalTrials.gov 19).
- Duplicate records removed before screening: 482.
- Records screened at title and abstract: 567.
- Records excluded at title and abstract: 104.
- A strict second pass then set the full text set: 157 reports marked for retrieval.

Full text stage, Stage 3:

- Reports sought for retrieval: 157
- Reports not retrieved: 74
  - 65 records yielded no file at all: no free full text found through Europe PMC or PubMed Central full text, Unpaywall open access locations, publisher open access pages, or medRxiv full text, across three retrieval waves.
  - 9 more files first counted as retrieved turned out to hold no article text (7 Europe PMC JavaScript stub pages, 1 paywall landing page, 1 publisher abstract page) and were moved to not retrieved in substance.
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

No record was retrieved from a pirated source. No paywalled record was counted as assessed on the basis of its abstract, except the flagged records resolved in flagged-resolutions-stage3.md, where the basis is stated per record.

## The LLM team

A Cochrane review is normally written by a team. This review has one human author, so a team of large language model roles does the team tasks, set up with the same separations as the human team. The roles, from protocol.md section 6:

1. Information specialist. Builds the search string for each source, runs it or marks it run pending access, and records string, date and hit count in the search log.
2. Screener A. Works through every title and abstract alone and records include, exclude or maybe, with a reason for each exclude.
3. Screener B. Does the same work in a separate pass, with a separate prompt, and does not see Screener A calls until both passes are complete.
4. Adjudicator. Takes every record where A and B disagree and settles the call with a logged reason. Items it cannot settle go to the human author.
5. Extractor A. Extracts each included study on the piloted form.
6. Extractor B. Extracts the same studies alone, in a separate pass. The two sheets are compared field by field and every mismatch is logged and settled against the source document.
7. Risk of bias assessor pair. Two independent passes, RoB 2 for trials and ROBINS-I for non-randomised studies, per outcome. Disagreements go to the human author.
8. Statistician. Writes the meta-analysis code, runs it, and checks it a second way. Code and data are posted with the review.
9. GRADE assessor. Drafts the GRADE rating per outcome with the reason for each downgrade, or the reason none was made. The human author signs each rating.
10. Methods editor. Checks the finished manuscript against PRISMA 2020 and the Cochrane Handbook structure.

Independence rules in short form: the A and B passes run apart, neither prompt contains the other pass calls, comparison happens only in a merge step done by code, and the adjudicator does not see any author preference. Prompts, model name and version, and dates for each role sit in llm-team-log.md and prompts.md.

Mechanics reported so far, from llm-team-log.md. Title and abstract screening, 22 October 2026:

- Records screened: 567.
- Agreements: 439. Agreement rate: 0.7743.
- Cohen kappa: 0.6439.
- Disagreements: 128.
- Records flagged for the human author at that stage: 13.
- Final calls after adjudication: include 328, maybe 135, exclude 104.

The 21 records flagged at Stage 2 were resolved at the full text stage. Each resolution, with its basis, sits in flagged-resolutions-stage3.md.

Human oversight: Raphael Malikian set the review question and the eligibility rules in the protocol. He settles every item the adjudicator flags, every risk of bias disagreement and every GRADE rating, and he checks every extracted number that enters a pool against the source document before he signs off the final numbers. No number in the finished review rests on a model pass alone.

## Files in this repo

- protocol.md: the full protocol, version 1.0, 22 October 2026. Question, eligibility, outcomes, search methods, synthesis plan and GRADE plan.
- prospero-form.md: the PROSPERO registration form as prepared. Registration number pending.
- search-log.md: each search string as run, with date, hit count and retrieved count per source, plus the sources that were attempted and blocked and the sources not run in this pass.
- search-results.csv: every retrieved record after deduplication, with source named per row. 567 records.
- screening.csv: title and abstract screening calls.
- screening-stage2.csv: the strict second pass that set the 157 reports for full text retrieval.
- full-text-list-v2.md: the full text list at Stage 2.
- flagged-for-author-v2.md: the 21 records flagged for the author at Stage 2.
- retrieval-log.csv: retrieval outcome per report sought.
- fulltext-screening.csv: full text screening calls, with one reason per exclusion and the not assessed records named.
- prisma-stage3.md: the PRISMA 2020 flow counts at Stage 3, as quoted above.
- flagged-resolutions-stage3.md: how each of the 21 flagged records was resolved, with the basis stated per record.
- extraction-form.md: the piloted data extraction form.
- extraction.csv: the working extraction sheet for the included studies. Extraction is under way.
- rob-forms.md: risk of bias forms, RoB 2 and ROBINS-I templates.
- prompts.md: role prompts and decision procedures, version 1.
- llm-team-log.md: the log of the LLM team set up, agreement counts and adjudication outcomes. This log is data for the finished review.
- CITATION.cff: citation metadata so GitHub shows its cite button.
- LICENSE: Creative Commons Attribution 4.0 International (CC BY 4.0).

Retrieved publisher full texts are not in this repository. They are other authors' copyrighted papers. The screening and extraction files record what was read and what was taken from each report.

## Data and code availability

The search data, screening calls, retrieval log, full text calls and extraction sheet in this repository are the working record of the review at Stage 3. Analysis code in R will be added with the synthesis stage, and any reader will be able to rerun the analysis from the posted data once it lands. Files are released in stages as each stage completes, and this README is updated at each stage.

## Links

- GitHub repository: https://github.com/rtmalikian/ambient-ai-scribes-meta-analysis-clinical-documentation-burnout-note-errors
- PROSPERO record: pending. No link exists yet.
- Zenodo record and DOI: pending. No link exists yet.
- medRxiv record: not posted yet.

## Declarations

Funding: none. No grant, no sponsor, no industry support, no product access given in kind for this review.

Conflicts of interest: none. The author has no industry affiliation of any kind and is fully independent.

AI use note: this review was built with help from a team of large language model roles (Muse Spark, Meta, October 2026) working under the roles and separations set out in the protocol and logged in llm-team-log.md. The human author set the question and the eligibility rules, settles flagged items and disagreements, checks numbers against source documents, and is accountable for every judgement and for the final text. This follows the 2025 RAISE statement on responsible AI use in evidence synthesis.

Scope note: this is evidence synthesis and policy discussion only. It makes no clinical recommendation and no medication recommendation, and it gives no advice for the care of any individual patient.

## Licence

This work is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0). You may share and adapt the material for any purpose, provided you give appropriate credit to the author, provide a link to the licence, and indicate if changes were made. See the LICENSE file in this repository.

## How to cite

Malikian, Raphael (2026). Ambient AI Scribes Meta-Analysis: Documentation Time, After-Hours Work, Clinician Burnout, Note Quality, Note Errors and Hallucinations. A Cochrane-Level Systematic Review Built by an LLM Team. Version 0.3 (Stage 3). GitHub repository: https://github.com/rtmalikian/ambient-ai-scribes-meta-analysis-clinical-documentation-burnout-note-errors

A Zenodo DOI is pending and will be added here once the record exists. Until then, cite the GitHub repository URL above.

## Version history

- 0.3, 22 October 2026: Stage 3 release. Full text stage complete: 157 reports sought, 83 assessed, 74 studies included. Extraction under way. No pooled result.
- Earlier stages (protocol, search, title and abstract screening, strict second pass) are recorded in the files listed above, with dates in each file.
