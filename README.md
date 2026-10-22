# Ambient AI Scribes Meta-Analysis: Documentation Time, After-Hours Work, Clinician Burnout, Note Quality, Note Errors and Hallucinations. A Cochrane-Level Systematic Review Built by an LLM Team

**Author:** Raphael Malikian, independent researcher, healthcare founder and operator, clinical AI builder.

**Method in one line:** Cochrane Handbook version 6.5 (2024) methods, PRISMA 2020 reporting, one human author accountable for every number, and a team of large language model roles doing the team tasks a Cochrane group would do.

**Status: complete, version 1.0, 22 October 2026.** The manuscript is in this repository in Markdown and PDF, with the analysis code, the data behind every pool, and a v1.0 release. This review follows Cochrane methods. It is not a Cochrane review and has not been submitted to Cochrane.

## Headline results

| Outcome | Pooled effect | Studies | GRADE certainty |
|---|---|---|---|
| Documentation time | SMD -0.38 (95% CI -0.53 to -0.24), I squared 83.4%; controlled studies SMD -0.52; relative change -18.9% (-25.9% to -11.9%) | k 13 for SMD, k 6 controlled, k 15 for relative change | Low |
| After-hours documentation time | SMD -0.25 (95% CI -0.52 to 0.01), before-after studies only | k 6 | Very low |
| Burnout and work exhaustion | Randomised trials SMD -0.44 (-0.61 to -0.28) | k 2 trials | Moderate |
| Note quality | SMD +0.57 (0.51 to 0.64) | k 6 | Low |
| Notes with at least one error | 59.8% (37.9% to 78.4%) of AI drafted notes | k 2 | Very low |
| Error types, one study (Taylor 2026, 356 notes) | Omissions 18.0% of notes, hallucinations 11.5%, wrong inclusions 9.3% | 1 study | Very low |

Full GRADE reasoning per outcome sits in [summary-of-findings.md](summary-of-findings.md). Every pooled number in this table comes from [meta_analysis.py](meta_analysis.py) run on [selected-effects.csv](selected-effects.csv); the run output is in [analysis-results.md](analysis-results.md) and [analysis-results.json](analysis-results.json).

## Plain language summary

A standalone summary written for patients, clinic managers and anyone else who wants the findings without the statistics sits in [plain-language-summary.md](plain-language-summary.md). It gives the same numbers as the manuscript: note time down by about a fifth on average with wide spread between settings, evening work unproven, work exhaustion eased in the two randomised trials, and error rates of about 18 in 100 notes for omissions, 12 in 100 for content that was never said, and 9 in 100 for material that belonged in a different note.

## The limits, in plain sight

- 55 of the 74 included studies sit at serious risk of bias on their worst outcome group, most of them uncontrolled studies of self-selected early users.
- The prediction interval for documentation time (-0.84 to 0.07) crosses zero. The class average is a fall of about a fifth; a new setting could see little or no gain.
- 74 of the 157 reports sought for full text were not retrieved through lawful open routes, and eight database searches named in the protocol (Embase, CINAHL, PsycINFO, Cochrane CENTRAL, Scopus, Web of Science, ACM Digital Library, WHO ICTRP) were not run because no licensed access was available. Their strings sit in [search-appendix-pending.md](search-appendix-pending.md), marked as not run.
- No PROSPERO registration number was issued before this analysis was run. The protocol record route is OSF. The manuscript states this in its registration section, and the protocol, search log and timestamps are in this repository for checking.

## Structured abstract

**Background.** Health systems have bought ambient artificial intelligence (AI) scribes at scale. One system reported a rollout to 7,260 physicians across 2,576,627 encounters. The products listen to a consultation and draft the note. Buyers were promised less documentation time, less after-hours work and less clinician burnout. The primary studies behind those promises are mostly small, single site and uncontrolled, and the error burden of AI drafted notes is rarely reported in the same papers as the time gains.

**Objectives.** To assess the effects of ambient AI scribes, compared with usual documentation, on documentation time, after-hours documentation time, burnout and work exhaustion, workload, note quality and note errors.

**Search methods.** PubMed, Europe PMC, OpenAIRE (two title runs) and ClinicalTrials.gov were searched on 22 October 2026 for records from 1 January 2019, with no language limit. OpenAlex and Semantic Scholar were attempted and blocked by rate limits. Embase, CINAHL, PsycINFO, Cochrane CENTRAL, Scopus, Web of Science, ACM Digital Library and WHO ICTRP were not run, because no licensed access was available; their strings are printed in an appendix, marked as not run.

**Selection criteria.** Randomised trials, non-randomised controlled studies, uncontrolled before-after studies, interrupted time series and note audit studies of ambient AI scribes used by documenting clinicians, reporting at least one protocol outcome. A team of large language model roles screened, extracted and assessed risk of bias in duplicate passes under independence rules, with the human author accountable for every judgement. Agreement at title and abstract screening was 0.7743 (Cohen kappa 0.6439).

