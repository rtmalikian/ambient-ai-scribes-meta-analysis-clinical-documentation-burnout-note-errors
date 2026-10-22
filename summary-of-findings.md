# Summary of findings: ambient AI scribes for clinical documentation

Review: Ambient artificial intelligence scribes for clinical documentation: effects on documentation time, after-hours work, clinician burnout, note quality and note errors. A systematic review and meta-analysis. Malikian R, 2026.

Population: clinicians using electronic health records (mostly physicians in primary care and outpatient specialties; also pharmacists, surgeons, nurses and mixed clinician samples). Intervention: ambient AI scribe (microphone capture of the consultation, AI generated draft note for clinician review and sign-off). Comparison: usual documentation (typing, dictation, human scribe, or pre-implementation period). Setting: mostly US health systems, 2024 to 2026. Follow-up: mostly 30 to 90 days.

All pooled estimates are from `stage5/meta_analysis.py` (REML random effects, Hartung-Knapp intervals where k is 3 or more). Analysis units differ by study (clinicians, encounters, appointments, notes, paired periods); the counts below are the units each study analysed, summed.

| Outcome | Effect (pooled) | Studies (analysis units) | Certainty (GRADE) | Plain reading |
|---|---|---|---|---|
| Documentation time | SMD -0.38 (95% CI -0.53 to -0.24) across all studies; controlled studies SMD -0.52 (-0.88 to -0.15); before-after studies SMD -0.31 (-0.43 to -0.19). On the percentage scale, -18.9% (-25.9% to -11.9%) | 13 studies for SMD (12,900 units); 15 for the percentage pool | LOW | Documentation time falls by roughly a fifth on average. The spread across settings is wide, and a new setting could see little or no gain. |
| After-hours documentation time | SMD -0.25 (95% CI -0.52 to 0.01), before-after studies only | 6 studies (1,003 units) | VERY LOW | The average points to less after-hours work. The interval includes no effect, one large study runs the other way on raw minutes, and no controlled estimate exists. |
| Burnout and work exhaustion | SMD -0.34 (95% CI -0.53 to -0.15) across four studies; the two randomised trials pool at SMD -0.44 (-0.61 to -0.28), equal to -0.36 points (-0.52 to -0.20) on the PFI work exhaustion composite | 4 studies (682 units); trials 257 clinicians | MODERATE for the trial estimate; LOW for the all studies estimate | Work exhaustion scores fall by about a third of a standard deviation over 30 to 90 days. Whether the gain lasts past a few months is untested. |
| Workload and task load | SMD -1.46 (95% CI -2.13 to -0.78) across all studies; the one study at lower risk of bias (the randomised trial) gives SMD -0.39 (-0.70 to -0.09) | 7 studies (975 units) | VERY LOW | Clinicians report lower task load. The size is not pinned down: small uncontrolled surveys give very large effects, the trial gives a moderate one. |
| Note quality (structured rating instruments) | SMD 0.57 (95% CI 0.51 to 0.64); PDQI family only, SMD 0.55 (0.49 to 0.61) | 6 studies (1,193 units) | LOW | Notes score higher on rating instruments. Higher scores are not the same as fewer errors, and several audits used simulated encounters. |
| Notes with at least one error | 59.8% (95% CI 37.9% to 78.4%) of AI drafted notes had at least one error, two studies with different error definitions; type specific rates come from one study: omissions 18.0% of notes, hallucinations 11.5%, wrong inclusions 9.3% | 2 studies (93 notes) for the pool; 1 study (356 notes) for type specific rates | VERY LOW | Errors in AI drafts are common enough that review before sign-off carries real weight. The exact rate depends on how errors are defined and detected. |
| Professional fulfilment | Not pooled. One trial reports +0.14 points (95% CI 0.004 to 0.28) on the PFI fulfilment composite; one before-after study reports threshold proportions of 37.5% before, 36.5% at 42 days and 41.7% at 84 days | 2 studies | VERY LOW | No clear change in fulfilment alongside the fall in work exhaustion. |

## GRADE judgements, outcome by outcome

### Documentation time: LOW

- Risk of bias, downgrade 1. Eleven of the 13 studies in the SMD pool are at serious risk of bias for the time outcome (self-selected users, no concurrent control, high user subgroups analysed as if assigned). The sensitivity pool without serious or critical studies holds three studies and its interval runs from -1.22 to 0.49, so the headline estimate depends on the biased studies.
- Inconsistency, downgrade 1. I squared 83.4% in the all studies pool and 88.2% in the controlled pool. The prediction interval (-0.84 to 0.07) crosses no effect.
- Indirectness, no downgrade. Time in notes is the outcome services care about, measured from EHR logs in most studies.
- Imprecision, no downgrade. Both design specific intervals exclude no effect.
- Publication bias, no downgrade. Egger test p 0.56 (SMD pool) and p 0.95 (percentage pool). Power is low and the test is reported, not leaned on.

