# Ambient AI Scribes Meta-Analysis: Documentation Time, After-Hours Work, Clinician Burnout, Note Quality, Note Errors and Hallucinations. A Cochrane-Level Systematic Review Built by an LLM Team

**Author:** Raphael Malikian, independent researcher, healthcare founder and operator, clinical AI builder.

**Method in one line:** Cochrane Handbook version 6.5 methods, PRISMA 2020 reporting, one human author accountable for every number, and a team of large language model roles doing the team tasks a Cochrane group would do.

## Status: Stage 2 complete

This repository is published in stages, as the work is done. Each stage is uploaded when it is finished and checked, with its data files beside the text. The stage list below shows where the review stands today, 22 October 2026.

Done:

- Stage 1, protocol: a PROSPERO-ready protocol and a field by field PROSPERO form, with eligibility rules, outcomes, subgroups and analysis plans set before extraction.
- Stage 2, search: 1,049 records identified across PubMed (385), Europe PMC (299), OpenAIRE (346 across two runs) and ClinicalTrials.gov (19). OpenAlex and Semantic Scholar runs were blocked by rate limits and are logged as blocked. Strings for Embase, CINAHL, PsycINFO, Cochrane CENTRAL, Scopus, Web of Science and ACM Digital Library are prepared and marked as run pending access.
- Stage 2, deduplication: 482 duplicate records removed, leaving 567 records for screening.
- Stage 2, screening stage 1: two independent screening passes over 567 records, agreement rate 0.77, Cohen kappa 0.64, 128 disagreements adjudicated, 104 records excluded, 463 records passed on.
- Stage 2, screening stage 2: every one of the 463 abstracts read against the protocol rules, 306 records excluded, 157 reports sought for full text retrieval.
- Forms ready for the next stage: a 39 field extraction form and RoB 2 and ROBINS-I judgement templates.

Not done yet:

- Stage 3, full text retrieval, full text screening and extraction, is in progress.
- No pooled result exists at this stage. This README claims no result, and no number in this repository is a result of this review yet. The numbers above are counts of records and screening calls. Effect estimates named in the background section belong to the published studies cited there.
- No summary of findings table exists yet. It will be added at Stage 4, after extraction and risk of bias work.
- A PROSPERO registration number and a preprint DOI are pending. Placeholder lines in this README will be replaced with the record links when each record exists.

## The question

To assess the effects of ambient AI scribes, compared with usual documentation, dictation or manual typing, on documentation time, after-hours work, clinician burnout, note quality and note errors in outpatient and inpatient care.

An ambient AI scribe listens to a clinical encounter, with patient consent, and drafts a structured note that the clinician reviews, edits and signs. Products in scope include Microsoft DAX Copilot and Dragon Ambient eXperience, Nabla, Abridge and Ambience Healthcare products, and any equivalent tool that captures an encounter and drafts the note.

### PICO

| Part | What the protocol sets |
|---|---|
| Population | Clinicians who document patient encounters, any specialty, any country: physicians, advanced practice clinicians such as nurse practitioners and physician assistants, and other documenting clinicians, in outpatient, inpatient, emergency and virtual care |
| Intervention | Ambient AI scribe: software that captures a clinical encounter by listening, with consent, and generates a draft clinical note for clinician review and signature, with no dictation step. Dictation-only tools and typed prompt summary tools are out, unless a study reports an ambient arm apart |
| Comparator | Usual documentation, manual typing, dictation, speech recognition, human scribe, no scribe, or the same clinicians in a pre-implementation period |
| Critical outcomes | Documentation time from electronic health record audit logs or timed observation; after-hours documentation time; burnout and work exhaustion on a validated scale; note errors per note audited, split into omissions, hallucinations or fabrications, and wrong inclusions |
| Important outcomes | Note quality on a named instrument; professional fulfillment; time to note closure; patient experience where a study measured it; note length, reported as a cost signal |
| Study designs | Randomised trials including stepped wedge, non-randomised studies with a concurrent comparison, uncontrolled before and after studies synthesised apart from controlled studies, and note audit studies that grade a defined sample of notes and report a denominator in notes |

Full eligibility wording, outcome definitions and time point groups sit in [protocol.md](protocol.md).

## Why this review matters