**Data collection and analysis.** Risk of bias was assessed with RoB 2 and ROBINS-I per outcome. Random effects meta-analysis (REML, Hartung-Knapp intervals where k was 3 or more) pooled standardised mean differences for time, burnout, workload and quality, and logit transformed proportions for note errors. Before-after studies were pooled apart from controlled studies. Certainty was rated with GRADE.

**Main results.** The search found 1,049 records; 567 were screened after deduplication, 157 reports were sought, 83 were assessed and 74 studies were included. Documentation time fell: standardised mean difference (SMD) -0.52 (95% CI -0.88 to -0.15, k 6) in controlled studies and -0.31 (-0.43 to -0.19, k 7) in before-after studies, with high heterogeneity (I squared 88.2% and 64.2%); on a percentage scale the pooled change was -18.9% (-25.9% to -11.9%, k 15). Certainty: low. After-hours time gave SMD -0.25 (-0.52 to 0.01, k 6, all before-after); no controlled estimate exists. Certainty: very low. Burnout and work exhaustion gave SMD -0.44 (-0.61 to -0.28, k 2 randomised trials), equal to -0.36 points on the Professional Fulfillment Index work exhaustion composite. Certainty: moderate for the trial estimate. Workload gave SMD -1.46 across seven studies, but the one study at lower risk of bias gave -0.39. Certainty: very low. Note quality scores rose, SMD 0.57 (0.51 to 0.64, k 6). Certainty: low. For note errors, one study of 356 notes found omissions in 18.0% of notes, hallucinations in 11.5% and wrong inclusions in 9.3%; a two study pool of notes with at least one error gave 59.8% (37.9% to 78.4%). Certainty: very low. Professional fulfilment showed no clear change. Certainty: very low.

**Authors' conclusions.** Ambient scribes cut documentation time by about a fifth on average and ease work exhaustion over 30 to 90 days. The average hides wide spread between settings, the after-hours claim rests on uncontrolled studies alone, and AI drafts carry an error load that makes clinician review part of the intervention rather than an afterthought. Longer trials, controlled after-hours measurement and standardised error audits would change these ratings more than further pilot studies of the same design.

## PRISMA 2020 counts

- Records identified: 1,049 (PubMed 385, Europe PMC 299, OpenAIRE 346 across two runs, ClinicalTrials.gov 19)
- Duplicates removed: 482, leaving 567 records screened
- Stage 1 screening excluded 104; Stage 2 strict abstract screening excluded 306 of the 463 passed on
- Reports sought for full text: 157
- Reports not retrieved: 74
- Reports assessed: 83; excluded at full text: 8; awaiting classification: 1
- Studies included: 74

Stage files: [prisma-flow.md](prisma-flow.md), [stage2-prisma-update.md](stage2-prisma-update.md) and the Stage 3 update in the review record. Search strings as run: [search-log.md](search-log.md).

## The LLM team

A Cochrane review is team work: an information specialist, two screeners working apart, two extractors, a statistician and editors. This review has one human author, and a team of large language model roles (Muse Spark, Meta, October 2026) filled those seats under independence rules: screeners who did not see each other's calls, extractors whose sheets were compared field by field, and risk of bias passes that disagreed in the open.

Numbers from the team log ([llm-team-log.md](llm-team-log.md)): screeners agreed on 439 of 567 records, agreement 0.7743, Cohen kappa 0.6439; 128 disagreements went to adjudication and 13 records were flagged for the human author. Extraction produced 1,357 outcome rows, 527 of them poolable. The risk of bias pair disagreed on 185 domain judgements across 138 study by outcome rows, and adjudication moved the overall judgement in 32 rows. Raphael Malikian set the question and the eligibility rules, settled the flagged items and signs off every number, following the 2025 RAISE statement on AI use in evidence synthesis.

## Repository contents

