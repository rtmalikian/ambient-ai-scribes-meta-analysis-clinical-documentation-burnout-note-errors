# Stage 5 analysis results: ambient AI scribes meta-analysis

Analysis date: 22 October 2026. Script: `meta_analysis.py` (this folder). Machine readable results: `analysis-results.json`. Selected effects, one per study per outcome, with the derivation for each: `selected-effects.csv`. Every number in this document was produced by the script. No number was copied from a paper abstract or entered from memory.

## Methods used in this stage

- Random effects, inverse variance, tau squared estimated by REML.
- Hartung-Knapp confidence intervals where k is 3 or more. Where k is 2, a normal interval on the model based standard error is used and the prediction interval is reported as not estimable.
- Prediction intervals use a t distribution with k minus 2 degrees of freedom and the model based standard error.
- Standardised mean differences are Hedges g where they are computed from group means and SDs. Where a study printed a model based difference with a CI, the effect is that difference divided by a standardiser taken from the same study (pooled raw SD, baseline SD, or SD of change), and the SE is the printed SE divided by the same standardiser. Each such choice is recorded in `selected-effects.csv`.
- Before-after studies are pooled apart from controlled studies, as the protocol requires. The all studies pool is a sensitivity check and is labelled as such.
- Binary burnout outcomes are converted to SMD by the Cox transformation (log odds ratio times sqrt(3) over pi) and are pooled only in a sensitivity set, apart from the continuous scales.
- Error proportions are pooled on the logit scale. Type specific proportions are not pooled across studies, because only one study reports each type against a notes denominator (see below).
- Funnel plot and Egger test only where k is 10 or more.
- Analysis units differ across studies (clinicians, encounters, appointments, notes, paired periods). Totals below are sums of the analysis units each study analysed, not counts of unique patients.

## 1. Documentation time

### 1a. Standardised mean difference (primary metric)

| Pool | k | Analysis units | SMD | 95% CI | 95% prediction interval | I squared | Tau squared | p |
|---|---|---|---|---|---|---|---|---|
| Controlled studies | 6 | 11,108 | -0.52 | -0.88 to -0.15 | -1.49 to 0.46 | 88.2% | 0.102 | 0.015 |
| Uncontrolled before-after | 7 | 1,792 | -0.31 | -0.43 to -0.19 | -0.61 to -0.02 | 64.2% | 0.011 | <0.001 |
| All studies (sensitivity) | 13 | 12,900 | -0.38 | -0.53 to -0.24 | -0.84 to 0.07 | 83.4% | 0.039 | <0.001 |
| Excluding serious or critical risk of bias | 3 | 978 | -0.37 | -1.22 to 0.49 | -5.30 to 4.56 | 93.6% | 0.111 | 0.20 |
| Journal articles only (preprints removed) | 12 | 12,840 | -0.40 | -0.56 to -0.24 | -0.89 to 0.09 | 84.4% | 0.044 | <0.001 |

Controlled pool studies: Wright 2026 (R0023), Kashiouris 2026 (R0043), Grand 2026 (R0068), Prasser 2026 (R0102), Philips 2026 (R0123), Etagiuri 2026 (R0181). Before-after pool: Harvey 2026 (R0111), Olson 2025 (R0127), Tan 2026 (R0186), van Linschoten 2026 (R0206), North 2025 (R0270), Stults 2025 (R0346), Duggan 2025 (R0360).

Reading: the average effect is a reduction of about 0.4 SD in documentation time. Heterogeneity is high in every pool. The prediction interval for the all studies pool runs from -0.84 to 0.07, so a new setting could see no reduction. The sensitivity pool that drops serious and critical risk of bias studies keeps only Kashiouris 2026, Etagiuri 2026 and van Linschoten 2026, and its interval runs from -1.22 to 0.49. The estimate rests on studies at serious risk of bias.

### 1b. Relative change in documentation time (supplementary metric, percent)