Health systems bought these tools at enterprise scale before the evidence settled. Kaiser Permanente rolled one tool out to 7,260 physicians across 2,576,627 encounters (Kaiser Permanente Division of Research report of the TPMG rollout, 2023 to 2024). Menlo Ventures put ambient scribe spending at $600M in 2025, up 2.4 times on the year before, the largest single category in $1.4B of healthcare AI spending (Menlo Ventures, State of AI in Healthcare, 2025).

The synthesis behind that spending is thin. Zhao and colleagues published the one prior meta-analysis in 2025 in BMC Medical Informatics and Decision Making, covering artificial intelligence tools for clinical note creation in general: 23 studies, pooled standardised mean difference minus 0.71 for documentation burden, heterogeneity I squared 93.3 percent, and study quality described as generally low. It came out before the 2025 randomised trials, and it did not pool note errors beside time and burnout.

The field knows the gap is open. NEJM AI paired its December 2025 randomised trial reports with an editorial titled "AI Scribes Are Not Productivity Tools (Yet)". Regulators and system leaders have issued guidance that asks for local validation and error monitoring: NHS England ambient scribing guidance on 27 April 2025, and the Joint Commission and Coalition for Health AI responsible use guidance on 17 September 2025. Guidance can ask for a pooled estimate with a certainty rating. At the time of writing, no published review gives one for ambient scribes alone, with error burden pooled beside benefit. This review aims to supply that estimate, with its data and code in public.

## The LLM team

A Cochrane review is normally written by a group: a search specialist, two screeners who work apart, two extractors, a statistician, and editors who check method. This review has one human author. In place of that group it uses a team of large language model roles, set up with the same separations, and it reports how that team performed in numbers.

Roles:

| Role | Job |
|---|---|
| Information specialist | Builds and runs a search string per database, records string, date and hit count |
| Screener A | Calls every title and abstract include, exclude or maybe, alone, with a reason per exclude |
| Screener B | Same work in a separate pass with a separate prompt, with no sight of screener A calls until both passes end |
| Adjudicator | Settles every A and B disagreement with a logged reason, and flags items it cannot settle for the human author |
| Extractor A and extractor B | Extract each included study apart, on the same piloted form, for a field by field comparison |
| Risk of bias assessor pair | Two independent passes on RoB 2 for trials and ROBINS-I for non-randomised studies, per outcome |
| Statistician | Writes the meta-analysis code, runs it, and checks one pool by hand against the extraction sheet |
| GRADE assessor | Drafts the certainty rating per outcome, with the reason for each downgrade |
| Methods editor | Checks the finished manuscript against PRISMA 2020, MECIR style conduct standards and the Cochrane Handbook structure |

Independence rules, in short: A and B passes run apart, comparison happens in a merge step by code, the adjudicator sees both calls and both reasons, and prompt changes are versioned in the log. Raphael Malikian sets the question and the eligibility rules, settles every flagged item and every risk of bias and GRADE disagreement, checks every extracted number that enters a pool against its source document, and signs off the final numbers.

Mechanics so far, from the title and abstract stage: 567 records screened, agreement 439 records, agreement rate 0.7743, Cohen kappa 0.6439, disagreements 128 (97 maybe against include, 15 exclude against maybe, 13 include against exclude, 3 maybe against exclude). The 13 include against exclude records were flagged for the human author. Extraction discrepancy rates will be added when the extractor pair runs. Full log: [llm-team-log.md](llm-team-log.md). Prompts: [prompts.md](prompts.md).

## Repository contents

