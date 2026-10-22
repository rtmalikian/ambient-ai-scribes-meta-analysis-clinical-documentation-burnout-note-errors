# Data extraction form, piloted version 1

For use by extractor A and extractor B, working apart, on every study that passes full text screening. One form per study. Both sheets are compared field by field. Each mismatch is logged in llm-team-log.md with the field name, settled against the source document, and counted in the extraction discrepancy rate. The human author checks every number that will enter a pool.

Pilot note: the form was drafted from protocol section 4 outcomes and section 8 bias concerns before screening began. It gets its first live test on the first five included studies. Any field change after that test is logged here with a date, and forms already filled are rechecked on the changed field.

## A. Study identity
1. Record ID from screening.csv.
2. First author, year, journal or source.
3. DOI or PMID.
4. Country and health system, as stated.
5. Registration number, if any, and registry.
6. Report type: journal article, preprint, trial results report.

## B. Design and setting
7. Study design, in the study words first, then the review class: randomised, stepped wedge, non-randomised controlled, controlled before and after, uncontrolled before and after, interrupted time series, note audit.
8. Setting: outpatient, inpatient, emergency, virtual, mixed. Specialty or specialties.
9. Study dates and follow-up length in days. Follow-up group for analysis: under 90 days, or 90 days or more.
10. How clinicians entered the study: volunteered, assigned, whole service switched. This field feeds the self-selection judgement in ROBINS-I.
11. Concurrent changes in the study period: record system changes, template changes, documentation training, staffing changes. Stated as none, stated in words, or not mentioned.

## C. Participants
12. Clinician count, by type: physicians, advanced practice clinicians, other.
13. Encounter count and note count, with the period each covers.
14. Baseline documentation load, if reported, with its measure.

## D. Intervention
15. Product name and version, as stated. If no version is stated, write not stated.
16. What the tool captures: whole encounter audio, part encounter, other. Consent model for patients and clinicians, as stated.
17. What the clinician does with the draft: review and edit route, sign route, average edit time if reported.
18. Training or support given with the tool.

## E. Comparator
19. Comparator in words: usual documentation, typing, dictation, speech recognition, human scribe, pre-implementation period.
20. Comparator size and period, where a group or period applies.

## F. Outcomes, one block per outcome reported
For each outcome the study reports, copy the block. No block, no pool entry.
21. Outcome name from protocol section 4: documentation time, after-hours time, burnout or work exhaustion, professional fulfillment, note quality, note errors (type split below), time to note closure, patient experience, note length.
22. Measure in the study words: instrument or audit log field, scale range and direction where a scale applies.
23. Time point, in days from implementation where it can be set.
24. Value for the scribe group and the comparator or pre period: mean and standard deviation, or median and spread, or count and denominator, exactly as printed. Page or table the value came from.
25. Adjusted or unadjusted, and the variables in the adjustment, where the study gives them.
26. Missing data on this outcome, as stated.

## G. Note errors, audit block
27. Notes audited, count, and how they were picked.
28. Reference the notes were graded against: encounter audio, encounter record, human note, other.
29. Grader: who graded, their role, and whether they knew which tool wrote the note.
30. Omissions: notes with at least one omission, and total omission count, as printed.
31. Hallucinations or fabrications: notes with at least one, and total count, as printed. Keep apart from omissions in every field.
32. Wrong inclusions: notes with at least one, and total count, as printed.
33. Harm or severity grading, where the study gives one, in the study words.

## H. Funding and vendor role
34. Funding source in words.
35. Vendor role: design, data handling, analysis, writing, none stated, none.
36. Author conflicts as stated in the paper.
37. Review class for subgroup work: vendor funded or vendor staffed, against independent. Set from fields 34 to 36, with the line that decided it quoted.

## I. Extractor notes
38. Anything in the paper that does not fit a field above and bears on eligibility, bias or an outcome.
39. Data the paper should have and does not give, by field number, for the author contact list.
