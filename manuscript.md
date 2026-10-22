# Ambient artificial intelligence scribes for clinical documentation: effects on documentation time, after-hours work, clinician burnout, note quality and note errors

## A systematic review and meta-analysis

**Raphael Malikian**
Independent researcher. Healthcare founder and operator; clinical AI builder.

Version 1.0, 22 October 2026. This review follows Cochrane Handbook methods (version 6.5, 2024) and PRISMA 2020 reporting. It is a Cochrane level review. It is not a Cochrane review and has not been submitted to Cochrane.

**Registration.** Protocol prepared for PROSPERO on 22 October 2026. No registration number had been issued when this analysis was run. The protocol, search log, screening files, extraction sheets and analysis code sit in the review repository named in the data availability statement.

**Funding.** None. **Conflicts of interest.** None. The author has no industry affiliation and received no product access, payment or support from any scribe vendor.

---

## Abstract

**Background.** Health systems have bought ambient artificial intelligence (AI) scribes at scale. One system reported a rollout to 7,260 physicians across 2,576,627 encounters. The products listen to a consultation and draft the note. Buyers were promised less documentation time, less after-hours work and less clinician burnout. The primary studies behind those promises are mostly small, single site and uncontrolled, and the error burden of AI drafted notes is rarely reported in the same papers as the time gains.

**Objectives.** To assess the effects of ambient AI scribes, compared with usual documentation, on documentation time, after-hours documentation time, burnout and work exhaustion, workload, note quality and note errors.

**Search methods.** PubMed, Europe PMC, OpenAIRE (two title runs) and ClinicalTrials.gov were searched on 22 October 2026 for records from 1 January 2019, with no language limit. OpenAlex and Semantic Scholar were attempted and blocked by rate limits. Embase, CINAHL, PsycINFO, Cochrane CENTRAL, Scopus, Web of Science, ACM Digital Library and WHO ICTRP were not run, because no licensed access was available; their strings are printed in an appendix, marked as not run.

**Selection criteria.** Randomised trials, non-randomised controlled studies, uncontrolled before-after studies, interrupted time series and note audit studies of ambient AI scribes used by documenting clinicians, reporting at least one protocol outcome. A team of large language model roles screened, extracted and assessed risk of bias in duplicate passes under independence rules, with the human author accountable for every judgement. Agreement at title and abstract screening was 0.7743 (Cohen kappa 0.6439).

**Data collection and analysis.** Risk of bias was assessed with RoB 2 and ROBINS-I per outcome. Random effects meta-analysis (REML, Hartung-Knapp intervals where k was 3 or more) pooled standardised mean differences for time, burnout, workload and quality, and logit transformed proportions for note errors. Before-after studies were pooled apart from controlled studies. Certainty was rated with GRADE.

**Main results.** The search found 1,049 records; 567 were screened after deduplication, 157 reports were sought, 83 were assessed and 74 studies were included. Documentation time fell: standardised mean difference (SMD) -0.52 (95% CI -0.88 to -0.15, k 6) in controlled studies and -0.31 (-0.43 to -0.19, k 7) in before-after studies, with high heterogeneity (I squared 88.2% and 64.2%); on a percentage scale the pooled change was -18.9% (-25.9% to -11.9%, k 15). Certainty: low. After-hours time gave SMD -0.25 (-0.52 to 0.01, k 6, all before-after); no controlled estimate exists. Certainty: very low. Burnout and work exhaustion gave SMD -0.44 (-0.61 to -0.28, k 2 randomised trials), equal to -0.36 points on the Professional Fulfillment Index work exhaustion composite. Certainty: moderate for the trial estimate. Workload gave SMD -1.46 across seven studies, but the one study at lower risk of bias gave -0.39. Certainty: very low. Note quality scores rose, SMD 0.57 (0.51 to 0.64, k 6). Certainty: low. For note errors, one study of 356 notes found omissions in 18.0% of notes, hallucinations in 11.5% and wrong inclusions in 9.3%; a two study pool of notes with at least one error gave 59.8% (37.9% to 78.4%). Certainty: very low. Professional fulfilment showed no clear change. Certainty: very low.

**Authors' conclusions.** Ambient scribes cut documentation time by about a fifth on average and ease work exhaustion over 30 to 90 days. The average hides wide spread between settings, the after-hours claim rests on uncontrolled studies alone, and AI drafts carry an error load that makes clinician review part of the intervention rather than an afterthought. Longer trials, controlled after-hours measurement and standardised error audits would change these ratings more than further pilot studies of the same design.

## Plain language summary

An ambient AI scribe is a program that listens to a medical consultation, with the patient's consent, and writes a draft of the clinical note. The doctor or nurse then checks the draft, fixes it and signs it. Health systems have spent heavily on these tools. One market report put spending on ambient scribes at $600M in 2025.

This review found 74 studies of these tools and combined their results. The tools cut the time clinicians spend writing notes by about a fifth on average. Two randomised trials found that scores for work exhaustion, one part of burnout, fell by about a third of a standard deviation over one to three months. Studies of after-hours work, the note writing clinicians do at home in the evening, point to a smaller load, but every study of that outcome lacked a comparison group, so the review rates that evidence very low.

The drafts contain errors. In the largest audit that counted error types, 18 of every 100 AI drafted notes missed something that was said in the consultation, about 12 in 100 contained something that was never said, and about 9 in 100 contained material that did not belong in that note. Notes also scored higher on quality rating scales. A higher score and a real error can sit in the same note, which is why checking the draft stays part of the job.

Most studies were small, ran for one to three months, and had design weaknesses: the clinicians who volunteered to use the tools were compared with everyone else, or with their own past, and keen users report better results. The findings are a good reason to keep measuring these tools properly. They are not proof that every product, in every clinic, will save the same time.

## Summary of findings

Population: clinicians who document patient encounters. Intervention: ambient AI scribe. Comparison: usual documentation or the pre-implementation period. Follow-up: mostly 30 to 90 days. Full GRADE reasoning for each row sits in the certainty section of the results and in the review files.

| Outcome | Pooled effect | Studies (analysis units) | GRADE certainty |
|---|---|---|---|
| Documentation time | SMD -0.38 (95% CI -0.53 to -0.24) all studies; controlled -0.52, before-after -0.31; percentage change -18.9% (-25.9% to -11.9%) | 13 (12,900) for SMD; 15 for percentage | Low |
| After-hours documentation time | SMD -0.25 (-0.52 to 0.01), before-after studies only | 6 (1,003) | Very low |
| Burnout and work exhaustion | SMD -0.34 (-0.53 to -0.15) all studies; randomised trials -0.44 (-0.61 to -0.28) | 4 (682); trials 257 | Moderate (trial estimate); low (all studies) |
| Workload and task load | SMD -1.46 (-2.13 to -0.78); the one lower risk study -0.39 (-0.70 to -0.09) | 7 (975) | Very low |
| Note quality | SMD 0.57 (0.51 to 0.64); PDQI family only 0.55 (0.49 to 0.61) | 6 (1,193) | Low |
| Notes with at least one error | 59.8% (37.9% to 78.4%), two studies with different error definitions. Type specific rates, one study: omissions 18.0% of notes, hallucinations 11.5%, wrong inclusions 9.3% | 2 (93 notes); type specific 1 (356 notes) | Very low |
| Professional fulfilment | Not pooled. One trial: +0.14 points (0.004 to 0.28) on the PFI fulfilment composite. One before-after study: threshold proportions 37.5% before, 41.7% at 84 days | 2 | Very low |

Analysis units differ by study (clinicians, encounters, appointments, notes, paired periods). Counts are the units each study analysed, summed.

## Background

### The documentation load

Clinical notes are the record of care, the billing document and the handover tool, and they take a large share of the working day to produce. The studies in this review measured baseline loads of 5 to 15 minutes of note time per encounter and several hours of electronic health record (EHR) work per week outside scheduled hours. That load is one of the most cited reasons clinicians give for exhaustion and for leaving practice. Any tool that credibly cuts it will be bought. The question for a buyer is whether the cut is real, how large it is, and what it costs in checking work and errors.

Adoption has run ahead of evaluation. Kaiser Permanente and The Permanente Medical Group reported rolling an ambient scribe out to 7,260 physicians across 2,576,627 encounters. Menlo Ventures estimated ambient scribe spending at $600M in 2025, the largest single slice of $1.4B in healthcare AI spending that year, up 2.4 times on the year before. The American Medical Association reported AI use by 66% of surveyed physicians in 2024, against 38% in 2023; scribes are a large part of that rise. Enterprise contracts are being signed on the strength of pilot studies, most of them small, short and run by the services that chose the tool.

### What an ambient scribe is, and how it is meant to work

An ambient scribe captures a consultation through a microphone, with patient consent, separates the speakers, transcribes the conversation and drafts a structured note. The clinician reads the draft, edits it and signs it. The mechanism has three places where time can be saved and three where it can be lost. Typing during and after the consultation falls. Recall work falls, because the draft holds the conversation. Structuring work falls, because the draft arrives in note format. Against that, reading and checking work rises. Correction work rises when the draft is wrong. Attention during the consultation changes shape: clinicians in several included studies described speaking for the microphone, spelling out findings they would once have typed silently.

The products differ. Some are built by EHR vendors, some by standalone companies, some inside health systems. Draft quality, latency, specialty tuning and the review interface all vary, and the models underneath them change during the study periods themselves. A class level claim, "ambient scribes save time", can be true on average and wrong for a named product in a named clinic. This review therefore pools the class and tests product subgroups where the numbers allow, rather than treating the class average as a purchasing answer.

### What the studies showed before this review

One prior meta-analysis exists. Zhao (2025) pooled AI tools for clinical note creation in general: 23 studies, a standardised mean difference of -0.71 for documentation burden, -0.72 for time, and heterogeneity of I squared 93.3%, with study quality described as generally low. Zhao's set covered AI documentation tools broadly, not ambient scribes alone, and it predates the 2025 randomised trials. No published synthesis has set the time and burnout outcomes against error outcomes for the same tools. A buyer reading Zhao learns that documentation burden fell. They learn nothing about what arrived in the notes in exchange.

The two 2025 trials in NEJM AI show why product level reading matters. Lukac (2025) randomised 238 physicians to DAX Copilot, Nabla or usual documentation. In December, time in note fell 9.5% with Nabla (p 0.02) and 1.7% with DAX, a difference that did not reach significance. Same trial, same clinic system, same outcome: one product cut note time and one did not. Afshar (2025), a stepped wedge trial across two systems, found work exhaustion and interpersonal disengagement scores 0.44 points lower in scribe periods. Both trials are inside this review's pools, and the pools can be read against their individual results in the forest plots.

The error side of the ledger comes from audits. Taylor (2026) checked 356 AI drafted notes against the consultation record: omissions in 18.0% of notes, hallucinations in 11.5%, wrong inclusions in 9.3%, and an error rated severity 4 or 5 in 5.3%. Draper (2025), working in UK primary care, graded error severity and set out what an uncorrected error could do in practice. Bergman (2026) showed that the measured error rate depends on who or what looks for the errors: on the same notes, clinician adjudication found 6.2% of AI notes carrying at least one error of Critical or High grade, while a calibrated automated reviewer found 24.4%. Time saved and vigilance added are the same intervention read from two ends, and any synthesis that reports one without the other is half a result.

### Why an LLM team review

A Cochrane review is team work: an information specialist, two screeners working apart, two extractors, a statistician and editors. This review has one human author. It used a team of large language model (LLM) roles in place of that team, with the separations the human team would have: screeners who did not see each other's calls, extractors whose sheets were compared field by field, risk of bias passes that disagreed in the open, and an accountable human author who set the question, settled the flagged items and signs the result. The 2025 RAISE statement from Cochrane, Campbell, JBI and the Collaboration for Environmental Evidence sets the terms for this: state the tool, the purpose and the checks. This review goes one step further and reports the team's agreement numbers as results, so a reader can judge the substitute team on its numbers: kappa 0.6439 at screening, 185 risk of bias domain disagreements across 138 assessed rows, adjudication moving the overall judgement in 32 rows. Whether this method holds up is part of what the review tests.