| File | What it holds |
|---|---|
| [concept-and-protocol.md](concept-and-protocol.md) | The concept paper: topic scoring, the gap, and the first protocol sketch |
| [protocol.md](protocol.md) | The PROSPERO-ready protocol, version 1.0, 22 October 2026 |
| [prospero-form.md](prospero-form.md) | The PROSPERO form, field by field, matching the protocol |
| [search-log.md](search-log.md) | Search string as run, date and hit count per source, with blocked sources logged as blocked |
| [search-appendix-pending.md](search-appendix-pending.md) | Ready to run strings for databases with access pending, each marked as such |
| [search-results.csv](search-results.csv) | The 567 deduplicated records: title, authors, year, sources, identifier, abstract, link |
| [screening.csv](screening.csv) | Stage 1 screening: screener A and B calls, reasons, adjudicated decision per record |
| [screening-stage2.csv](screening-stage2.csv) | Stage 2 strict screening of the 463 passed records, with a reason grounded in each abstract |
| [prisma-flow.md](prisma-flow.md) | PRISMA 2020 flow counts from the Stage 1 files |
| [stage2-prisma-update.md](stage2-prisma-update.md) | Updated PRISMA counts after Stage 2, with exclusions by reason |
| [full-text-list-v2.md](full-text-list-v2.md) | The 157 reports sought for full text retrieval, with design, reason, identifier and link |
| [flagged-for-author-v2.md](flagged-for-author-v2.md) | Records with a genuinely open question for the human author |
| [background-studies-stage2.md](background-studies-stage2.md) | Qualitative attitudes studies kept for the background and discussion, outside the synthesis |
| [llm-team-log.md](llm-team-log.md) | LLM team setup, agreement and kappa, disagreement types and adjudication outcomes |
| [extraction-form.md](extraction-form.md) | The piloted extraction form, 39 fields, with vendor role recorded per study |
| [rob-forms.md](rob-forms.md) | RoB 2 and ROBINS-I judgement templates, per outcome, with confounders set in advance |
| [prompts.md](prompts.md) | Screener A, screener B and adjudicator prompts, version 1 |
| [github-publication-plan.md](github-publication-plan.md) | The publication plan for this repository: name, description, topics and staged release plan |
| [CITATION.cff](CITATION.cff) | Citation file, so GitHub shows a cite button for this work |
| [LICENSE](LICENSE) | Creative Commons Attribution 4.0 International licence text |

Copyrighted publisher full texts are not in this repository and never will be. Retrieval notes and extraction sheets will name each source so a reader can find the same text through a library.

## Staged roadmap

- Stage 1, protocol. Done. Protocol and PROSPERO form in this repository.
- Stage 2, search and screening. Done. Search log, record set, both screening passes and PRISMA counts in this repository.
- Stage 3, full text and extraction. In progress. Retrieval log, full text screening calls with one reason per exclude, the extraction sheet and the risk of bias judgements will be uploaded at this stage.
- Stage 4, meta-analysis and GRADE. Random effects pools in R for time, after-hours work and burnout, proportions for each error type kept apart, subgroup and sensitivity runs as set in the protocol, and a summary of findings table with at most seven outcomes. Analysis code and figures will be uploaded at this stage.
- Stage 5, manuscript, preprint and journal submission. Full manuscript in Markdown and PDF, Zenodo preprint record, medRxiv record where the framing fits, and one submission to a journal that charges no fee, by the subscription route. A conference abstract version will be prepared at the same stage.

Each stage will land as its own commit, signed off by the author, so the history of this repository reads as the history of the review.

## Declarations

Funding: none. No grant, no sponsor, no industry support, no product access given in kind for this review.

Conflicts of interest: none. The author has no industry affiliation of any kind and is fully independent.

AI use, RAISE 2025: a team of large language model roles (Muse Spark, Meta, October 2026) carried out the team tasks of this review under named roles and independence rules set in the protocol, following the 2025 RAISE statement on responsible AI use in evidence synthesis from Cochrane, Campbell, JBI and the Collaboration for Environmental Evidence. The human author set the question and the eligibility rules and is accountable for every judgement, every checked number and the final text. Journals and conferences that ask for an AI use statement will get these same facts.

Scope: this work is evidence synthesis and policy discussion only. It gives no clinical advice, no medication advice and no advice for the care of any individual patient. It makes no claim about any single product beyond what the included studies report.

## How to cite

Cite this repository through [CITATION.cff](CITATION.cff), which GitHub reads for its cite button:

Malikian R. Ambient AI Scribes Meta-Analysis: Documentation Time, After-Hours Work, Clinician Burnout, Note Quality, Note Errors and Hallucinations. A Cochrane-Level Systematic Review Built by an LLM Team. Version 0.2-stage2, 2026.

DOI: pending. A Zenodo DOI will be added here and to CITATION.cff when the preprint record exists. PROSPERO registration number: pending, to be added in the same way.

## Licence

Text and data in this repository are published under the Creative Commons Attribution 4.0 International licence, CC BY 4.0. The full licence text is in [LICENSE](LICENSE). Analysis code added at Stage 4 will carry its licence in its own folder.

## Contact

Raphael Malikian, rtmalikian@gmail.com, GitHub [@rtmalikian](https://github.com/rtmalikian). Corrections and missed studies are welcome as issues in this repository. A correction that changes a number will be logged in the repository history with its reason.