### After-hours documentation time: VERY LOW

- Risk of bias, downgrade 1. All six poolable studies are uncontrolled before-after studies at serious risk of bias for this outcome. The controlled only and the lower risk of bias sensitivity pools are both empty (k 0).
- Inconsistency, downgrade 1. I squared 71.8%, and the largest study's raw off-hour minutes move in the opposite direction to its adjusted model estimate.
- Imprecision, downgrade 1. The interval runs from -0.52 to 0.01 and includes no effect.
- Indirectness, no downgrade. EHR log measures of out of hours work are direct for the question, though they count EHR activity, not all work.

### Burnout and work exhaustion: MODERATE (trial estimate), LOW (all studies)

- Risk of bias, no downgrade for the trial estimate; downgrade 1 for the all studies estimate. Both trials sit at some concerns (unblinded, self-reported outcome, volunteer samples, survey response under 100%). The validated instruments and balanced response rates keep this short of serious for the trials. The two before-after studies are at serious risk of bias (responder samples of users), which is why the all studies estimate is rated lower. Excluding serious studies leaves the trial pool unchanged.
- Indirectness, downgrade 1. Follow-up is 30 to 90 days in the trials. Burnout moves slowly, and a short window after a tool launch mixes novelty, relief at any help with documentation, and any lasting change. The outcome that matters, sustained burnout reduction, is not what was measured.
- Inconsistency, no downgrade. I squared 0.0% across the two trials and 34.0% across all four studies. A binary measure sensitivity set (five studies, threshold proportions converted to SMD) pools at -0.39 and agrees with the continuous estimate.
- Imprecision, no downgrade. The trial interval (-0.61 to -0.28) excludes no effect and is narrow enough to separate a small from a moderate effect.

### Workload and task load: VERY LOW

- Risk of bias, downgrade 1. Six of seven studies are at serious risk of bias for this outcome. Only the randomised trial survives the filter, at SMD -0.39.
- Inconsistency, downgrade 1. I squared 90.8%. Study effects run from -0.39 to -2.66.
- Indirectness, downgrade 1. The pool mixes NASA-TLX totals, a three item documentation burden composite, a note related cognitive load composite and one single item (mental demand). One study's units are five clinic days from a single surgeon. These are related but different constructs.
- Imprecision, no further downgrade. The all studies interval excludes no effect; the problem is bias and spread, not width alone.

### Note quality: LOW

- Risk of bias, downgrade 1. One study is at critical risk of bias (LLM raters with a negative agreement statistic scoring the notes). Graders were unblinded or were the notes' own authors in several audits. The study carrying 78.7% of the weight is a preprint.
- Indirectness, downgrade 1. Ratings come from structured instruments (PDQI-9 family, SAIL, study specific scores) and several audits used simulated or actor performed consultations. A higher rating does not show the note is more accurate.
- Inconsistency, no downgrade. I squared 0.0% in every quality pool. This is noted, not rewarded: with one dominant study, the statistic has little room to move.
- Imprecision, no downgrade. Intervals are narrow, though they lean on the dominant preprint.

### Notes with at least one error: VERY LOW

- Risk of bias, downgrade 1. Both pooled studies are at serious risk of bias for the errors outcome (convenience sets of notes, graders who knew the notes were AI drafts).
- Inconsistency, downgrade 1. I squared 76.9% on the logit scale, and the two studies define an error differently (any error vs clinically meaningful error).
- Imprecision, downgrade 1. 93 notes in total. The interval runs from 37.9% to 78.4%.
- Indirectness, no separate downgrade. The definition problem is counted under inconsistency. The type specific rates (Taylor 2026) come from one study and are reported as study level data, not as a pooled effect.

### Professional fulfilment: VERY LOW

- Not pooled: two studies, two metrics (a mean difference on the PFI composite; proportions over a threshold). One is a trial at some concerns, one a before-after study at serious risk of bias. Small samples, short follow-up, and no shared metric. The certainty is very low and the direction is unclear.

## What would raise these ratings

- A controlled study of after-hours work, which does not exist yet in poolable form.
- Burnout follow-up at 6 to 12 months in a randomised design with response rates reported by arm.
- Error audits that prespecify error types, use a notes denominator, blind the graders, and publish the detection method alongside the rate, since the detection method moved one study's severe error rate from 6.2% to 24.4% on the same notes.
- Time studies that report an SD or a model SE on a stated scale, which would have let at least four more controlled studies into the SMD pool.