Guidance has also moved ahead of the pooled evidence. NHS England issued guidance on ambient scribing technology on 27 April 2025, covering device status, safety cases and human review of drafts. The Joint Commission and the Coalition for Health AI issued responsible use guidance on 17 September 2025, asking for local validation and monitoring. The FDA Digital Health Advisory Committee meeting of 6 November 2025 took up hallucinations and model drift as risks that need controls. Each document asks, in its own words, for local measured evidence on accuracy and effect. Until now there has been no pooled, certainty graded synthesis to point at.

## Objectives

To assess the effects of ambient AI scribes, compared with usual documentation, dictation or manual typing, on documentation time, after-hours work, clinician burnout and work exhaustion, workload, note quality and note errors in outpatient and inpatient care, and to report how a team of LLM roles performed the team tasks of a Cochrane level review under human accountability.

## Methods

### Differences between protocol and review

Five differences are declared. First, the protocol named Embase, CINAHL, PsycINFO, Cochrane CENTRAL, Scopus, Web of Science, ACM Digital Library and WHO ICTRP as sources; no licensed access was available in the environment used, so those searches were not run. Their strings are printed in Appendix B, marked as not run, and the gap is treated as a limitation, not passed over. Second, the protocol's statistician section named R as the analysis language; the analysis was written and run in Python (pandas, numpy, scipy, matplotlib), with the same models specified. The code is public with the review. Third, the protocol set prediction intervals where ten or more studies pool; this review reports a prediction interval for pools with three or more studies and marks it not estimable at k 2, because the spread of effects is a central finding and hiding it in small pools would mislead. Fourth, title and abstract screening ran in two steps: a first pass that proved too permissive, then a strict second pass that read each abstract against the eligibility rules. Both steps and their counts are reported. Fifth, the pre-specified subgroups for specialty, clinician type and follow-up length could not be run: the analysis rows do not carry poolable numbers in those strata. The design, product and vendor subgroups were run with interaction tests.

### Eligibility criteria

**Studies.** Randomised trials including stepped wedge designs; non-randomised studies with a concurrent comparison; uncontrolled before-after studies and interrupted time series, synthesised apart from controlled studies; note audit studies grading a defined sample of scribe notes against the encounter record, audio or a human reference note, with a denominator in notes. Simulation studies entered only where the graded unit was the generated note (quality or errors), not where the outcomes were clinician time or workload measured inside simulated encounters. Reviews, editorials, protocols without results, qualitative studies and vendor white papers were excluded from the synthesis; qualitative studies were kept as background.

**Participants.** Clinicians who document patient encounters in any specialty and country: physicians, advanced practice clinicians and other documenting clinicians. Studies of students, patients or administrators alone were excluded.

**Intervention.** An ambient AI scribe: software that listens to an encounter, with consent, and drafts a note for clinician review and signature, with no dictation step. Dictation and speech recognition tools, prompt based summarisation of typed text, human scribes without AI generation, and coding or inbox tools were excluded.

**Comparisons.** Usual documentation, manual typing, dictation, speech recognition, human scribe, no scribe, or a pre-implementation period.

**Outcomes.** Critical: documentation time; after-hours documentation time; burnout and work exhaustion on a named scale; note errors per note, split into omissions, hallucinations or fabrications, and wrong inclusions. Important: note quality on a named instrument; professional fulfilment; workload and task load; time to note closure; patient experience; note length.

**Reports.** 1 January 2019 to 22 October 2026. No language limit at search. Journal articles, published trial results and preprints with original data. Preprints are flagged and removed in a sensitivity analysis.

### Search methods

Searches ran on 22 October 2026. PubMed returned 385 records for the string in Appendix A. Europe PMC returned 299. OpenAIRE returned 145 for the title words "ambient scribe" and 201 for "AI scribe"; OpenAIRE indexes Crossref records and stood in for a Crossref phrase search, which its interface cannot run. ClinicalTrials.gov returned 19. Total retrieved: 1,049. OpenAlex and Semantic Scholar were attempted and returned HTTP 429 rate limit errors; both are logged as attempted and blocked, not as searched. Deduplication (DOI, then normalised title, then a near duplicate pass) removed 482 records, leaving 567 for screening.

### Selection of studies, and the LLM team

The review team was a set of LLM roles (Muse Spark, Meta, October 2026) working to the protocol's role definitions: information specialist, Screener A, Screener B, adjudicator, Extractor A, Extractor B, a risk of bias assessor pair, statistician, GRADE assessor and methods editor. Screener A and Screener B worked apart, with separate decision procedures and no sight of each other's calls. Their calls agreed on 439 of 567 records (agreement rate 0.7743, Cohen kappa 0.6439). The 128 disagreements went to the adjudicator; 13 records where one screener said include and the other exclude were flagged for the human author.

Stage 1 passed 463 records as include or maybe. That pass was too loose: it let through records that were plainly reviews and editorials on a full reading. Stage 2 therefore read the abstract of each of the 463 records and applied the eligibility rules strictly, excluding 306 and sending 157 reports to full text retrieval. The flaw and its correction are part of this review's record. A permissive first pass costs time; it does not cost validity, because every record it passed was read again. The reverse error, a strict first pass that drops eligible studies, would have been worse, and the two screener disagreement profile (97 of 128 disagreements were include against maybe) shows the pass erred on the side of keeping records.

Full text retrieval used lawful open routes only: PubMed Central, Europe PMC, publisher open access pages, Unpaywall and medRxiv. Of 157 reports sought, 74 were not retrieved. Eight of the 83 assessed reports were excluded with reasons, one report sits awaiting classification, and 74 studies were included.

### Data extraction

Extraction ran in two passes over the converted full texts, compared field by field, in 12 batches. The merged set holds 1,357 outcome rows across the 74 studies, each with values as printed, a table or page reference and a poolability call: 527 rows poolable, 830 narrative only, each with its reason filed. For 43 studies the main text is fully extracted and the gap is material printed only in a supplement, appendix or figure; six studies rest on a text shorter than the full article. One effect per study per outcome entered each pool, at the protocol preferred time point, and every selection and derivation is recorded in the selected effects file published with the analysis code.

### Risk of bias

RoB 2 was used for randomised designs and ROBINS-I for the rest, per outcome group, in two independent passes with adjudication. Confounders set in advance were baseline documentation load, specialty mix, concurrent EHR changes and self-selection of keen users into scribe groups. The two passes disagreed on 185 domain judgements; 121 of 138 rows had at least one domain disagreement; overall judgements differed in 32 rows; adjudication moved the judgement away from Pass A in 8 rows and away from Pass B in 24 rows. The commonest split was moderate against serious (103 of 185).

### Synthesis

Random effects inverse variance meta-analysis with tau squared estimated by REML. Hartung-Knapp confidence intervals where k was 3 or more; normal intervals at k 2; prediction intervals where k was 3 or more, from a t distribution with k minus 2 degrees of freedom. Hedges g for standardised mean differences computed from group means. Where a study printed a model based difference with a confidence interval, the effect is that difference divided by a standardiser from the same study, with the derivation logged. Before-after studies were pooled apart from controlled studies; combined pools are labelled sensitivity checks. Error proportions were pooled on the logit scale. Type specific error proportions were not pooled across studies, because one study reports each type against a notes denominator. Binary burnout outcomes were converted to standardised mean differences by the Cox transformation and pooled only in a sensitivity set. Subgroup claims rest on interaction tests on the subgroup pooled estimates. Sensitivity analyses: controlled studies only; excluding serious or critical risk of bias; leave one product out; preprints removed. Funnel plot and Egger test only where k was 10 or more. Certainty was rated with GRADE, at most seven outcomes in the summary of findings.

## Results

### Study flow

The searches returned 1,049 records: PubMed 385, Europe PMC 299, OpenAIRE 145 and 201 across its two title runs, ClinicalTrials.gov 19. Deduplication removed 482. Of 567 records screened, Stage 1 excluded 104 and passed 463; Stage 2 excluded 306 of those on a strict abstract reading, with non-primary publication type the largest single reason (136). Reports sought: 157. Reports not retrieved: 74. Reports assessed: 83. Excluded at full text: 8 (one qualitative study, one with no protocol outcome, one simulation study with no graded note outcome, one wrong intervention, and four earlier reports of studies already in the set). One report (R0506, a conference abstract in a journal supplement, with no notes denominator) awaits classification. Studies included: 74, one report per study.

### Description of studies

The 74 studies were published in 2024 (2), 2025 (27) and 2026 (45). Sixty-four are journal articles, counting one conference proceedings paper and one research letter; ten are preprints. Fifty were conducted in the United States. The rest came from the United Kingdom (6), Australia (5), Canada (2), the Netherlands (2), and one each from Switzerland, Spain, Singapore, Saudi Arabia, the United Arab Emirates, South Africa and Sweden, one multinational European study, and one study whose country was not stated in the retrieved text.

Designs: uncontrolled before-after studies 25, note audits 20, non-randomised controlled studies 12, randomised trials 6, cross-sectional studies 5, controlled before-after studies 2, one interrupted time series, one stepped wedge trial, and 2 studies in other designs. The before-after study is the workhorse of this literature and its weakest instrument at the same time: a quarter of the included set, and the design most exposed to the self-selection problem the protocol named in advance.

Products, grouped by the primary named product in each report: Abridge 18 studies, DAX or Dragon Ambient eXperience 10, Heidi 3, and one study each for Ambience, Suki and Lyrebird, one two arm study of DAX Copilot and Nabla, and 39 studies of other, mixed, anonymised or unnamed products. That last group is a reporting problem in itself. A literature that will not name its intervention in two fifths of its papers cannot support product level purchasing claims, however its class level pools behave.

Vendor involvement, as extracted from funding and conflict statements: 17 studies were vendor linked (vendor funding, vendor staff involvement, or both), 44 were independent, and 13 were unclear. Follow-up was short throughout. Twenty-eight studies describe a single audit or a single study period with no follow-up at all, and most of the rest ran 30 to 90 days of use. Clinician samples ran from a single surgeon in one workload study to system wide rollouts; outcome analysis units across the review include clinicians, encounters, appointments, notes and paired periods, and are reported per pool rather than summed into a single misleading total.

Outcome data: 1,357 outcome rows were extracted, 527 of them poolable. Twenty-seven studies had no poolable row in any protocol outcome and enter the narrative synthesis only. The analysis datasets held 28 studies for time, 16 for burnout and workload, 10 for errors and 17 for quality before the one effect per study selections were made for pooling.

### Risk of bias in included studies

All 74 studies were assessed, in 138 study by outcome rows (RoB 2: 17 rows; ROBINS-I: 121 rows). Adjudicated overall judgements across the rows: serious 94, moderate 24, some concerns 11, high 5, critical 3, low 1. By study, taking each study's worst row: serious 55, moderate 10, high 5, critical 2, some concerns 2, low 0. No study in this literature is clean across every outcome it reported.

The pattern has a shape. Time outcomes: 44 rows, 33 serious. Burnout: 29 rows, 23 serious. Quality: 39 rows, 25 serious. Errors: 22 rows, 10 serious and 9 moderate; the error audits are the strongest part of this literature, because the better ones used a human checked reference transcript and blinded graders. The drivers of the serious ratings were confounding and selection: volunteer early adopters compared with non-users, high user subgroups analysed as if they had been assigned, no concurrent control, and concurrent EHR changes left open. For errors and quality, measurement drove the ratings: graders who were the notes' own authors, unblinded grading, or grading against the tool's own transcript. Two studies carry critical rows. One restricted its survey to fully onboarded sustained users, with discontinuers excluded by design. One scored PDQI-9 with LLM raters whose inter-rater agreement statistic was negative, and its own text warns that the scores cannot be read as reliable quality evidence. Both stay in their pools, flagged, with the sensitivity analyses showing what changes when they leave.

### Synthesis: documentation time

