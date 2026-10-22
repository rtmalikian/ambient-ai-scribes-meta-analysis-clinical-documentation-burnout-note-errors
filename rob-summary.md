# Risk of bias summary, Stage 4a

All 74 included studies were assessed. Assessments sit in rob-assessments.csv: 138 study by outcome-group rows, each with Pass A, an independent Pass B, and an adjudicated judgement per domain, plus a support line for every domain. RoB 2 was used for randomised designs (17 rows, 7 studies: 6 RCTs and the stepped wedge trial, judged with RoB 2 as a randomised design). ROBINS-I was used for everything else (121 rows, 67 studies). Outcome groups: time, burnout (burnout, professional fulfillment and workload grouped), errors, quality, and patient experience where a study reported it apart.

## Adjudicated overall judgements, all 138 rows

- Serious (ROBINS-I): 94 rows
- Moderate (ROBINS-I): 24 rows
- Critical (ROBINS-I): 3 rows
- Some concerns (RoB 2): 11 rows
- High (RoB 2): 5 rows
- Low (RoB 2): 1 row

## By outcome group (adjudicated overall)

- Time, 44 rows: serious 33, moderate 5, some concerns 3, low 1, high 1, critical 1. The single low row is the stepped wedge trial (Afshar, R0235) on audit log time.
- Burnout, 29 rows: serious 23, some concerns 4, high 1, critical 1.
- Errors, 22 rows: serious 10, moderate 9, high 2, some concerns 1.
- Quality, 39 rows: serious 25, moderate 10, some concerns 3, critical 1.
- Patient experience, 4 rows: serious 3, high 1.

## Per study, worst adjudicated judgement across its outcome groups

- Serious: 55 studies
- Moderate: 10 studies
- High: 5 studies
- Critical: 2 studies
- Some concerns: 2 studies
- Low: 0 studies (no study was low across every group it reported)

## By design (per study, worst judgement)

- Uncontrolled before-after, 25 studies: serious 23, moderate 1, critical 1
- Note audit, 20 studies: serious 13, moderate 7
- Non-randomised controlled, 12 studies: serious 10, moderate 2
- RCT, 6 studies: high 5, some concerns 1 (worst per study; the high ratings sit in the errors, burnout or patient experience groups of trials whose time outcomes rated some concerns)
- Cross-sectional, 5 studies: serious 5
- Controlled before-after, 2 studies: serious 2
- Other designs, 2 studies: critical 1, serious 1
- Interrupted time series, 1 study: serious 1
- Stepped wedge, 1 study: some concerns (worst group; its time group rated low)

## What drove the judgements

- Confounding and self-selection (ROBINS-I D1 and D2) carry most of the serious ratings in the before-after literature: volunteer early adopters, high-user subgroups analysed as if assigned, and no concurrent control. The protocol confounders set in advance (baseline documentation load, specialty mix, concurrent record system changes, self-selection of keen users) were left open in most of these studies.
- Measurement (D6 in ROBINS-I, D4 in RoB 2) is the split that matters most for errors and quality: audits graded by the notes' own authors, unblinded, or graded against the tool's own transcript rate serious; audits with a human-validated reference transcript and blinded raters rate moderate. Of the 22 error rows, 9 reached moderate, the highest share of any group.
- The three critical rows belong to two studies: R0548 (time and burnout rows; survey restricted to fully onboarded sustained users, discontinuers excluded by design, D2 critical) and R0128 (quality row; LLM scoring of PDQI-9 with a negative inter-rater agreement statistic and no human ground truth, D6 critical).

## Pass mechanics

Pass A and Pass B disagreed on 185 domain judgements across the 138 rows (counted field by field from rob-assessments.csv). 121 of 138 rows had at least one domain disagreement. The commonest split was moderate against serious (103 of the 185). Pass A and Pass B overall judgements differed in 32 rows. Adjudication changed the overall judgement away from Pass A in 8 rows and away from Pass B in 24 rows. Domain disagreement counts: D6 measurement 44, D5 missing data 39, D4 deviations 24, D2 selection 26, D7 reported result 21, D1 confounding or randomisation 18, D3 classification or missing outcome data 13.
