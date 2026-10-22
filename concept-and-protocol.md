# Ambient AI Scribes: Time Saved, Work Shifted, Errors Added
## A Cochrane-style systematic review and meta-analysis. Concept and protocol, 22 October 2026
Author: Raphael Malikian, independent researcher. Healthcare founder and operator, clinical AI builder. No industry affiliation. No conflicts of interest.

Status: Protocol stage. No screening or data extraction has started. That order matters. PROSPERO registration comes before extraction, and pooled results will come only from studies found, screened and checked in this review. Nothing in this document invents a result.

## The concept in one paragraph

Health systems are buying ambient AI scribes at scale. Kaiser Permanente rolled one tool out to 7,260 physicians across 2,576,627 encounters. Menlo Ventures put ambient scribe spending at $600M in 2025, up 2.4 times on the year before, the largest single slice of $1.4B in healthcare AI spending. The claim sold to boards is simple: less typing, less after-hours work, less burnout. The evidence behind that claim is thin, mixed and, in places, contradictory. In the first head to head randomised trial, one leading product cut time in note by 9.5 percent and the other did not cut it at all. Separate audits found omissions in 18 percent of evaluated notes and hallucinations in 11.5 percent. No published synthesis pools benefit and error burden together. That is the gap this review fills.

## Why this topic, and why the other three lose

Scoring used four tests: demand, how little synthesis exists, whether enough primary studies exist to pool, and whether one reviewer with LLM help and human checking can do the work well.

1. Ambient AI scribes. Rank 1. One prior meta-analysis only, Zhao 2025 in BMC Medical Informatics and Decision Making, 23 studies, pooled SMD minus 0.71 for documentation burden, time SMD minus 0.72, heterogeneity I squared 93.3 percent, study quality generally low. It covered AI note tools in general, not ambient scribes alone, and it came out before the 2025 randomised trials. Pool now holds about 25 to 40 studies. Outcomes use standard measures: minutes in note from EHR audit logs, after-hours time, Mini-Z and Stanford Professional Fulfillment Index scores.

2. LLM hallucinations in clinical use. Rank 2, and only in a narrow form. No review pools clinical incidence. The problem is arithmetic. Rates run from 1.47 percent per sentence in a summarisation pipeline to 50 to 82 percent per adversarial prompt, and 28.6 to 91.4 percent for made up citations. Those numbers do not share a denominator, so they cannot be averaged honestly. A second review in this series can take one task only, for example errors per generated clinical note, or made up citations per reference list.

3. Sepsis and deterioration prediction, including the Epic Sepsis Model. Rank 3. A direct competitor landed in 2026. Patel in Journal of General Internal Medicine pooled 22 studies and more than 2.3 million patients, Epic Sepsis Model AUROC 0.65. At least five earlier sepsis meta-analyses sit behind it. A new entry needs a different angle, such as alert burden or calibration, and prediction model methods that are heavy for one reviewer.

4. LLMs for diagnosis against clinicians. Rank 4. Do not do this one. Takita 2025 pooled 83 studies at 52.1 percent accuracy. Shan 2025 covered 30 studies. A npj Digital Medicine review covered 50. The exam to practice gap has already been reviewed across 39 benchmarks. Any new paper repeats them.

Cochrane check: no Cochrane review was found for any of the four topics. That check needs one repeat pass through the Cochrane Library and PROSPERO before title registration, because one ambient scribe review is already in progress at PROSPERO, CRD420250650612. Its scope decides how this review sets its dates and products so the two do not collide.

## The hard constraint on the word Cochrane

Cochrane will not take a one person review. Its proposal system states a proposal will be rejected if it does not include at least two authors. An independent team can publish there without joining a group, through the Central Editorial Service, but it must bring its own search specialist if it has no group support. Protocol deadline is 90 days after invitation, the review itself 365 days, and the search must be under 12 months old at submission.

So there are two honest routes.

Route A, Cochrane-style, solo byline intact. Register on PROSPERO, follow Cochrane Handbook version 6.5 methods in full, publish the preprint free on Zenodo and medRxiv, then submit by the subscription route to a journal that takes this format with no fee. JBI Evidence Synthesis is the closest fit found. BMJ Open charges 2,163 pounds and Systematic Reviews charges 2,390 pounds, so both are out under the free only rule.

Route B, actual Cochrane. Recruit one co-author who can act as second screener and, ideally, search specialist. That co-author is not decoration. Duplicate screening and extraction are what make the numbers defensible anyway.

My recommendation is Route A for this first review, with a second human checker for screening decisions even if that person does not take authorship. The 2025 RAISE statement from Cochrane, Campbell, JBI and CEE allows AI help in evidence synthesis with human oversight, a stated reason, and full reporting of tool, version and checks. LLM screens, human decides. That sentence goes in the protocol, word for word in substance.

## Protocol