Thirteen studies gave a standardisable effect (Figure 1). Controlled studies pooled at SMD -0.52 (95% CI -0.88 to -0.15; k 6; 11,108 analysis units; I squared 88.2%; tau squared 0.102; prediction interval -1.49 to 0.46). Before-after studies pooled at SMD -0.31 (-0.43 to -0.19; k 7; 1,792 units; I squared 64.2%; tau squared 0.011; prediction interval -0.61 to -0.02). The combined pool, a sensitivity check, gave SMD -0.38 (-0.53 to -0.24; k 13; 12,900 units; I squared 83.4%). The design interaction test did not confirm the visible gradient (chi squared 4.88, df 2, p 0.087).

On the percentage scale, 15 studies pooled at -18.9% (-25.9% to -11.9%; I squared 88.4%; prediction interval -43.4% to 5.5%). The before-after percentage pool was tight (I squared 0.0%, -14.3%) and the controlled percentage pool was wide (I squared 92.5%, -21.8%), a reminder that the controlled set contains both the largest system studies and the widest spread of results. Removing the one preprint in the SMD pool changed the estimate little (-0.40). Excluding serious and critical risk of bias studies left three studies and a wide interval (-0.37; -1.22 to 0.49), which is the single most honest sentence about this literature: the time effect is probably real and its size rests on studies with known weaknesses.

Product subgroups did not separate: Abridge SMD -0.36 (k 7), DAX family -0.37 (k 3), other products -0.52 (k 3); interaction p 0.39. Vendor subgroups did not separate either: vendor linked studies -0.28 (k 3), independent studies -0.43 (k 9); interaction p 0.14. Leaving out each product family in turn moved the combined estimate between -0.36 and -0.43. Reporting bias: the funnel plot (Figure 2) and Egger test (intercept -0.71, p 0.56 for the SMD pool; p 0.95 for the percentage pool) showed no asymmetry, at low power.

Four further controlled studies reported time effects that could not be standardised and are part of the narrative record: Husa (2026) reported an interrupted time series with time in notes per day falling from 50.7 to 41.6 minutes at implementation; Rotenstein (2026) reported 16.0 fewer minutes in notes per 8 scheduled hours; Afshar (2025) reported -0.36 hours of documentation time per day; Wright (2025) reported median paired differences. Their direction matches the pool. Survey agreement items ("the tool saves me time") were not pooled with measured time.

![Figure 1. Forest plot, documentation time, standardised mean difference.](stage5/forest-time-smd.png)

![Figure 2. Funnel plot, documentation time, standardised mean difference.](stage5/funnel-time-smd.png)

![Figure 3. Forest plot, documentation time, relative change in percent.](stage5/forest-time-relative.png)

### Synthesis: after-hours documentation time

Six studies, all uncontrolled before-after, pooled at SMD -0.25 (95% CI -0.52 to 0.01; 1,003 analysis units; I squared 71.8%; tau squared 0.037; prediction interval -0.85 to 0.34; p 0.058) (Figure 4). The Abridge subset (k 4) gave -0.26, with a wider interval. Vendor and independent subgroups did not separate (interaction p 0.50).

Two sensitivity results define this outcome. The controlled studies only pool is empty: no controlled study reported an after-hours effect in a form that could be standardised. The pool excluding serious and critical risk of bias studies is also empty: all six studies are at serious risk of bias for this outcome. One large study's raw off-hour minutes rose slightly after implementation (39.8 against 38.2 minutes) while its adjusted model estimate fell, and the raw values were used, which is part of the heterogeneity. A controlled study that did report after-hours work, Prasser (2026), found an adjusted +9.1 seconds per encounter after the shift with medians of zero in both arms; it is described here rather than forced into the pool. The claim that scribes give clinicians their evenings back is, on current evidence, the least supported claim in the sales material.

![Figure 4. Forest plot, after-hours documentation time.](stage5/forest-afterhours-smd.png)

### Synthesis: burnout, work exhaustion and workload

Four studies reported work exhaustion or burnout on continuous scales (Figure 5). The two randomised trials, Afshar (2025) and Lukac (2025), pooled at SMD -0.44 (95% CI -0.61 to -0.28; 257 clinicians; I squared 0.0%). On their shared instrument, the Professional Fulfillment Index work exhaustion composite, the pooled mean difference was -0.36 points (-0.52 to -0.20). The two before-after studies pooled at SMD -0.23 (-0.35 to -0.12). All four together: SMD -0.34 (-0.53 to -0.15; 682 units; I squared 34.0%; prediction interval -0.87 to 0.19). The design interaction test gave p 0.038 with two studies per subgroup; it is a signal to test in later trials, not a settled finding. Excluding serious and critical studies leaves the trial pool unchanged. A sensitivity set of five studies reporting burnout only as proportions over a threshold, converted to SMD, pooled at -0.39 (-0.61 to -0.16), and the combined nine study set at -0.35 (-0.46 to -0.25; I squared 14.4%). Two routes to the same quantity, continuous scales and threshold counts, land in the same place.

Follow-up in the trials was 30 to 90 days. Nothing in this pool speaks to a year. Professional fulfilment did not move with exhaustion: Afshar (2025) reported +0.14 points (0.004 to 0.28) on the fulfilment composite, and You (2025) reported threshold proportions of 37.5% before, 36.5% at 42 days and 41.7% at 84 days. The two were not pooled; they use unlike metrics.

Workload told a less tidy story (Figure 6). Seven studies pooled at SMD -1.46 (-2.13 to -0.78; I squared 90.8%), an average carried by small uncontrolled surveys with very large standardised effects: Kashiouris (2026) at g -2.66, one Olson (2025) study at d -1.90, another at SMD -1.60. The six other studies in the pool sit at serious risk of bias for this outcome. The one study that survives the risk of bias filter is Lukac (2025), the randomised trial, at SMD -0.39 (-0.70 to -0.09). The design subgroup test was formally significant (chi squared 26.3, df 2, p below 0.001) on subgroups of 1, 2 and 4 studies, and is reported as descriptive. The review's reading: task load falls when a scribe takes the typing away, and the fall is probably nearer the trial's -0.4 SD than the survey average of -1.5 SD. Vendor and independent workload subgroups did not separate (interaction p 0.46).

![Figure 5. Forest plot, burnout and work exhaustion.](stage5/forest-burnout-smd.png)

![Figure 6. Forest plot, workload and task load.](stage5/forest-workload-smd.png)

### Synthesis: note quality

Six studies reported quality scores that could be standardised (Figure 7): SMD 0.57 (95% CI 0.51 to 0.64; 1,193 analysis units; I squared 0.0%; prediction interval 0.45 to 0.70). The PDQI family subset (three studies) gave 0.55 (0.49 to 0.61). Excluding serious and critical studies left three studies at 0.57 (0.41 to 0.73). Journal articles only gave 0.65 (0.58 to 0.72). Vendor and independent subgroups did not separate (interaction p 0.099).

Three cautions travel with this result. Bergman (2026), a preprint reporting 385 paired consultations in simulated encounters across five countries, carries 78.7% of the weight because its printed interval is narrow; the pool is, in large part, that study plus small change. Gladysz (2026) is at critical risk of bias for this outcome, for the LLM scoring reason given in the risk of bias section; its weight is small and removing the serious and critical studies together leaves the estimate at 0.57. And the instruments rate structure, completeness and readability. A note can score well on all three and still contain a fabricated detail. Quality scores and error rates are different measurements, and this review keeps them apart on purpose.

Not pooled: Zuckerman (2025) compares two scribe workflows against each other; Verma (2026) compares two versions of one model (omissions 21.60% of clinical elements for the earlier version against 9.32% for the later one, a model improvement result, not a scribe against usual care result); Taylor (2026) reports a median quality score with no variance.

![Figure 7. Forest plot, note quality.](stage5/forest-quality-smd.png)

### Synthesis: note errors

Type specific proportions rest on one study each and were not pooled across studies. Taylor (2026), 356 notes checked against the consultation record: omissions 18.0% of notes (95% CI 14.3% to 22.3%), hallucinations 11.5% (8.6% to 15.3%), wrong inclusions 9.3% (6.7% to 12.7%), errors rated severity 4 to 5 in 5.3% (3.4% to 8.2%), and 94.7% of notes free of significant errors on the study's grading. Menz (2026) used a data point denominator: omissions were 10 of 2,160 data points (0.5%), and 46 data points (2.1%) were incorrect in total. The two denominators, notes and data points, answer different questions and were not mixed.

Two studies report the share of notes with at least one error, under different definitions (Figure 8). Biro (2025): 31 of 44 draft notes (70.5%), with a mean of 2.9 errors per note. De John (2026): 24 of 49 notes (49.0%) with at least one clinically meaningful error. Pooled on the logit scale: 59.8% (37.9% to 78.4%; I squared 76.9%). Both studies are at serious risk of bias for this outcome, so the risk of bias sensitivity pool is empty, and removing the preprint leaves Biro (2025) alone. The pooled figure is reported with its interval and its grade, and the review does not headline it: two definitions, 93 notes, and a detection problem underneath both.

The detection problem is measurable. In Bergman (2026), clinician adjudication found at least one Critical or High error in 6.2% of AI notes (24 of 385); a calibrated automated reviewer, reading the same notes, found 24.4% (94 of 385). Error rates in this literature are a property of the detection method as much as of the notes. Other error data were not pooled: counts per note (Bauer 2026: medians of 5 omissions per AI note against 8 per comparator note), planted error propagation (Rabotin 2026: 55% and 60% of planted interpreter errors reached the final note in two arms), arm level error totals (Etagiuri 2026: 19 against 9), and clinician reports of spotting errors (Draper 2025: 45 of 141 surveyed GPs, 31.9%, said they often or always spot errors in AI drafts; the denominator there is clinicians, not notes).

![Figure 8. Forest plot, notes with at least one error.](stage5/forest-errors-any.png)

### Other outcomes

Patient experience had four study by outcome rows, on unlike instruments, three of them at serious or high risk of bias; it is reported in the extraction set and not pooled. Note length, time to note closure and documentation volume were reported on unlike metrics by a handful of studies and are not pooled. No included study reported a cost outcome in a form the protocol could use.

### Certainty of the evidence

Documentation time: low. Downgraded for risk of bias (the estimate rests on serious risk studies; the cleaner sensitivity pool is null and wide) and for inconsistency (I squared 83.4%, prediction interval crossing no effect). After-hours time: very low; risk of bias (all six studies serious, no controlled estimate), inconsistency (I squared 71.8%, one study's raw minutes moving the other way) and imprecision (the interval includes no effect). Burnout and work exhaustion: moderate for the trial estimate, downgraded once for indirectness, because 30 to 90 day follow-up cannot carry a claim about lasting burnout; low for the all studies estimate, with a further downgrade for the serious risk before-after studies. Workload: very low; risk of bias, inconsistency (I squared 90.8%) and indirectness (four different constructs in one pool, one study's units being five clinic days). Note quality: low; risk of bias (one critical study, unblinded grading in several audits, the dominant study a preprint) and indirectness (rating instruments and simulated encounters stand in for accuracy in live care). Note errors: very low; risk of bias, inconsistency across two definitions, and imprecision (93 notes). Professional fulfilment: very low; two studies, two metrics, no pool.

### How the LLM team performed

The mechanics are part of the method, so they are reported with the results. Screening pass A called include 233, maybe 207, exclude 127; pass B called include 339, maybe 122, exclude 106. Agreement 439 of 567 (0.7743), kappa 0.6439. Of the 128 disagreements, 97 were include against maybe, which is the cheap direction to disagree in: the record stays alive either way. Thirteen include against exclude records were flagged to the author. The strict Stage 2 pass then excluded 306 of the 463 records Stage 1 had passed, which is the clearest measure of how permissive the first pass was.