Many studies report time as a percentage change. These 15 studies were pooled on the percentage scale as a secondary synthesis. It answers a different question from the SMD pool and the two should not be averaged together.

| Pool | k | Analysis units | Change | 95% CI | 95% prediction interval | I squared | Tau squared | p |
|---|---|---|---|---|---|---|---|---|
| All studies | 15 | 14,742 | -18.9% | -25.9% to -11.9% | -43.4% to 5.5% | 88.4% | 118.8 | <0.001 |
| Controlled studies | 9 | 13,485 | -21.8% | -34.5% to -9.2% | -59.8% to 16.1% | 92.5% | 229.4 | 0.004 |
| Uncontrolled before-after | 6 | 1,257 | -14.3% | -18.0% to -10.7% | -18.9% to -9.8% | 0.0% | 0.44 | <0.001 |
| Excluding serious or critical risk of bias | 4 | 1,205 | -9.2% | -22.1% to 3.7% | -45.5% to 27.2% | 83.9% | 55.0 | 0.11 |

### 1c. Subgroups, documentation time SMD

By design. Randomised (k 1, Etagiuri 2026): SMD -0.58 (95% CI -0.81 to -0.34). Non-randomised controlled (k 5): SMD -0.52 (95% CI -1.00 to -0.03), I squared 90.0%. Before-after (k 7): SMD -0.31 (95% CI -0.43 to -0.19), I squared 64.2%. Interaction test (Wald omnibus on the subgroup pooled estimates): chi squared 4.88, df 2, p 0.087. The design gradient is visible but the interaction test does not confirm it at the 5% level.

By product. Abridge (k 7): SMD -0.36 (95% CI -0.65 to -0.07), I squared 80.0%. DAX family (k 3): SMD -0.37 (95% CI -0.87 to 0.13), I squared 89.2%. Other or mixed products (k 3): SMD -0.52 (95% CI -0.83 to -0.20), I squared 22.8%. Interaction: chi squared 1.89, df 2, p 0.39. No product subgroup difference is supported.

By vendor involvement. Vendor linked studies (k 3): SMD -0.28 (95% CI -0.61 to 0.06), I squared 42.4%. Independent studies (k 9): SMD -0.43 (95% CI -0.60 to -0.27), I squared 79.3%. One study (Kashiouris 2026) had unclear vendor involvement and is left out of this comparison. Interaction: z 1.47, p 0.14. No vendor subgroup difference is supported. The point estimates run against the direction a sponsorship story would predict, and the test does not confirm any difference either way.

Leave one product out (all studies SMD pool). Leaving out Abridge: SMD -0.43 (95% CI -0.61 to -0.25), k 6, I squared 80.8%. Leaving out the DAX family: SMD -0.39 (95% CI -0.58 to -0.20), k 10, I squared 81.4%. Leaving out other products: SMD -0.36 (95% CI -0.55 to -0.17), k 10, I squared 85.1%. The direction does not depend on any one product family.

### 1d. Reporting bias, documentation time

Funnel plot: `funnel-time-smd.png`. Egger test on the SMD pool (k 13): intercept -0.71, t -0.59, p 0.56. Egger test on the relative change pool (k 15): intercept -0.11, t -0.06, p 0.95. Neither test shows funnel plot asymmetry. Both tests have low power at this k and sit on top of high heterogeneity, so they rule out little.

### 1e. Time outcomes not pooled, and why