### Title
Ambient artificial intelligence scribes for clinical documentation: effects on documentation time, after-hours work, clinician burnout, note quality and note errors. A systematic review and meta-analysis.

### Review question
To assess the effects of ambient AI scribes, compared with usual documentation, dictation or manual typing, on documentation time, after-hours work, clinician burnout, note quality and note errors in outpatient and inpatient care.

### PICO
Population: clinicians who document patient encounters, any specialty, any country. Physicians, advanced practice clinicians, and other documenting clinicians analysed apart where data allow.
Intervention: ambient AI scribe. Software that listens to a clinical encounter, with consent, and drafts a note for clinician review and signature. Products include DAX Copilot, Nabla, Abridge, Ambience and equivalents. Tools that only transcribe dictation are out. Tools where the clinician types a prompt and gets a summary are out, unless the study reports them apart.
Comparator: usual documentation, manual typing, dictation, human scribe, or pre-implementation period in before and after studies.
Outcomes, critical: documentation time per note or per day from EHR audit logs; after-hours documentation time; burnout and work exhaustion on a validated scale; note errors, split into omissions, hallucinations or fabrications, and wrong inclusions, per note.
Outcomes, important: note quality on a validated instrument; professional fulfillment; time to note closure; patient experience where the study measured it; note length, reported as a possible cost, not a benefit.

### Study designs
Randomised trials, including stepped wedge. Non-randomised studies with a concurrent control. Before and after studies, kept in a separate synthesis from controlled studies. Qualitative work, editorials and vendor white papers are out of the synthesis and in the background only.

### Search
Databases: MEDLINE (PubMed), Embase, CINAHL, PsycINFO, Cochrane CENTRAL, Scopus or Web of Science, and ACM Digital Library for system evaluations that medical databases miss. Trial registers: ClinicalTrials.gov and WHO ICTRP. Grey sources: first 200 Google Scholar results, reference lists of included studies and of Zhao 2025, forward citation chasing on the two 2025 NEJM AI trials.
Dates: 1 January 2019 to search date. Ambient products in current form did not exist in practice before then. No language limit at search. Non-English studies translated or listed as awaiting classification, never silently dropped.
Example MEDLINE core, to be peer reviewed before registration: (ambient OR AI scribe OR artificial intelligence scribe OR automated documentation OR DAX OR Nabla OR Abridge OR Ambience) AND (documentation time OR burnout OR note quality OR clinical documentation). Full strings for every database go in an appendix, copied exactly as run.

### Selection and extraction
Two stage screening, title and abstract then full text. LLM tool does first pass ranking and data extraction drafts. A human checks every include decision, every exclude at full text with one stated reason, and every extracted number against the source PDF. Disagreements and corrections logged. Extraction items: setting, specialty, product and version, consent model, study design, clinician count, encounter count, follow up length, each outcome with its measure and time point, error audit method and who graded the notes, funding, and vendor involvement in design or analysis. Vendor funding is an extraction item, not a footnote. Half this literature is vendor linked, and readers deserve that count early.

### Risk of bias
RoB 2 for randomised trials, five domains. ROBINS-I for non-randomised studies, seven domains, with confounding pre-specified: baseline documentation load, specialty mix, concurrent EHR changes, and self-selection of keen users into scribe groups. That last one is the bias that runs through this whole field. Early adopters volunteer, report relief, and would probably report relief for almost any tool that promised help.

### Synthesis
Random effects meta-analysis, inverse variance, in R. Standardised mean difference for burnout and task load scales that differ across studies, mean difference where minutes are reported on the same basis. Error outcomes pooled as proportions per note, per study, with omissions and hallucinations kept apart. Pooling them into one error number would hide the point, since omissions made up 83.8 percent of errors in one seven product study and the rarer fabrications carried more clinical weight.
Heterogeneity: I squared and tau squared reported, prediction interval where ten or more studies pool. Zhao 2025 found I squared 93.3 percent, so heterogeneity is expected, not a surprise failure. The job is to explain it.
Pre-specified subgroups: product; specialty (primary care against other); study design (randomised against before and after); vendor funded against independent; follow up under 90 days against 90 days or more.
Sensitivity: controlled studies only; studies at low or moderate risk of bias only; leave one product out.
Reporting bias: funnel plot and Egger test only where ten or more studies pool, plus a comparison of registered against published outcomes where a registration exists.
Certainty: GRADE per outcome, for a summary of findings table with at most seven outcomes. Expected downgrades, stated now so they cannot be softened later: risk of bias from self-selected users, inconsistency if heterogeneity stays high, and indirectness where burnout was measured at 30 days and sold as a lasting effect.