Extraction produced two discrepancies worth naming, because both were caught by the pass comparison rather than by a reader's luck: one study's summary line carried a 70 second figure that its full text does not contain (the paper prints 86 seconds), and one study's abstract and results disagree on the direction of a burnout item. Risk of bias passes disagreed on 185 domain judgements and on the overall judgement in 32 of 138 rows; adjudication sided away from Pass B more often (24 rows) than away from Pass A (8 rows). A human team would call those numbers ordinary. The point of printing them is that a reader does not have to take the substitute team's word for anything: the disagreement record sits in the review files next to the clinical data.

## Discussion

### Summary of main results

Ambient scribes cut documentation time. The controlled studies pool at SMD -0.52, the before-after studies at -0.31, and the percentage pool at -18.9%, with low certainty and wide spread. Work exhaustion fell in two randomised trials, SMD -0.44, at moderate certainty for follow-up of 30 to 90 days. After-hours work, the outcome patients never see and clinicians feel most, has no controlled pooled estimate at all and a very low certainty uncontrolled one. Notes scored higher on quality instruments (SMD 0.57, low certainty) and carried errors at rates that depend on the error type and on who looked: omissions in 18.0% of notes in the one study that counted types against a notes denominator, hallucinations in 11.5%, wrong inclusions in 9.3%. Workload scores fell, by an amount the studies cannot pin down (very low certainty). Fulfilment did not clearly change.

### Limits of the evidence

The risk of bias picture is the first limit. Fifty-five of 74 studies carry a serious worst judgement, and none is clean across every outcome. The bias has a known address: self-selection. Clinicians who volunteer for a scribe pilot are the clinicians most burdened by notes or most open to the tool, and studies that then analyse high users as if they were an assigned group build the answer into the sample. One included study excluded discontinuers from its survey by design; its results describe people who stayed. A field that samples its fans will report relief.

The second limit is time. Most follow-up sits between a single audit and 90 days. A burnout score taken five weeks after a hated task shrinks is a real measurement and a weak basis for a claim about burnout, which is built over years and driven by staffing, workload and control over work, with documentation one contributor among several. The moderate certainty rating for the trial estimate is a rating about 30 to 90 days, and it should not be quoted without the window attached.

The third limit is that the intervention moves. Products update their models during study periods; one included study compared two versions of its own model and found omissions falling from 21.60% of clinical elements to 9.32% between versions. A pooled estimate for "ambient scribes" averages versions that no longer exist in some cases. This argues for version stamped reporting in primary studies, which almost none of the 74 provided in a usable form: product version was extractable in a minority of reports.

The fourth limit is measurement on the error side. Error audits disagree with each other by design: different denominators (notes, data points, clinical elements, planted errors), different reference standards (audio, transcript, the record, the tool's own transcript), different graders (blinded clinicians, the notes' authors, LLM raters, calibrated automated reviewers). The same notes in Bergman (2026) gave a severe error rate of 6.2% under clinician adjudication and 24.4% under an automated reviewer. Until audits share a denominator and a grading protocol, error rates across studies cannot be averaged and should not be quoted side by side as if they were one quantity.

The fifth limit is geography and naming. Fifty of 74 studies are from the United States, and 39 do not name a single primary product in a way that supports product level reading. Vendor involvement was unclear in 13 studies, which in a field this commercial is itself a finding about reporting standards.

### Limits of the review process

The largest limit is retrieval. Of 157 reports sought, 74 (47%) were not retrieved through lawful open routes. Those reports are not a random sample of the literature: paywalled reports skew toward established journals, and the included set skews toward open access and preprint friendly outlets. The pooled estimates could move when those reports are read, and the direction of that movement is unknown. One further report awaits classification, and eight unpublished database searches (Embase, CINAHL, PsycINFO, CENTRAL, Scopus, Web of Science, ACM, WHO ICTRP) were prepared but not run for lack of licensed access; two further sources (OpenAlex, Semantic Scholar) were blocked by rate limits. PsycINFO and CINAHL are real gaps for the burnout and workload outcomes. The review's counts say exactly which sources were searched, and the abstract repeats it, because a synthesis that overstates its search is worse than one with a smaller, honest search.

The screening flaw is the second limit, and it is declared rather than buried. Stage 1's two decision procedures passed 463 of 567 records, including records that a strict reading excludes at sight. Stage 2 corrected it by reading every abstract against the eligibility rules. The correction is auditable in the files: every Stage 2 exclusion carries a reason. What the flaw cost was effort, and what it revealed is worth keeping: rule based screening passes, LLM driven or not, need a strictness check against a human read sample before they are trusted at scale.

Extraction has gaps the files name plainly: 43 studies have material that sits only in supplements, appendices or figures; six studies rest on texts shorter than the full article; one included study yielded no outcome rows from its archived abstract length text. Numbers that enter the pools were checked against full text where a full text exists.

The LLM team is the fourth limit. Its members are one model family in several roles, not several independent minds. The independence rules kept the passes apart and the disagreement counts (kappa 0.6439; 185 domain disagreements; overall risk of bias judgements differing in 32 of 138 rows) show the passes were not copies of each other. They also show the ceiling: two passes from the same model can share a blind spot, and no agreement statistic rules that out. The human author is one person. A conventional review spreads these tasks across a team with a search specialist and a second senior reviewer; this review substitutes process and disclosure for headcount, and the substitution is visible in the record for readers to weigh.

### Agreements and disagreements with other syntheses

Zhao (2025) pooled 23 studies of AI note tools and found SMD -0.71 for documentation burden and -0.72 for time, with I squared 93.3%. This review, ambient scribes only and including the 2025 trials, finds a smaller time effect: SMD -0.38 across all studies, -0.52 in controlled studies, and -18.9% on the percentage scale. The direction agrees. The size does not, and the gap is instructive: Zhao's broader tool set and pre-trial study mix produced a bigger average, while the heterogeneity barely moved (93.3% there, 83.4% to 92.5% across this review's time pools). Twenty-five years of meta-analysis teaching says a bigger, tighter literature should narrow the spread. Here the literature grew and the spread stayed, which points at real differences between settings, products and study designs rather than at sampling noise. Where Zhao described study quality as generally low, this review can put numbers on that judgement: 55 of 74 studies at serious risk of bias on their worst outcome row.

The rapid review prepared for Canada Health Infoway (Sasseville 2025) sits in this review's search set and represents the other genre working this question: fast, buyer facing, with a narrower search and no certainty grading or error pooling. The genres agree on the direction of the time effect, which is the part a rapid review can carry. What a rapid review cannot carry is the sentence this review exists to write: the time effect is low certainty, the after-hours effect is very low certainty, and the error burden has a number attached (omissions 18.0% of notes in the largest type specific audit) that belongs in the same paragraph as the saving.

### The time saved and vigilance trade

Read the benefit and error results together and a trade appears. A clinician who stops typing starts proofreading. The pool says the proofreading job is smaller than the typing job was: time falls by about a fifth. The audits say the proofreading job is real: in Taylor (2026), roughly one note in five missed something said in the consultation and roughly one in nine contained something never said. Most of those errors are small. A share are not: 5.3% of notes in that audit carried an error rated severity 4 or 5, and Draper (2025) sets out how an uncorrected fabrication in a primary care note can travel into referrals, prescribing and the record other clinicians trust.

The trade turns on three quantities no single study in this review reports together: time saved per note, time spent reviewing per note, and errors caught per note reviewed. Studies report the first. Almost none report the second, and none reports the third. Until a study measures review time and catch rate alongside generation, the net effect on clinician attention is inferred, not measured. The guidance documents have noticed this gap before the primary literature has: NHS England's guidance asks for a safety case and human review of drafts, and the Joint Commission and CHAI guidance asks for local validation and monitoring. Those are process answers to a measurement gap. They are reasonable process answers. They are not evidence that the trade nets out positive in any given clinic, and this review does not claim it does.

### Product effects and class effects

Lukac (2025) remains the warning label for class level claims: Nabla cut time in note by 9.5% and DAX by 1.7% in the same trial. This review's product subgroups for time did not separate (Abridge -0.36, DAX family -0.37, other products -0.52; interaction p 0.39), and the leave one product out analyses moved the pooled estimate only between -0.36 and -0.43. Two readings are possible. Products may genuinely perform alike on time once study design noise is averaged out, with Lukac's split a chance pattern in one trial. Or the subgroup test may lack the power and the product reporting (39 studies with no single named product) to see a split that exists. The data cannot settle which. What they do settle is narrower: no product family in this literature has earned a claim of superiority on documentation time, and vendor linked studies did not report larger effects than independent ones on any outcome where the test could run (time interaction p 0.14; after-hours p 0.50; workload p 0.46; quality p 0.099). That second finding cuts against the simplest version of the sponsorship story, and it is reported with the same prominence as the rest.

### What the guidance documents ask for

NHS England (27 April 2025) treats ambient scribes as technology that needs a safety case, clarity on device status, and a human checking drafts before they enter the record. The Joint Commission and CHAI responsible use guidance (17 September 2025) asks deploying organisations for local validation, monitoring over time and a named owner for the tool's performance. The FDA advisory discussion (6 November 2025) named hallucinations and model drift as risks needing controls. Set against this review: the pooled error and time estimates give those documents their first certainty graded numbers to cite; the retrieval gap (74 reports unread) and the version problem (products changing mid-study) say the numbers will date fast, which is an argument for the monitoring the guidance asks for, done with local audit denominators that match the ones used here: notes audited, error type, grader, and detection method stated.

## Authors' conclusions

### Implications for practice

The evidence supports a measured reading of what ambient scribes do. Documentation time falls by about a fifth on average (low certainty), work exhaustion scores fall over one to three months (moderate certainty from two trials), and after-hours effects are unproven at controlled standards (very low certainty). AI drafts contain errors often enough (omissions in 18.0% of notes in the largest type specific audit) that clinician review of every draft is part of the intervention as studied, and any account of these tools that treats review as optional is describing a different, untested intervention. This review is evidence synthesis. It makes no clinical recommendation, no medication recommendation, and no recommendation that any service buy, deploy or remove any product. Decisions of that kind sit with the services that run them, on local data of the kind the guidance documents describe.

### Implications for research

Four gaps decide what the next version of this review can say. First, a controlled study of after-hours work: the outcome with the strongest sales claim has zero controlled pooled estimates. Second, burnout follow-up at 6 to 12 months in randomised designs, with response rates reported by arm, so the field can separate a lasting effect from the relief of the first quarter. Third, a shared error audit protocol: notes as the denominator, the three error types kept apart, blinded graders, the reference standard stated, and the detection method reported next to the rate, since detection method alone moved one study's severe error rate from 6.2% to 24.4%. Fourth, basic reporting repairs that cost nothing: name the product and its version, report an SD or a model standard error on a stated scale for every time outcome, and state vendor involvement plainly. Four controlled time studies in this review could not enter the SMD pool for want of a printed spread. A literature that wants to be pooled has to print poolable numbers.

For the method this review tested: an LLM team can carry the team tasks of a Cochrane level review to a standard a reader can audit, provided the passes are kept apart, the disagreements are printed, and a named human stays accountable. The agreement and disagreement numbers in this review are the evidence for that sentence, and they are mixed evidence: kappa 0.6439 is substantial agreement and a long way from perfect, and the first screening pass needed a strict second pass to correct it. The claim worth making is the narrow one. The process is auditable. Audit it.

## Declarations

**Funding.** None. No grant, sponsor or industry support of any kind.

**Conflicts of interest.** None. The author is an independent researcher with no industry affiliation. He is a healthcare founder and operator who bootstrapped and ran a direct primary care clinic as chief executive, and now builds clinical AI. He writes in that capacity and as an independent researcher.

**AI use disclosure.** A team of large language model roles (Muse Spark, Meta, used 22 October 2026) carried out the team tasks of this review: search string building, duplicate screening passes, adjudication support, dual extraction, dual risk of bias assessment, statistical analysis, GRADE drafting and methods editing, under the independence rules and human oversight set out in the methods. This disclosure follows the 2025 RAISE statement. The human author set the question and eligibility rules, settled flagged items and all risk of bias and GRADE disagreements, and is accountable for every judgement, every checked number and the final text. The LLM team holds no authorship.