| File | What it holds |
|---|---|
| [manuscript.md](manuscript.md) and [manuscript.pdf](manuscript.pdf) | The finished review, version 1.0: 9,287 words of main text, 43 pages, 8 figures |
| [plain-language-summary.md](plain-language-summary.md) | The findings in plain words, for patients and managers: what scribes are, what the review found, and the weak spots in the studies |
| [summary-of-findings.md](summary-of-findings.md) | GRADE table for seven outcomes, with the reason for every downgrade |
| [analysis-results.md](analysis-results.md) and [analysis-results.json](analysis-results.json) | Every pool, subgroup and sensitivity run, as produced by the code |
| [meta_analysis.py](meta_analysis.py) | The analysis code, rerunnable on the posted data |
| [selected-effects.csv](selected-effects.csv) | The 63 analysis rows that entered the pools, one per study per outcome, each with its derivation |
| [characteristics-of-included-studies.csv](characteristics-of-included-studies.csv) | Characteristics of the 74 included studies |
| [extraction-outcomes.csv](extraction-outcomes.csv) | 1,357 extracted outcome rows, values as printed in the source papers |
| [rob-assessments.csv](rob-assessments.csv) and [rob-summary.md](rob-summary.md) | Risk of bias judgements, two passes and adjudication, 138 rows |
| [forest-time-smd.png](forest-time-smd.png), [forest-time-relative.png](forest-time-relative.png), [forest-afterhours-smd.png](forest-afterhours-smd.png), [forest-burnout-smd.png](forest-burnout-smd.png), [forest-workload-smd.png](forest-workload-smd.png), [forest-quality-smd.png](forest-quality-smd.png), [forest-errors-any.png](forest-errors-any.png), [funnel-time-smd.png](funnel-time-smd.png) | Forest and funnel plots for the pooled outcomes |
| [qa-note.md](qa-note.md) | Stage 5 quality checks: de-AI audit, numbers audit, rendering checks |
| [protocol.md](protocol.md) and [prospero-form.md](prospero-form.md) | The protocol and the prepared PROSPERO form |
| [concept-and-protocol.md](concept-and-protocol.md) | The concept paper: topic scoring, the gap, the first protocol sketch |
| [search-log.md](search-log.md), [search-appendix-pending.md](search-appendix-pending.md), [search-results.csv](search-results.csv) | Search strings, dates, hit counts, blocked sources, and the record set |
| [screening.csv](screening.csv), [screening-stage2.csv](screening-stage2.csv) | Both screening passes, per record calls and reasons |
| [prisma-flow.md](prisma-flow.md), [stage2-prisma-update.md](stage2-prisma-update.md) | PRISMA counts by stage |
| [full-text-list-v2.md](full-text-list-v2.md), [flagged-for-author-v2.md](flagged-for-author-v2.md), [background-studies-stage2.md](background-studies-stage2.md) | Full text list, author flags, background studies |
| [prisma-stage3.md](prisma-stage3.md), [retrieval-log.csv](retrieval-log.csv), [fulltext-screening.csv](fulltext-screening.csv), [flagged-resolutions-stage3.md](flagged-resolutions-stage3.md) | Stage 3 flow counts, retrieval outcome per report, full text calls, flagged record resolutions |
| [llm-team-log.md](llm-team-log.md), [prompts.md](prompts.md) | Team setup and mechanics, prompt versions |
| [extraction-form.md](extraction-form.md), [rob-forms.md](rob-forms.md) | The piloted extraction form and risk of bias templates |
| [github-publication-plan.md](github-publication-plan.md) | Name, description, topics and staged release plan for this repository |
| [CITATION.cff](CITATION.cff) | Citation file, so GitHub shows a cite button |
| [LICENSE](LICENSE) | Creative Commons Attribution 4.0 International licence text |

Copyrighted publisher full texts are not in this repository and never will be. The extraction sheets name each source so a reader can find the same text through a library.

## Declarations

Funding: none. No grant, no sponsor, no industry support, no product access given in kind for this review.

Conflicts of interest: none. The author has no industry affiliation of any kind and is fully independent.

AI use, RAISE 2025: a team of large language model roles (Muse Spark, Meta, October 2026) carried out the team tasks of this review under named roles and independence rules set in the protocol, following the 2025 RAISE statement on responsible AI use in evidence synthesis from Cochrane, Campbell, JBI and the Collaboration for Environmental Evidence. The human author set the question and the eligibility rules and is accountable for every judgement, every checked number and the final text.

Scope: this work is evidence synthesis and policy discussion only. It gives no clinical advice, no medication advice and no advice for the care of any individual patient.

## How to cite

Cite this repository through [CITATION.cff](CITATION.cff), which GitHub reads for its cite button:

Malikian R. Ambient AI Scribes Meta-Analysis: Documentation Time, After-Hours Work, Clinician Burnout, Note Quality, Note Errors and Hallucinations. A Cochrane-Level Systematic Review Built by an LLM Team. Version 1.0, 2026.

DOI: pending. A Zenodo DOI will be added here and to CITATION.cff when the preprint record exists. Registration: no PROSPERO number was issued before the analysis; the protocol record route is OSF.

## Licence

Text and data in this repository are published under the Creative Commons Attribution 4.0 International licence, CC BY 4.0. The full licence text is in [LICENSE](LICENSE).

## Contact

Raphael Malikian, rtmalikian@gmail.com, GitHub [@rtmalikian](https://github.com/rtmalikian). Corrections and missed studies are welcome as issues in this repository. A correction that changes a number will be logged in the repository history with its reason.