### What the discussion has to argue, with the numbers attached
First, benefit is a product property, not a class property. Lukac 2025 randomised 238 physicians three ways. Nabla cut time in note 9.5 percent, p equals 0.02. DAX cut it 1.7 percent, not significant. A review that averages those two into one scribe effect tells a purchasing board something false.
Second, time saved and vigilance added are the same intervention seen from two ends. Olson 2025 reported burnout falling from 51.9 to 38.8 percent at 30 days with Abridge across six systems. Afshar 2025, stepped wedge, 71,487 notes, found work exhaustion down 0.44 points. Set that against audit work finding omissions in 18 percent of notes and hallucinations in 11.5 percent, with a small share carrying risk of serious harm if uncorrected. The clinician stops typing and starts proofreading machine text under time pressure. Whether that trade is worth it depends on the error rate, the review time, and who catches what. No vendor brochure reports all three.
Third, burnout gains measured at 30 to 90 days may be novelty, relief at being given anything, or real. The discussion will separate short follow up from longer follow up and say plainly which claim the data can carry.
Fourth, guidance has already moved ahead of evidence. NHS England issued ambient scribe guidance on 27 April 2025 covering device status, safety cases and human review. The Joint Commission and CHAI issued responsible use guidance on 17 September 2025 covering local validation and monitoring. The FDA digital health advisory meeting on 6 November 2025 named hallucinations and drift as risks that need controls. Health systems are not waiting. A pooled estimate with a GRADE rating is the thing those documents keep asking for and cannot cite, because it does not exist yet.

## Cochrane-style structure for the finished manuscript
Title page and citation. Structured abstract, under 1,000 words: rationale, objectives, search methods, eligibility, outcomes, risk of bias, synthesis methods, included studies, results per outcome with GRADE, authors conclusions, funding, registration. Plain language summary in the same order, written for a clinic manager, not a researcher. Summary of findings table placed before the background, seven outcomes at most. Background: the documentation burden, what an ambient scribe is and how it is supposed to work, why this review is needed now. Objectives in one sentence. Methods in seven parts, starting with differences between protocol and review. Results: PRISMA flow with counts, description of studies, risk of bias, synthesis by outcome. Discussion: summary of main results, limits of the evidence, limits of this review, agreement and disagreement with Zhao 2025 and the rapid reviews. Authors conclusions split into practice and research, with no instruction on how any clinic should deploy a product. Declarations, AI use disclosure as the venues require it, data and code availability, references, characteristics of included and excluded studies, full search strings in appendices. Main text limit 12,000 words.

## Conference abstract, ready shape
Background: ambient scribes are deployed at enterprise scale on limited evidence. Objectives: pool effects on time, after-hours work, burnout and note errors. Methods: Cochrane Handbook methods, RoB 2 and ROBINS-I, GRADE, PROSPERO registered, LLM assisted screening with full human checking. Results and conclusions stay blank until extraction is done. Submitting an abstract with invented results would end the credibility this series is built to create. Targets, free submission only: CHIL 2027, SIIM27, MedInfo 2027 (submissions open 30 October 2026 per current series notes), AMIA where a no fee route exists. Registration costs flagged before any acceptance is acted on.

## Rollout as a series
Review 1: ambient scribes, benefit against error burden, as above.
Review 2: LLM errors in one task. Errors per generated clinical note, or made up citations. One denominator, chosen after a scoping pass.
Review 3, only if a new angle holds up: prediction model alert burden and calibration on external validation, not another AUROC pool.
Diagnosis accuracy is closed as a topic. Three reviews that each fill a real gap beat four that chase a crowded one.

## De-AI and honesty checks before anything ships
Written under Raphael's de-AI copy rules. No em dashes. Banned words checked. No forced triplets as decoration. Every strong claim in the same paragraph as its number. AI use in the review process disclosed where a venue asks for it, in factual terms. No clinical recommendation, no medication advice, nothing that reads as practice of medicine. This is evidence synthesis and policy discussion only.

## Sources for the headline claims in this protocol
Zhao 2025, BMC Medical Informatics and Decision Making, PMC12836966. Lukac 2025, NEJM AI, PMC12768499. Afshar 2025, NEJM AI, PubMed 41625485. Olson 2025, JAMA Network Open, Abridge pre-post study. Error audit, PMC13089619: omissions 18 percent, hallucinations 11.5 percent. Seven product standardised study, PMC13528381. Asgari 2025, npj Digital Medicine, hallucination 1.47 percent per sentence. Omar 2025, Communications Medicine, false detail repeated in 50 to 82 percent. Patel 2026, Journal of General Internal Medicine, Epic pooled AUROC 0.65, 22 studies. Takita 2025, pooled diagnostic accuracy 52.1 percent, 83 studies. Kaiser Permanente TPMG ambient rollout, 7,260 physicians, 2,576,627 encounters. Menlo Ventures 2025 State of AI in Healthcare, ambient scribes $600M. AMA 2024 physician AI use, 66 percent against 38 percent in 2023. NHS England ambient scribing guidance, 27 April 2025. Joint Commission and CHAI RUAIH, 17 September 2025. FDA DHAC, 6 November 2025. Cochrane Handbook version 6.5, 2024, chapters III, 8, 14 and 25. RAISE position statement, 2025.