**Data and code availability.** The search log, screening files, extraction sheets, risk of bias assessments, selected effects, analysis code (Python) and figure files for this review are published with it in the public repository "ambient-ai-scribes-meta-analysis-clinical-documentation-burnout-note-errors" under the author's GitHub account (rtmalikian), under a CC BY 4.0 licence. No DOI had been issued for the repository or this manuscript when this version was completed.

**Ethics.** This review synthesises published and preprint reports. No patient data were collected and no ethics approval was required.

## References

### Methods, guidance and prior synthesis

- Cochrane Handbook for Systematic Reviews of Interventions, version 6.5. Cochrane, 2024.
- Page MJ, and others. The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. BMJ, 2021.
- RAISE statement on responsible use of artificial intelligence in evidence synthesis. Cochrane, Campbell Collaboration, JBI and Collaboration for Environmental Evidence, 2025.
- Sterne JAC, and others. RoB 2: a revised tool for assessing risk of bias in randomised trials. BMJ, 2019.
- Sterne JAC, and others. ROBINS-I: a tool for assessing risk of bias in non-randomised studies of interventions. BMJ, 2016.
- Zhao, and others. Artificial intelligence tools for clinical note creation: a systematic review and meta-analysis. BMC Medical Informatics and Decision Making, 2025. PMC12836966.
- Sasseville M, Yousefi F, Ouellet S, Bergeron F, LeBlanc A. Impacts of AI Scribes on Clinical Outcomes, Efficiency, and Documentation: a rapid review prepared for Canada Health Infoway, 2025. DOI 10.13140/rg.2.2.20047.19364.
- NHS England. Guidance on the use of ambient scribing technology. 27 April 2025.
- Joint Commission and Coalition for Health AI (CHAI). Responsible Use of AI in Healthcare (RUAIH) guidance. 17 September 2025.
- US Food and Drug Administration. Digital Health Advisory Committee meeting on generative AI enabled devices. 6 November 2025.
- Menlo Ventures. State of AI in Healthcare, 2025 (ambient scribe spending estimate, $600M).
- Kaiser Permanente and The Permanente Medical Group. Ambient AI scribe rollout figures (7,260 physicians; 2,576,627 encounters), as reported in the review's concept sources.
- American Medical Association. Physician AI use survey, 2024 (66% of surveyed physicians reporting AI use, against 38% in 2023).

### Included studies

- Adler-Milstein, and others (R0240). Subjective and objective impacts of ambulatory AI scribes. American Journal of Managed Care, 2026. 10.37765/ajmc.2026.89869.
- Afshar, and others (R0235). A Pragmatic Randomized Controlled Trial of Ambient Artificial Intelligence to Improve Health Practitioner Well-Being. NEJM AI, 2025. 10.1056/aioa2500945; PMID 41625485.
- Akhlaghi, and others (R0155). Evaluation of an AI Scribe Tool in the Emergency Department: A Single-Arm Observational Study. Emergency Medicine Australasia, 2026. 10.1111/1742-6723.70272; PMID 42087797.
- Alcazar-Peral, and others (R0077). Real-world evaluation of an ambient AI scribe in Spanish outpatient care after 2.3 million uses: impact on clinician experience, semantic agreement, and workflow efficiency. Frontiers in Digital Health, 2026. 10.3389/fdgth.2026.1874919; PMID 42518737.
- Alpert, and others (R0273). Evaluating an artificial intelligence scribe for clinical documentation. Digital Health, 2025. 10.1177/20552076251395588; PMID 41278378.
- Anderson, and others (R0078). The Impact of Ambient AI on Resident Documentation and Well-Being: A Pilot Study. PRiMER, 2026. 10.22454/PRiMER.2026.393770.
- Arko, and others (R0313). Documenting Care with AI: A Comparative Analysis of Commercial Scribe Tools. Studies in Health Technology and Informatics (MEDINFO 2025, vol 329, pp 337-341), 2025. 10.3233/SHTI250857.
- Balloch, and others (R0373). Use of an ambient artificial intelligence tool to improve quality of clinical documentation. Future Healthcare Journal, 2024. 10.1016/j.fhj.2024.100157; PMID 39371531.
- Bauer, and others (R0435). Impact of an ambient digital scribe on typing and note quality: the AutoscriberValidate study medRxiv (preprint), 2026. 10.64898/2026.02.19.26346634.
- Bergman, and others (R0408). Quality, consistency, and clinical safety of AI-generated versus clinician-written clinical notes: a multi-country paired simulation study medRxiv (preprint), 2026. 10.64898/2026.08.18.26360701.
- Biro, and others (R0363). Accuracy and Safety of AI-Enabled Scribe Technology: Instrument Validation Study. Journal of Medical Internet Research, 2025. 10.2196/64993; PMID 39869899.
- Blease, and others (R0105). Ambient AI in primary care: an exploratory mixed methods survey of UK general practitioners. BMJ Health & Care Informatics, 2026. 10.1136/bmjhci-2025-101847; PMID 42386325.
- Brunner, and others (R0256). Ambient Scribe Technology in Simulated Patient Encounters Across Specialties. JAMA Network Open, 2026. 10.1001/jamanetworkopen.2025.52870; PMID 41499119.
- Castro, and others (R0245). Psychiatric Documentation and Management in Primary Care With Artificial Intelligence Scribe Use. JAMA Psychiatry, 2026. 10.1001/jamapsychiatry.2025.4303; PMID 41563771.
- Chim, and others (R0173). Evaluating privacy leakages in LLM-driven ambient clinical documentation. Frontiers in Digital Health, 2026. 10.3389/fdgth.2026.1761624; PMID 41988159; PMC13076117.
- Davis, and others (R0232). Ambient AI Documentation and Patient Satisfaction in Outpatient Care: Retrospective Pilot Study. JMIR AI, 2026. 10.2196/78830; PMID 41650387.
- De John, and others (R0395). Accuracy and Safety of an AI Ambient Scribe Compared with Handwritten Clinical Notes Research Square (preprint), 2026. 10.21203/rs.3.rs-9139641/v1.
- Draper, and others (R0029). Clinical AI Scribes in primary care: accuracy, error severity and implications for clinical practice. BMJ Digital Health & AI, 2025. 10.1136/bmjdhai-2025-000092.
- Draper, and others (R0030). Impact of acoustic and informational noise on AI-generated clinical summaries. BMJ Digital Health & AI, 2025. 10.1136/bmjdhai-2025-000057.
- Draper, and others (R0165). AI-generated clinical summaries: errors and susceptibility to speech and speaker variability. BMJ Health and Care Informatics, 2026. 10.1136/bmjhci-2025-101918; PMID 42031419.
- Duggan, and others (R0360). Clinician Experiences With Ambient Scribe Technology to Assist With Documentation Burden and Efficiency. JAMA Network Open, 2025. 10.1001/jamanetworkopen.2024.60637; PMID 39969880.
- Etagiuri, and others (R0181). Evaluating the Impact of Artificial Intelligence Scribes on Clinical Workflow and Documentation Quality: A Randomized Controlled Trial. The Journal of Arthroplasty, 2026. 10.1016/j.arth.2026.03.069.
- Foo, and others (R0277). The Great Scribe-Off: A Comparative Analysis of AI Scribes Versus Human Documentation in Simulated General Practice Consultations. Studies in Health Technology and Informatics, 2025. 10.3233/SHTI251572.
- Foo, and others (R0179). A comparative analysis of AI scribes versus human documentation in simulated general practice consultations. Australian Journal of General Practice, 2026. 10.31128/AJGP-04-25-7645; PMID 41942089.
- Furrukh, and others (R0278). Implementation of Dragon Ambient Experience by Plastic Surgery Residents Improves Wellness and Decreases Burnout: A Pilot Study. Plastic and Reconstructive Surgery Global Open, 2025. 10.1097/GOX.0000000000007287; PMID 41229582.
- Ghanem, and others (R0265). DAX Copilot: ambient AI scribe may help reduce surgical resident clinical documentation burden. Surgical Endoscopy, 2026. 10.1007/s00464-025-12404-x.
- Gladysz, and others (R0128). AI-Assisted Medical Documentation in a Multilingual Swiss Health Care System: Proof-of-Concept Study. JMIR AI, 2026. 10.2196/77351; PMID 42247573.
- Golos, and others (R0012). Ambient artificial intelligence scribes in urology: a pilot evaluation of user experience and clinical efficiency gains. World Journal of Urology, 2026. 10.1007/s00345-026-06860-w.
- Grand, and others (R0068). Optimizing Hip and Knee Arthroplasty Clinic Flow: A Prospective Evaluation of Artificial Intelligence Scribe Technology. Arthroplasty Today, 2026. 10.1016/j.artd.2026.102095; PMID 42564601.
- Guo, and others (R0312). Ambient Listening in Clinical Practice: Evaluating EPIC Signal Data Before and After Implementation and Its Impact on Physician Workload. Studies in Health Technology and Informatics, 2025. 10.3233/SHTI250921; PMID 40775939.
- Ha, and others (R0316). Evaluating the Usability, Technical Performance, and Accuracy of Artificial Intelligence Scribes for Primary Care: Competitive Analysis. JMIR Human Factors, 2025. 10.2196/71434; PMID 40700466.
- Harvey, and others (R0287). Ambient AI-assited clinical documentation in surgical outpatient care: a preliminary study of usability, workflow, and patient experience. World Journal of Pediatric Surgery, 2025. 10.1136/wjps-2025-001073; PMID 41142586.
- Harvey, and others (R0111). Ambient AI Scribe Implementation in an Ambulatory Setting in a Single Medical Group: Prospective Study. JMIR Medical Informatics, 2026. 10.2196/84104; PMID 42337645.
- Hudson, and others (R0353). Impact of Ambient Artificial Intelligence Documentation on Cognitive Load. Mayo Clinic Proceedings: Digital Health, 2025. 10.1016/j.mcpdig.2024.100193; PMID 40206994.
- Husa, and others (R0134). Ambient Artificial Intelligence Use and Clinician Documentation Burden, Productivity, and Efficiency. JAMA Network Open, 2026. 10.1001/jamanetworkopen.2026.15762; PMID 42213439.
- Jain, and others (R0426). An LLM-Based Comparison of Ambient AI Scribes for Clinical Documentation medRxiv (preprint), 2025. 10.1101/2025.06.24.25330085.
- Kakaday, and others (R0355). The STREAMLINE Pilot Study on Time Reduction and Efficiency in AI-Mediated Logging for Improved Note-Taking Experience. Applied Clinical Informatics, 2025. 10.1055/a-2559-5791; PMID 40097146.
- Kashiouris, and others (R0043). The Effect of Ambient Artificial Intelligence Documentation on Clinician Workload, Efficiency, and Patient Experience in a Multisite Emergency Department Network. Applied Clinical Informatics, 2026. 10.1055/a-2939-3038.
- Khan, and others (R0191). A Bilingual Arabic-English Ambient AI Scribe for Clinical Documentation: Prospective Evaluation Study. JMIR Medical Informatics, 2026. 10.2196/83335; PMID 41875245.
- Lawrence, and others (R0131). Implementing Artificial Intelligence-Enabled Ambient Documentation Technology for Ambulatory Clinicians: An Innovation Evaluation. Journal of General Internal Medicine, 2026. 10.1007/s11606-026-10448-w.
- Li, and others (R0209). Linguistic Effects of Ambient AI on Clinical Documentation: A Matched Pre-Post Study. medRxiv (preprint), 2026. 10.64898/2026.02.16.26346370; PMID 41757209.
- Lukac, and others (R0257). Ambient AI Scribes in Clinical Practice: A Randomized Trial. NEJM AI, 2025. 10.1056/aioa2501000; PMID 41497288.
- Major, and others (R0048). Readability of AI-Generated Patient Visit Summaries in Orthopedic Surgery: Retrospective Analysis. Journal of Medical Internet Research, 2026. 10.2196/87283.
- Marquis, and others (R0205). AI-Powered Ambient Scribe Technology Experiences Among Emergency Physicians: Cross-Sectional, Mixed Methods Pilot Survey Study. JMIR Formative Research, 2026. 10.2196/80401; PMID 41775342.
- McCrudden, and others (R0198). AI-Powered Documentation for Mental Health Providers: Retrospective Observational Mixed Methods Study. JMIR Formative Research, 2026. 10.2196/84628; PMID 41818473.
- Memon, and others (R0255). Performance, acceptability, and impact of ambient listening scribe technology in an outpatient context: a mixed methods trial evaluation. BMC Health Services Research, 2026. 10.1186/s12913-025-13954-5; PMID 41507920.
- Menz, and others (R0210). Vision-Enabled AI scribes reduce omissions in clinical conversations: evidence from simulated medication histories. npj Digital Medicine, 2026. 10.1038/s41746-026-02494-9; PMID 41748705.
- Misurac, and others (R0412). Impact of Ambient Artificial Intelligence Notes on Provider Burnout medRxiv (preprint), 2024. 10.1101/2024.07.18.24310656.
- Moura, and others (R0059). Comparative effectiveness of ambient documentation tools in primary care tool-specific variations in efficiency, documentation burden, and productivity over time. JAMIA Open, 2026. 10.1093/jamiaopen/ooag155; PMID 42583084.
- Moura, and others (R0275). Hybrid Ambient Clinical Documentation and Physician Performance: Work Outside of Work, Documentation Delay, and Financial Productivity. Journal of General Internal Medicine, 2026. 10.1007/s11606-025-09979-5.
- Nawaz, and others (R0385). Evaluating an Ambient Artificial Intelligence Scribe for Documentation Quality and Efficiency in Psychiatric Consultations: A Simulation-based Study medRxiv (preprint), 2025. 10.1101/2025.09.21.25336260.
- North, and others (R0270). Ambient listening implementation in primary care and changes in electronic health record documentation metrics: Pre-post study of an ambient listening tool. Digital Health, 2025. 10.1177/20552076251403211; PMID 41323090.
- Olson, and others (R0127). The impact of an ambient documentation tool on the care experience of clinical pharmacists embedded in ambulatory clinics: A mixed-methods evaluation. medRxiv (preprint; published version in American Journal of Health-System Pharmacy 2026 per stage 3 record), 2025. 10.64898/2025.12.19.25342691 (DOI as printed in the preprint header).
- Olson, and others (R0295). Use of Ambient AI Scribes to Reduce Administrative Burden and Professional Burnout. JAMA Network Open, 2025. 10.1001/jamanetworkopen.2025.34976; PMID 41037268.
- Palm, and others (R0281). Assessing the quality of AI-generated clinical notes: validated evaluation of a large language model ambient scribe. Frontiers in Artificial Intelligence, 2025. 10.3389/frai.2025.1691499; PMID 41199808.
- Patel, and others (R0331). Evaluating the Application of Artificial Intelligence and Ambient Listening to Generate Medical Notes in Vitreoretinal Clinic Encounters. Clinical Ophthalmology, 2025. 10.2147/OPTH.S513633; PMID 40491696.
- Pearlman, and others (R0292). Use of an AI Scribe and Electronic Health Record Efficiency. JAMA Network Open, 2025. 10.1001/jamanetworkopen.2025.37000; PMID 41071550.
- Philips, and others (R0123). Prompt-directed ambient artificial intelligence for automated multidisciplinary tumor board documentation. Annals of Oncology, 2026. 10.1016/j.annonc.2026.05.709.
- Pollak, and others (R0392). The Impact of AI Scribes on Patient and Clinician Satisfaction and Communication Research Square (preprint), 2026. 10.21203/rs.3.rs-9929134/v1.
- Prasser, and others (R0102). Ambient AI Scribes and Emergency Department Documentation Burden: Retrospective Cohort Study. JMIR AI, 2026. 10.2196/92193; PMID 42391625.
- Rabotin, and others (R0076). Propagation of Interpreter Errors by Ambient AI Scribes: Study Using Simulated Clinical Encounters. JMIR Medical Informatics, 2026. 10.2196/88734; PMID 42520279.
- Rotenstein, and others (R0183). Changes in Clinician Time Expenditure and Visit Quantity With Adoption of Artificial Intelligence-Powered Scribes: A Multisite Study. JAMA, 2026. 10.1001/jama.2026.2253; PMID 41920565; PMC13044793.
- Sanmark, and others (R0548). Evaluation of an AI Medical Scribe After 236,153 Notes Generated Across Care Levels in a European Health System: Mixed Methods Retrospective Observational Study JMIR Medical Informatics, 2026. 10.2196/90052; PMID 42430713.
- Stults, and others (R0346). Evaluation of an Ambient Artificial Intelligence Documentation Platform for Clinicians. JAMA Network Open, 2025. 10.1001/jamanetworkopen.2025.8614; PMID 40314951.
- Talman, and others (R0148). Ambient Artificial Intelligence Scribes in Pediatric Hematology-Oncology: Early Implementation of DAX Copilot. Applied Clinical Informatics, 2026. 10.1055/a-2873-3894; PMID 42114818.
- Tan, and others (R0186). Impact of an Ambient AI Scribe Among Clinicians and Patients: Real-World Prospective Observational Time-Motion Study. JMIR Medical Informatics, 2026. 10.2196/85580; PMID 41915701; PMC13037756.
- Taylor, and others (R0112). Effect of use of ambient listening technology on patient-reported communication and satisfaction ratings. Journal of the American Medical Informatics Association (JAMIA), 2026. 10.1093/jamia/ocag103; PMID 42334196.
- Taylor, and others (R0170). Quality of Clinical Notes Created by Ambient Listening Generative AI: Pragmatic Prospective Pilot Study. JMIR Medical Informatics, 2026. 10.2196/86474; PMID 41996389; PMC13089619.
- Verma, and others (R0098). Feasibility of Tailoring Artificial Intelligence-Assisted Ambient Scribes for Intensive Care Unit Rounds: Algorithm Development and Validation. JMIR Medical Informatics, 2026. 10.2196/85015; PMID 42412948.
- Wright, and others (R0324). The Effect of Ambient Artificial Intelligence Scribes on Trainee Documentation Burden. Applied Clinical Informatics, 2025. 10.1055/a-2647-1142.
- Wright, and others (R0023). Navigating Collective Bargaining Barriers to the Implementation of AI Scribe Technology Among Ambulatory Advanced Practice Providers: Mixed Methods Quality Improvement Study. JMIR Formative Research, 2026. 10.2196/92364.
- You, and others (R0308). Ambient Documentation Technology in Clinician Experience of Documentation Burden and Burnout. JAMA Network Open, 2025. 10.1001/jamanetworkopen.2025.28056; PMID 40839265.
- Zuckerman, and others (R0414). Ambient Only vs. Longitudinal Data-Enhanced AI Documentation: A Pilot Study Quantifying the Value of Historical Clinical Context in Primary Care medRxiv (preprint), 2025. 10.1101/2025.11.07.25339620.
- van Linschoten, and others (R0206). Ambient scribe in general practice: a multi-perspective before-after longitudinal mixed-methods study. npj Digital Medicine, 2026. 10.1038/s41746-026-02454-3; PMID 41772212.