- Husa 2026 (R0134): interrupted time series level and slope changes with no outcome SD and no analysis n in the extracted rows. Reported levels: time in notes per day fell from 50.7 to 41.6 minutes at implementation.
- Rotenstein 2026 (R0183): direct differences in minutes per 8 scheduled hours (16.0 fewer minutes in notes) with CIs but no scale SD, so no SMD. Included in the study count for the outcome, narrative only.
- Afshar 2025 (R0235): documentation time difference of -0.36 hours per day with a CI but no SD in the extracted rows. Narrative only for time; the study is pooled for burnout, where a baseline SD was extracted.
- Wright 2025 (R0324): median paired differences with no SD. Narrative only for time; pooled for workload from raw NASA-TLX means.
- Survey proportions (for example R0105, R0205): shares of users agreeing that the tool saves time. These are attitudes data, not time measurements, and were not pooled with measured time.
- Encounter level time stamps and note counts (for example counts of notes closed the same day) use unlike denominators and are summarised in the manuscript text, not pooled.

## 2. After-hours documentation time

All six poolable studies are uncontrolled before-after studies. No controlled study reported an after-hours effect that could be standardised, so the controlled only sensitivity analysis has k 0. Excluding serious or critical risk of bias studies also leaves k 0, because all six studies are at serious risk of bias for this outcome.

| Pool | k | Analysis units | SMD | 95% CI | 95% prediction interval | I squared | Tau squared | p |
|---|---|---|---|---|---|---|---|---|
| Uncontrolled before-after (all poolable) | 6 | 1,003 | -0.25 | -0.52 to 0.01 | -0.85 to 0.34 | 71.8% | 0.037 | 0.058 |
| Abridge studies only | 4 | 858 | -0.26 | -0.74 to 0.23 | not reported for a product subset (see note) | 79.6% | 0.063 | 0.19 |

Studies: Harvey 2026 (R0111), Olson 2025 (R0127), Olson 2025 (R0295), Stults 2025 (R0346), Duggan 2025 (R0360), Pollak 2026 (R0392). Stults 2025 runs in the opposite direction on raw off-hour EHR minutes (39.8 post vs 38.2 pre) while its adjusted model estimate is -0.9 minutes; the raw values were used, which is one source of the heterogeneity.

By vendor involvement: vendor linked (k 2) SMD -0.17 (95% CI -0.52 to 0.19), I squared 79.9%; independent (k 4) SMD -0.33 (95% CI -0.80 to 0.14), I squared 73.2%. Interaction: z 0.68, p 0.50. No difference supported. A product subgroup beyond Abridge is not possible: the remaining studies use DAX (k 1) and unnamed products (k 1).

Not pooled: Prasser 2026 (R0102) reported an adjusted after-shift effect of +9.1 seconds with medians of 0 in both arms; a standardised effect from zero medians would mislead, so it is described in text. Moura 2026 (R0059) compares one scribe product against another, not a scribe against no scribe.

Note on the Abridge subset row: the script computed a prediction interval for this subset; it is not quoted here because a four study product subset is too small for a prediction interval to guide decisions. The full value is in `analysis-results.json`.

## 3. Burnout and work exhaustion

### 3a. Continuous scales, SMD

| Pool | k | Analysis units | SMD | 95% CI | 95% prediction interval | I squared | Tau squared | p |
|---|---|---|---|---|---|---|---|---|
| Controlled trials (both randomised designs) | 2 | 257 | -0.44 | -0.61 to -0.28 | not estimable at k 2 | 0.0% | 0.000 | <0.001 |
| Uncontrolled before-after | 2 | 425 | -0.23 | -0.35 to -0.12 | not estimable at k 2 | 0.0% | 0.000 | <0.001 |
| All studies | 4 | 682 | -0.34 | -0.53 to -0.15 | -0.87 to 0.19 | 34.0% | 0.010 | 0.011 |
| Journal articles only | 3 | 629 | -0.34 | -0.67 to -0.02 | -2.07 to 1.39 | 55.7% | 0.012 | 0.045 |

Studies: Afshar 2025 (R0235, stepped wedge), Lukac 2025 (R0257, randomised, two product arms combined into one study effect with a shared control allowance), Olson 2025 (R0295, before-after), Pollak 2026 (R0392, before-after, preprint). Excluding serious or critical risk of bias studies leaves the two trials, so that sensitivity pool equals the controlled pool: SMD -0.44 (95% CI -0.61 to -0.28).