## Appendix A: search strings as run, 22 October 2026

**PubMed (MEDLINE via NCBI E-utilities).** Hit count 385, retrieved 385.
`("ambient scribe*"[Title/Abstract] OR "AI scribe*"[Title/Abstract] OR "artificial intelligence scribe*"[Title/Abstract] OR "ambient documentation"[Title/Abstract] OR "ambient clinical documentation"[Title/Abstract] OR "ambient listening"[Title/Abstract] OR "DAX Copilot"[Title/Abstract] OR "Dragon Ambient eXperience"[Title/Abstract] OR "ambient artificial intelligence"[Title/Abstract]) AND ("2019/01/01"[Date - Publication] : "2026/10/22"[Date - Publication])`

**Europe PMC (REST API, result type core).** Hit count 299, retrieved 299.
`(TITLE_ABS:"ambient scribe" OR TITLE_ABS:"AI scribe" OR TITLE_ABS:"ambient documentation" OR TITLE_ABS:"ambient clinical documentation" OR TITLE_ABS:"ambient listening" OR TITLE_ABS:"DAX Copilot" OR TITLE_ABS:"ambient artificial intelligence") AND FIRST_PDATE:[2019-01-01 TO 2026-10-22]`

**OpenAIRE search API, run 1.** Title words: ambient scribe; fromDateAccepted 2019-01-01 to 2026-10-22. Hit count 145, retrieved 145.

**OpenAIRE search API, run 2.** Title words: AI scribe; fromDateAccepted 2019-01-01 to 2026-10-22. Hit count 201, retrieved 201.

**ClinicalTrials.gov (API version 2).** query.term = ambient scribe OR "AI scribe" OR "ambient documentation" OR "ambient artificial intelligence". Hit count 19, retrieved 19.

**Attempted and blocked.** OpenAlex: HTTP 429 on test and run calls, no records retrieved, logged as attempted and blocked. Semantic Scholar: query=ambient scribe, year 2019-2026, limit 100; HTTP 429, no records retrieved, logged as attempted and blocked. Crossref direct search cannot hold a phrase query and was not used as a result source; OpenAIRE, which indexes Crossref, stood in for it.

## Appendix B: search strings prepared but not run

None of the sources in this appendix was searched. Each string is marked: string prepared, run pending access. This appendix reproduces the review's pending strings file.

# Appendix: search strings prepared, runs pending access

Every string in this file is marked: string prepared, run pending access. None of these databases was searched on 22 October 2026, because the environment used for that pass holds no licensed or direct access to them. The review must not state or imply that they were searched. When access exists, run the string as written, add the date and hit count to search-log.md, and move the string from this file to the log as run.

Core concept blocks used in each string: ambient scribe terms (ambient scribe, AI scribe, artificial intelligence scribe, ambient documentation, ambient clinical documentation, ambient listening, ambient artificial intelligence), product names (DAX Copilot, Dragon Ambient eXperience, Nabla, Abridge, Ambience), date limit 1 January 2019 to search date, no language limit.

## Embase, Elsevier, via Embase.com
String prepared, run pending access.
('ambient scribe':ti,ab OR 'ai scribe':ti,ab OR 'artificial intelligence scribe':ti,ab OR 'ambient documentation':ti,ab OR 'ambient clinical documentation':ti,ab OR 'ambient listening':ti,ab OR 'ambient artificial intelligence':ti,ab OR 'dax copilot':ti,ab OR 'dragon ambient experience':ti,ab) AND [2019-2026]/py
Add Emtree checks at run time for 'medical documentation' and 'artificial intelligence' and record any change as an amendment with a date.

## CINAHL, EBSCOhost
String prepared, run pending access.
TI ( "ambient scribe*" OR "AI scribe*" OR "artificial intelligence scribe*" OR "ambient documentation" OR "ambient listening" OR "DAX Copilot" OR "Dragon Ambient eXperience" ) OR AB ( same set as TI ). Limiters: publication date 20190101 to search date. Subject heading check at run time for Documentation and Artificial Intelligence, logged if used.

## PsycINFO, APA PsycNet or EBSCO
String prepared, run pending access.
TI,AB ( "ambient scribe*" OR "AI scribe*" OR "ambient documentation" OR "ambient artificial intelligence" OR "DAX Copilot" ) AND TI,AB ( burnout OR "documentation time" OR "note quality" OR workload ). Date 2019 to search date. PsycINFO matters here for the burnout and task load scales, which the medical databases index thinly.

## Cochrane CENTRAL, Cochrane Library
String prepared, run pending access.
Title, abstract and keyword search: (ambient NEXT scribe*) OR "AI scribe" OR "ambient documentation" OR "ambient listening" OR "DAX Copilot" OR "Dragon Ambient". Date 2019 to search date. CENTRAL is the trial backstop for the ClinicalTrials.gov run, which returned 19 records on 22 October 2026.

## Scopus, Elsevier
String prepared, run pending access.
TITLE-ABS-KEY ( "ambient scribe*" OR "AI scribe*" OR "artificial intelligence scribe*" OR "ambient documentation" OR "ambient clinical documentation" OR "ambient listening" OR "ambient artificial intelligence" OR "DAX Copilot" OR "Dragon Ambient eXperience" ) AND PUBYEAR > 2018 AND PUBYEAR < 2027.

## Web of Science, Core Collection, Clarivate
String prepared, run pending access.
TS = ( "ambient scribe*" OR "AI scribe*" OR "ambient documentation" OR "ambient listening" OR "ambient artificial intelligence" OR "DAX Copilot" OR "Dragon Ambient eXperience" ). Timespan 2019-01-01 to search date.

## ACM Digital Library
String prepared, run pending access.
Title and abstract fields: ("ambient scribe" OR "AI scribe" OR "ambient documentation" OR "clinical scribe" AND "artificial intelligence"). Filter: 2019 to search date. The ACM pass hunts system evaluations and error audit work that medical databases miss. Any ACM record found still has to pass the same eligibility screen.

## WHO ICTRP
String prepared, run pending access.
Condition field left blank. Intervention field: ambient scribe; AI scribe; ambient documentation; DAX. Run as four single term searches and merge, since the register handles combined strings poorly. Date of registration from 2019.

## Google Scholar, first 200
String prepared, run pending access.
"ambient scribe" clinician documentation. Sort by relevance, take the first 200, screen as records, and log the date, since Scholar counts shift between runs. This pass is a check on the database set, not a source in its own right for the PRISMA identification count until it has been run and dated.


## Appendix C: characteristics of included studies

One row per included study, from the extraction file. Product group is the primary named product family used for subgroup classification. The full extraction file, with setting, specialty, comparator, funding and conflicts per study, is published with the review data.