Design interaction (randomised vs before-after, on the subgroup pooled estimates): z -2.07, p 0.038. With two studies per subgroup this is a weak test. It is reported because the protocol pre-specified the design subgroup, and it should be read as a signal to check in later trials, not as a settled finding.

### 3b. Same instrument mean difference (PFI work exhaustion composite)

Afshar 2025 and Lukac 2025 both report the Professional Fulfillment Index work exhaustion composite. Pooled mean difference: -0.36 points (95% CI -0.52 to -0.20), k 2, analysis units 257, I squared 27.3%, tau squared 0.004, p <0.001. The composite runs 0 to 4 in Lukac 2025 (item means) and 1 to 5 per item in Afshar 2025; the difference metric is on the same 4 point span in both. A prediction interval is not estimable at k 2.

### 3c. Sensitivity set: binary burnout measures converted to SMD

Five further studies report burnout only as a proportion over a threshold (Harvey 2026, Olson 2025 pharmacists, You 2025, Stults 2025, Misurac 2024). Converted by the Cox transformation and pooled on their own: SMD -0.39 (95% CI -0.61 to -0.16), k 5, analysis units 786, I squared 0.0%, tau squared 0.006, prediction interval -0.77 to -0.002, p 0.009. Pooled together with the four continuous studies: SMD -0.35 (95% CI -0.46 to -0.25), k 9, analysis units 1,468, I squared 14.4%, tau squared 0.008, prediction interval -0.60 to -0.11, p <0.001. The binary and continuous routes agree in direction and roughly in size. Single item measures sit inside the binary set (Harvey 2026, Olson 2025 pharmacists, Stults 2025); removing them leaves You 2025 and Misurac 2024, both PFI threshold studies, and the manuscript reports the set with and without them in text rather than as a further pool.

### 3d. Professional fulfilment

Not pooled. Two studies report it on unlike metrics: Afshar 2025 gives a model difference of +0.14 points (95% CI 0.004 to 0.28) on the PFI fulfilment composite in the scribe period; You 2025 gives proportions meeting a fulfilment threshold at two time points (37.5% pre vs 36.5% at 42 days and 41.7% at 84 days). One mean difference and one threshold proportion do not form a pool. Narrative range: no clear change in fulfilment alongside the fall in work exhaustion.

## 4. Workload and task load

| Pool | k | Analysis units | SMD | 95% CI | 95% prediction interval | I squared | Tau squared | p |
|---|---|---|---|---|---|---|---|---|
| All studies | 7 | 975 | -1.46 | -2.13 to -0.78 | -3.31 to 0.40 | 90.8% | 0.444 | 0.002 |
| Controlled studies | 3 | 241 | -1.50 | -4.42 to 1.43 | -18.51 to 15.51 | 92.1% | 1.291 | 0.16 |
| Uncontrolled before-after | 4 | 734 | -1.49 | -2.14 to -0.83 | -3.14 to 0.17 | 69.9% | 0.110 | 0.006 |
| Excluding serious or critical risk of bias | 1 | 191 | -0.39 | -0.70 to -0.09 | not estimable at k 1 | n/a | n/a | 0.012 |

Studies: Kashiouris 2026 (R0043), Grand 2026 (R0068), Olson 2025 (R0127), Lukac 2025 (R0257), Olson 2025 (R0295), Wright 2025 (R0324), Stults 2025 (R0346, mental demand item, no total score printed).

Reading: this is the least trustworthy pool in the review. The large average effect is carried by small uncontrolled survey studies with very large standardised effects (Kashiouris 2026, g -2.66; Olson 2025 pharmacists, d -1.90; Olson 2025, SMD -1.60). The one study that survives the risk of bias filter is the randomised trial, Lukac 2025, at SMD -0.39. The design subgroup test is formally significant (chi squared 26.3, df 2, p <0.001), but the subgroups hold 1, 2 and 4 studies, so it is reported as descriptive. The honest summary is that task load falls, by an amount the current studies cannot pin down, with the best controlled estimate near -0.4 SD.