| Record | Study | Design | Product group | Country | Clinicians n | Encounters or notes n | Vendor class | Report type |
|---|---|---|---|---|---|---|---|---|
| R0012 | Golos 2026 | uncontrolled before-after | Other, mixed, anonymised or not named | United States | 41 eligible; 8 persistent users (19.5%) | not stated in abstract | independent | journal article |
| R0023 | Wright 2026 | non-randomised controlled | Abridge | United States | 15 pilot APPs (12 nurse practitioners, 3 physician assistants); 98 nonpilot APPs | 8100 pilot encounters (5403 scribe notes, 66.7%); 32,983 nonpilot encounters | vendor | journal article |
| R0029 | Draper 2025 | note audit | Other, mixed, anonymised or not named | United Kingdom | not applicable (actor consultations) | 8 scenarios x 7 products = 56 summaries | independent | journal article |
| R0030 | Draper 2025 | note audit | Other, mixed, anonymised or not named | United Kingdom | not applicable (actor consultations) | 5 conditions (memory loss, diarrhoea, headaches, skin rash, prostate); summaries typically 25-30 points of information | independent | journal article |
| R0043 | Kashiouris 2026 | non-randomised controlled | Abridge | United States | 329 active ED clinicians (166 used AI for at least 1 note; 163 control); workload survey 25 pre and 15 post of 329 invited | 315,242 ED clinical notes (AI used in 8.6%); postintervention 26,583 AI notes | unclear | journal article |
| R0048 | Major 2026 | cross-sectional | Abridge | United States | not applicable (summaries analysed) | 1007 summaries extracted; 982 analysed after excluding 25 incomplete | independent | journal article |
| R0059 | Moura 2026 | non-randomised controlled | Abridge | United States | 163 providers in analytic cohort (150 adopters: Tool A 65, Tool B 68, Tool C 17; plus 13 non-adopters described only) | 59130 provider-days (encounter count not stated) | independent | journal article |
| R0068 | Grand 2026 | controlled before-after | DAX / Dragon Ambient eXperience | United States | 1 surgeon | 112 encounters (55 AI scribe, 57 traditional documentation) | independent | journal article |
| R0076 | Rabotin 2026 | note audit | Other, mixed, anonymised or not named | United States | not applicable - 3 native Spanish-speaking medical students simulated patient, clinician and interpreter in consistent roles | 5 scripted scenarios with 20 planted interpreter errors; 20 errors evaluated per vendor (40 note evaluations) | independent | journal article |
| R0077 | Alcazar-Peral 2026 | non-randomised controlled | Other, mixed, anonymised or not named | Spain | 7147 clinicians used Scribe at least once (3506 with more than 100 queries, 1617 with more than 500); survey Round 1 n=184, Round 2 n=163 | 2339281 Scribe-assisted encounters of 11599484 outpatient visits (overall usage rate 20.17%) | vendor | journal article |
| R0078 | Anderson 2026 | uncontrolled before-after | Other, mixed, anonymised or not named | United States | 16 third-year residents eligible/invited; 15 enrolled and contributed EHR data; 13 completed pre- and postintervention surveys | not stated | independent | journal article |
| R0098 | Verma 2026 | note audit | Other, mixed, anonymised or not named | United States | not applicable (simulated cases); evaluators: 2 physicians in Phase 1, 3 physicians in Phase 2 | Phase 1: 1 case (C1) per model/prompt version; Phase 2: 5 cases (C1-C5), 1 note per model per case (10 notes) | unclear | journal article |
| R0102 | Prasser 2026 | non-randomised controlled | DAX / Dragon Ambient eXperience | United States | 100 attending physicians | 10344 encounters (1881 ambient, 18.2%; 8463 non-ambient) | independent | journal article |
| R0105 | Blease 2026 | cross-sectional | Heidi | United Kingdom | 141 current GP users (of 1003 survey respondents) | survey sample (Doctors.net.uk Omnibus); no encounter/note denominator | independent | journal article |
| R0111 | Harvey 2026 | uncontrolled before-after | Abridge | United States | 79 providers completing pilot (80 recruited; 45 high users with use in >=60% of notes) | more than 25600 notes generated (text also prints more than 25000) | independent | journal article |
| R0112 | Taylor 2026 | non-randomised controlled | Other, mixed, anonymised or not named | United States | 31 pilot physicians (28 with patient surveys) and 125 control physicians | 31917 patient surveys (7164 pilot; 24753 control) | independent | journal article |
| R0123 | Philips 2026 | controlled before-after | Abridge | United States | not stated (core multidisciplinary tumor board team; number of clinicians not reported) | 12 tumor boards across 4 cohorts; patients discussed: unprompted 131, prompt-directed 73, manual 48 (paired subset, overlapping), validation 81 | independent | journal article |
| R0127 | Olson 2025 | uncontrolled before-after | Abridge | United States | 41 pharmacists given ADT licences (40 used ADT at least once; 30 with usable survey + Epic Signal data analysed) | ADT used in 65% of eligible encounters (Table 2: utilisation rate 64.8%, SD 21.8); total eligible encounter count not printed (programme context: about 210000 encounters per year) | independent | preprint |
| R0128 | Gladysz 2026 | other | Other, mixed, anonymised or not named | Switzerland | 2 (1 native Swiss German-speaking consultant; 1 non-native German-speaking consultant) | 12 simulated patient encounters; 48 medical notes (12 per workflow x 4 workflows, as printed in quality prompt) | independent | journal article |
| R0131 | Lawrence 2026 | uncontrolled before-after | Other, mixed, anonymised or not named | United States | 97 ambulatory clinicians (number in pre-post efficiency subset not stated in available text) | not stated in available text | unclear | journal article |
| R0134 | Husa 2026 | interrupted time series | DAX / Dragon Ambient eXperience | United States | 1547 active users in analysis (1073 [69.4%] physicians; 272 [17.6%] nurse practitioners; 197 [12.7%] physician assistants; 5 [0.3%] midwives); 16149 observations | Total appointment/encounter count not stated; 16149 observations from 1547 clinicians | independent | journal article |
| R0148 | Talman 2026 | non-randomised controlled | DAX / Dragon Ambient eXperience | United States | 29 providers eligible (15 attendings, 9 fellows, 5 APPs); 10 used DAX at least once; 6 repeat users (used more than twice) in the comparative analysis | 11544 outpatient encounters in total (427 [3.7%] DAX); analysis subset (repeat users) 1615 encounters: 414 DAX and 1201 non-DAX (Table 1) | independent | journal article |
| R0155 | Akhlaghi 2026 | other | Other, mixed, anonymised or not named | Australia | 63 provided access (40 consultants and 23 trainees); 20 used the system (9 consultants [22.5%] and 11 trainees/registrars [48%]) | 248 ED presentations (185 [74.6%] by trainees; 63 [25.4%] by consultants) | vendor | journal article |
| R0165 | Draper 2026 | note audit | Other, mixed, anonymised or not named | United Kingdom | not applicable (trained actors; human voice actors for Irish, Chinese and Nigerian accents) | Personality: 20 consultations (4 scenarios x 5 personality types); Accents: 70 consultations in total (50 accent combinations plus 5 fully synthetic controls plus 15 human-accent consultations); Speech impairments: recordings for 5 profiles (count per profile not stated in main text) | independent | journal article |
| R0170 | Taylor 2026 | note audit | Other, mixed, anonymised or not named | United States | 31 physicians (volunteers) | 7545 AI-generated notes in pilot; 356 notes evaluated (4.7%) | independent | journal article |
| R0173 | Chim 2026 | note audit | Other, mixed, anonymised or not named | United Kingdom | not applicable (no clinicians) | 420 test transcripts (10 patients x 6 relationship types x 7 information topics); notes generated per model per prompt condition | independent | journal article |
| R0179 | Foo 2026 | cross-sectional | Other, mixed, anonymised or not named | Australia | 2 GPs generating notes; 3 blinded GP raters; 4 patient actors | 20 clinical notes rated (4 cases x 5 scribes: 4 AI + 1 human) | unclear | journal article |
| R0181 | Etagiuri 2026 | RCT | Heidi | Canada | 1 surgeon | 304 patients eligible; 291 enrolled; 279 randomised and analysed (139 AI scribe, 140 conventional) | independent | journal article |
| R0183 | Rotenstein 2026 | non-randomised controlled | Abridge | United States | 8581 clinicians (1809 AI scribe adopters; 6772 nonadopters) | 181273 clinician-month observations (encounter counts not printed) | independent | journal article |
| R0186 | Tan 2026 | uncontrolled before-after | Other, mixed, anonymised or not named | Singapore | 9 clinicians (experienced users; >=30 scribe notes in prior 3 months; convenience sample of 27 eligible) | 169 consultations observed (78 with AI scribe, 91 without); patient surveys n=39 | vendor | journal article |
| R0191 | Khan 2026 | note audit | Other, mixed, anonymised or not named | Saudi Arabia | 6 participating physicians in stage 2; 22 physicians in experience survey (stage 1 assessor clinician count not stated) | 64 encounters (stage 1); 55 consultations (40 Arabic, 15 English) (stage 2) | vendor | journal article |
| R0198 | McCrudden 2026 | uncontrolled before-after | Other, mixed, anonymised or not named | United States | 162 full-time and 1366 contractual MHPs used Smart Notes; productivity analysis: 140 full-time and 1698 contractual MHPs | 286,911 Smart Notes submitted (88,591 full-time; 198,320 contractual) plus 237,955 traditional progress notes over about 1 year; 466,139 total Smart Notes for quality ratings denominator as printed | vendor | journal article |
| R0205 | Marquis 2026 | cross-sectional | DAX / Dragon Ambient eXperience | United States | 16 EPs granted access; 14 survey respondents (8 general EM, 6 pediatric EM) | not reported (survey study; no encounter or note count) | independent | journal article |
| R0206 | van Linschoten 2026 | uncontrolled before-after | Other, mixed, anonymised or not named | Netherlands | 12 GPs | 535 consultations observed (264 baseline, 271 intervention); 333 complaints in baseline and 339 in intervention consultations | independent | journal article |
| R0209 | Li 2026 | uncontrolled before-after | Abridge | United States | not stated in available text | 6,026 outpatient clinical notes; manual review of 50 paired notes | unclear | preprint |
| R0210 | Menz 2026 | note audit | Other, mixed, anonymised or not named | Australia | 10 clinical pharmacists (5 pairs) recorded the simulated interviews; no real documenting clinicians | 110 simulated recordings (10 training, 100 test); test set 2,160 data points (300 patient-detail and 1,860 medication-specific) | independent | journal article |
| R0232 | Davis 2026 | uncontrolled before-after | DAX / Dragon Ambient eXperience | United States | 49 (46 physicians, 3 nurse practitioners) | Press Ganey survey responses: overall assessment 1640 pre / 3034 post; concern 1643 pre / 3027 post; recommending 1623 pre / 3021 post (encounter count not stated) | independent | journal article |
| R0235 | Afshar 2025 | stepped wedge | Abridge | United States | 66 (48 physicians; 5 nurse practitioners; 13 physician assistants) | 71487 notes (27092 [38%] ambient AI-generated; 44395 human-authored) | independent | journal article |
| R0240 | Adler-Milstein 2026 | uncontrolled before-after | Ambience | United States | 310 adopting physicians (252 [81.3%] with postadoption survey) | mean 58.7% (SD 32.9%) of weekly encounters used the tool in 12 weeks post adoption (total encounter count not stated) | independent | journal article |
| R0245 | Castro 2026 | non-randomised controlled | Other, mixed, anonymised or not named | United States | not applicable (notes analysed; clinician count not stated) | 20302 notes (ambient AI scribe 5076; human virtual scribe 5075; no scribe after deployment 5075; no scribe prior to deployment 5076) | independent | journal article |
| R0255 | Memon 2026 | uncontrolled before-after | Other, mixed, anonymised or not named | Australia | 100 clinicians with trial licences (medical officers, clinical nurses running nurse-led clinics, registrars) | 7499 consultations using the scribe during the trial; 18 note pairs PDQI-9 assessed; 21 note pairs ROUGE analysed; staff survey 43/100 responses; 22 patient surveys | independent | journal article |
| R0256 | Brunner 2026 | note audit | Other, mixed, anonymised or not named | United States | 16 specialist clinicians (4 per specialty); Table 1 footnote: ratings include 82 respondents | simulated encounters per specialty (count in eTable 1, Supplement 1, not in main text) | independent | journal article |
| R0257 | Lukac 2025 | RCT | DAX Copilot and Nabla (two arms) | United States | 238 outpatient physicians (DAX 79; Nabla 79; control 80) | DAX 24696 visits; Nabla 23653 visits; control 24020 encounters | independent | journal article |
| R0265 | Ghanem 2026 | note audit | DAX / Dragon Ambient eXperience | United States | 3 author-graders; no resident clinicians tested as participants | 25 simulated inpatient scenarios | unclear | journal article |
| R0270 | North 2025 | uncontrolled before-after | Abridge | United States | 332 primary care physicians in paired analysis (582 unique physicians with data; 333 ever used Abridge) | 22495 physician-weeks; total note count not stated | independent | journal article |
| R0273 | Alpert 2025 | uncontrolled before-after | Other, mixed, anonymised or not named | United States | 10 primary care physicians | median 61 encounters per physician (range 1-181; IQR 9.5-75) | independent | journal article |
| R0275 | Moura 2026 | non-randomised controlled | Other, mixed, anonymised or not named | United States | 181 attending physicians and advanced practice clinicians (66 voluntarily enrolled; 36%) | not stated in abstract | independent | journal article |
| R0277 | Foo 2025 | note audit | Other, mixed, anonymised or not named | Australia | 3 experienced general practitioner raters (blinded); no clinicians generating notes as participants | 4 standardised clinical scenarios from the Royal Australian College of General Practitioners examination repository | unclear | journal article (conference proceedings paper) |
| R0278 | Furrukh 2025 | uncontrolled before-after | DAX / Dragon Ambient eXperience | United States | 6 residents | not stated | independent | journal article |
| R0281 | Palm 2025 | note audit | Suki | United States | not stated (clinicians in 5 specialties; 1 Gold note author per specialty) | 97 recordings; 194 notes (97 AI and 97 physician gold notes); 388 paired reviews | vendor | journal article |
| R0287 | Harvey 2025 | uncontrolled before-after | Abridge | United States | 79 ambulatory providers (8 surgical specialty participants; 3 surgeons analysed) | not stated (clinic visits December 2024 to February 2025) | unclear | journal article |
| R0292 | Pearlman 2025 | non-randomised controlled | Abridge | United States | 603 (125 AI scribe users; 478 covariate-balanced nonusers) | 40,350 encounters; scribe used in 19,486 (48.3%) by pilot clinicians | independent | journal article |
| R0295 | Olson 2025 | uncontrolled before-after | Abridge | United States | 263 analysed (451 enrolled; 272 completed both surveys) | not stated (252 of 263 [95.9%] generated at least 5 notes using the ambient AI scribe) | vendor | journal article |
| R0308 | You 2025 | uncontrolled before-after | Other, mixed, anonymised or not named | United States | 1,430 enrolled (873 MGB; 557 Emory); survey respondents 265 at 42 days and 192 at 84 days (MGB) and 62 matched (Emory) | not stated | independent | journal article |
| R0312 | Guo 2025 | uncontrolled before-after | Abridge | United States | 124 physicians enrolled; 68 met inclusion criteria (>=4 weeks use and >=10 notes); final analysis 42 at 1 month, 32 at 2 months, 31 at 3 months | total note/encounter count not printed; minimum 10 notes per included participant | unclear | journal article |
| R0313 | Arko 2025 | note audit | Other, mixed, anonymised or not named | Not stated | not applicable (no clinicians) | 2 simulated encounters x 4 vendors (8 notes) | unclear | journal article |
| R0316 | Ha 2025 | note audit | Other, mixed, anonymised or not named | Canada | not applicable (4 research team members operated the scribes; no treating clinicians) | 4 standardized encounters x 3 trials per scribe (12 appointments per scribe; 72 notes/transcripts in total) | independent | journal article |
| R0324 | Wright 2025 | uncontrolled before-after | Abridge | United States | 55 trainees selected/invited; 47 enrolled and provisioned (completed presurvey); 43 used the tool at least once; 37 completed both surveys; 31 with Epic Signal data | vendor utilisation: mean (SD) 23.3 (17.9) total notes generated per trainee (total encounter count not printed) | unclear | journal article |
| R0331 | Patel 2025 | note audit | Other, mixed, anonymised or not named | United States | no treating clinicians; 5 practicing board-certified retina specialist graders | 10 scripted vitreoretinal diagnoses/encounters x 2 engines = 20 notes | independent | journal article |
| R0346 | Stults 2025 | uncontrolled before-after | Abridge | United States | 100 clinicians selected (92 physicians, 8 advanced practice clinicians); 92 with EHR metrics; 57 completed both pre and post surveys | encounter/note total not printed; EHR metrics per appointment over 3 months pre and 3 months post | vendor | journal article |
| R0353 | Hudson 2025 | RCT | Abridge | United States | 40 ambulatory providers | 2 comparable clinic sessions per participant (encounter/note counts not stated) | vendor | journal article |
| R0355 | Kakaday 2025 | RCT | DAX / Dragon Ambient eXperience | United States | 45 (DAX n=25; control n=20) | visit counts not stated; clinicians required >=100 outpatient visits/month at entry | unclear | journal article |
| R0360 | Duggan 2025 | uncontrolled before-after | DAX / Dragon Ambient eXperience | United States | 46 (physicians 40; nurse practitioners 2; physician assistants 4) | not stated (mean 36.5 visits/week per clinician) | independent | journal article |
| R0363 | Biro 2025 | note audit | Other, mixed, anonymised or not named | United States | no practising clinicians; 2 researcher-readers as patients plus medical residents as physicians; 2 error reviewers (JB or JLH categorisation) | 44 draft notes (11 scripts x 2 products x 2 readings) | independent | journal article (research letter) |
| R0373 | Balloch 2024 | non-randomised controlled | Other, mixed, anonymised or not named | United Kingdom | 8 enrolled (5 consultants; 3 allied health professionals); 7 with timing data | 47 consultations (23 EHR-alone, 1 incomplete; 24 AI tool); timing averages from 42 consultations by 7 clinicians | vendor | journal article |
| R0385 | Nawaz 2025 | RCT | Lyrebird | United Arab Emirates (Dubai) | 8 (3 consultants; 2 specialists; 3 residents) | 16 documentation episodes (8 paired observations); 128 observations across outcome measures as printed | vendor | preprint |
| R0392 | Pollak 2026 | uncontrolled before-after | Other, mixed, anonymised or not named | United States | 30 consented (10 per specialty); 29 recorded; 28 completed baseline surveys; 25 completed at least one follow-up survey | 232 audio-recorded encounters (8 per clinician; 4 pre and 4 post); 230 coded (2 uncoded due to audio issues / non-English); 231 patient surveys (116 no scribe, 115 scribe) | independent | preprint |
| R0395 | De John 2026 | note audit | Other, mixed, anonymised or not named | South Africa (Groote Schuur Hospital, Cape Town) | not stated (encounters by registrars 39/49 and consultants 10/49) | 53 encounters recorded; 49 analysed (1 prompt-optimisation encounter prospectively excluded, 2 excluded for device truncation, 1 for insufficient content); 49 AI notes and 49 handwritten notes | vendor | preprint |
| R0408 | Bergman 2026 | note audit | Heidi | Multinational (five European countries) | 40 note-writing clinicians (8 per site; junior-to-middle-grade, Foundation Year to Specialty Registrar or equivalent; mean age 29 years, range 24-34); 67 unique blinded clinical evaluators | 400 consultations planned; 385 paired consultations analysed (770 notes): Cambridge 80, Paris 80, Milan 80, Barcelona 79, Cologne 66; 15 excluded for missing primary evaluation; separate 15-consultation Allied Health arm excluded before pooling | vendor | preprint |
| R0412 | Misurac 2024 | uncontrolled before-after | Other, mixed, anonymised or not named | United States | 38 volunteer physicians and advanced practice providers enrolled; 35 completed pre and post surveys (92%) | not stated as total; median 51 patient encounters per participant in the 5-week trial (IQR 17-85); average visit duration 18 minutes | independent | preprint |
| R0414 | Zuckerman 2025 | cross-sectional | Other, mixed, anonymised or not named | United States | not stated (limited number of physicians at two sites, per Limitations) | 354 primary care encounters; 400 condition instances analysed (DM n=119, HTN n=281; some encounters addressed both conditions); each instance documented by both methods | vendor | preprint |
| R0426 | Jain 2025 | note audit | Other, mixed, anonymised or not named | United States | not applicable (volunteer participants enacting scenarios; 1 experienced human scribe with over 5 years of professional scribing experience) | 6 clinical scenarios, each documented by 7 scribes (42 notes); scored by 4 LLM evaluators (OpenAI o1-pro, Grok 3, Claude 3.5, DeepSeek R1) | unclear | preprint |
| R0435 | Bauer 2026 | RCT | Other, mixed, anonymised or not named | Netherlands | 35 healthcare providers (physicians, physician assistants and nurse practitioners) | 529 consultations recorded: 387 in intervention weeks and 142 in control weeks; 456 Autoscriber-generated summaries in total (some generated in control weeks contrary to instruction) | vendor | preprint |
| R0548 | Sanmark 2026 | uncontrolled before-after | Other, mixed, anonymised or not named | Sweden (Capio Ramsay Santé) | 1295 clinicians in note metadata cohort (1302 generated >=1 note, 7 nonclinical accounts excluded); 517 met survey eligibility, 451 surveyed, 177 responded (39.2% of invited; 34.2% of eligible) who created 67,679 notes | 376,596 notes in original dataset; 236,153 unique notes in final analytic dataset; 138,196 notes excluded (no recorded edits) and 2,247 excluded (editing time >3 hours) | vendor | journal article |