By vendor involvement: vendor linked (k 2) SMD -1.60 (95% CI -1.74 to -1.45), I squared 0.0%; independent (k 3) SMD -1.23 (95% CI -3.34 to 0.88), I squared 90.7%; two studies had unclear vendor involvement. Interaction: z -0.74, p 0.46. No difference supported.

## 5. Note quality

| Pool | k | Analysis units | SMD | 95% CI | 95% prediction interval | I squared | Tau squared | p |
|---|---|---|---|---|---|---|---|---|
| All studies | 6 | 1,193 | 0.57 | 0.51 to 0.64 | 0.45 to 0.70 | 0.0% | 0.000 | <0.001 |
| PDQI family only | 3 | 802 | 0.55 | 0.49 to 0.61 | -0.09 to 1.19 | 0.0% | 0.000 | <0.001 |
| Excluding serious or critical risk of bias | 3 | 1,065 | 0.57 | 0.41 to 0.73 | -0.02 to 1.16 | 0.0% | 0.000 | 0.004 |
| Journal articles only | 4 | 407 | 0.65 | 0.58 to 0.72 | 0.22 to 1.08 | 0.0% | 0.000 | <0.001 |

Studies: Philips 2026 (R0123), Gladysz 2026 (R0128), Etagiuri 2026 (R0181), Foo 2025 (R0277), Nawaz 2025 (R0385), Bergman 2026 (R0408).

Reading: the direction is consistent and the statistical heterogeneity is zero, which is unusual in this review and should not be over-read. Bergman 2026, a preprint with 385 paired consultations, carries 78.7% of the weight in the all studies pool because its printed CI is narrow. Gladysz 2026 is at critical risk of bias: its PDQI-9 scores were produced by LLM raters whose agreement statistic was negative, and the source paper itself warns the scores cannot be read as reliable quality evidence. Removing it changes the pooled estimate little because its weight is small, but the pool without it is the cleaner one to quote. Quality here means scores on structured rating instruments, several of them applied to simulated or standardised encounters. It does not mean the notes were more accurate; accuracy is the errors outcome, below.

By vendor involvement: vendor linked (k 2) SMD 0.56 (95% CI 0.46 to 0.65); independent (k 3) SMD 0.65 (95% CI 0.55 to 0.75); one study unclear. Interaction: z -1.65, p 0.099. No difference supported. A design subgroup was not run for quality: the six studies are two trials, two note audits, one controlled before-after and one paired workflow comparison, which do not fill the protocol design classes in poolable numbers.

Not pooled for quality: Zuckerman 2026 (R0414) compares a consolidated documentation pipeline against ambient only documentation, which is a comparison of two scribe workflows, not scribe against usual documentation. Verma 2026 (R0098) compares two versions of one model. Taylor 2026 (R0170) reports a median overall quality score with no variance. These are described in the manuscript text.

## 6. Note errors

### 6a. Type specific proportions: not pooled across studies

Only Taylor 2026 (R0170) reports type specific error proportions against a notes denominator (356 AI generated notes checked against the consultation record). With one study per type, there is nothing to pool. Study level proportions with Wilson 95% CIs, all produced by the script:

| Study and type | Events / denominator | Proportion | 95% CI |
|---|---|---|---|
| Taylor 2026, omissions | 64 / 356 notes | 18.0% | 14.3% to 22.3% |
| Taylor 2026, hallucinations | 41 / 356 notes | 11.5% | 8.6% to 15.3% |
| Taylor 2026, wrong inclusions | 33 / 356 notes | 9.3% | 6.7% to 12.7% |
| Taylor 2026, errors rated severity 4 to 5 | 19 / 356 notes | 5.3% | 3.4% to 8.2% |
| Bergman 2026, at least one Critical+High error, clinician adjudication | 24 / 385 notes | 6.2% | 4.2% to 9.1% |
| Bergman 2026, at least one Critical+High error, calibrated automated reviewer | 94 / 385 notes | 24.4% | 20.4% to 28.9% |
| Menz 2026, omission errors | 10 / 2,160 data points | 0.5% | 0.3% to 0.9% |
| Menz 2026, incorrect data points, all types | 46 / 2,160 data points | 2.1% | 1.6% to 2.8% |

The Bergman 2026 pair of rows is the measurement warning for this whole outcome: the same notes give 6.2% under clinician adjudication and 24.4% under a calibrated automated reviewer. Error rates in this literature are a property of the detection method as much as of the notes.

### 6b. Any error proportion: two study sensitivity pool

Two studies report the share of notes with at least one error, under different definitions: Biro 2025 (R0363), 31 of 44 draft notes with at least one error (70.5%, 95% CI 55.8% to 81.8%), mean 2.9 errors per note; De John 2026 (R0395), 24 of 49 notes with at least one clinically meaningful error (49.0%, 95% CI 35.6% to 62.5%), derived from the 25 notes the study reports as free of clinically meaningful errors. Pooled on the logit scale: 59.8% (95% CI 37.9% to 78.4%), k 2, 93 notes, I squared 76.9%, tau squared 0.32 on the logit scale, p 0.38. A prediction interval is not estimable at k 2. This pool mixes two definitions of an error and two note sets of under 50 notes each. It is reported so the number exists with its uncertainty attached; the summary of findings grades it very low and the manuscript does not use it as a headline. Excluding serious or critical risk of bias studies leaves k 0 (both studies are serious for this outcome), and removing the preprint leaves Biro 2025 alone at 70.5%.

### 6c. Error data not pooled, and why

- Error counts per note (Biro 2025 mean 2.9 per note; Bauer 2026 (R0435) medians of 5 omissions per AI note vs 8 per comparator note; De John 2026, 21 hallucinations across 49 notes) are counts, not proportions of notes, and are not mixed with the proportion pool.
- Verma 2026 (R0098) reports errors as shares of clinical elements and compares two model versions (omissions 21.60% for M1 vs 9.32% for M6). Unlike denominator, wrong comparison for this review question.
- Rabotin 2026 (R0076) measures propagation of planted interpreter errors (55% and 60% of planted errors reaching the final note in two arms). The denominator is planted errors, not notes.
- Etagiuri 2026 (R0181) reports total medical error counts per arm (19 vs 9 across letters), not notes with at least one error.
- Blease 2026 (R0029) reports the share of surveyed GPs who say they often or always spot errors (45 of 141, 31.9%). The denominator is clinicians, not notes.

## 7. Outcomes and families not pooled at all

- Patient experience: four study by outcome rows across the extraction set, on unlike instruments, with serious or high risk of bias in three of four. Narrative only.
- Note length, time to note closure, documentation volume: reported by a handful of studies on unlike metrics (words, characters, minutes to closure, notes per day). Narrative only.
- Professional fulfilment: see 3d.
- Cost and revenue outcomes: outside the protocol outcomes.
- Subgroups by specialty, clinician type and follow-up duration: the selected effects do not carry poolable numbers in these strata (most time studies are primary care, follow-up is rarely stated in the analysis rows), so no subgroup claim is made for them. The protocol asked for an interaction test or a plain statement that k was too small; this is that statement.

## 8. Reproducibility

Run `python3 meta_analysis.py` in this folder. It reads `extraction.csv`, `rob-assessments.csv` and its own encoded selected effects, writes `selected-effects.csv`, `analysis-results.json`, seven forest plots and one funnel plot, and prints the pooled estimates. The encoded effects and their derivations are listed in full in `selected-effects.csv`; any reader can check each one against the study report.
