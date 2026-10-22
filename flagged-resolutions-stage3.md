# Flagged records, Stage 3 resolutions

The 21 records flagged at Stage 2 (flagged-for-author-v2.md), resolved at the full text stage on 22 October 2026. Basis stated per record: full text where a text was retrieved, abstract detail where it was not.

Count check: 21 = 5 included on full text + 1 excluded on full text + 1 pair partner (same study) + 4 not retrieved + 10 Stage 2 excludes confirmed.

## Included on full text (5)

- **R0098**. Simulated ICU round transcripts, but the graded unit is the generated progress note: accuracy error percentages and PDQI-9 scores on a defined set of generated notes. Passes the note audit test in protocol section 3.2. Include, flagged in extraction as a standardised simulated audit and algorithm development study.
- **R0123**. Real multidisciplinary tumor boards, not patient encounters. Reports documentation quality scores and administrative time per case for ambient AI against manual documentation of the same meetings (author manuscript retrieved). Include. Extraction flags the setting as non-encounter clinical documentation.
- **R0173**. Benchmark of transcripts with planted third party personal information; the outcome counted is inappropriate inclusion of that information in the generated note. That is a wrong inclusion under protocol section 4.1, with transcripts as the denominator. Include for the note errors question.
- **R0256**. The abstract called the study qualitative. The full text reports adapted PDQI-9 means and standard deviations per specialty in its results tables, alongside focus groups. Quantitative note quality data are extractable. Include on the PDQI-9 data; the denominator question from Stage 2 is settled by the results tables.
- **R0363**. Research letter with the audit in full: 2 reviewers graded each note, errors categorised as omission, addition, wrong output, or irrelevant or misplaced text, 127 errors in total. Include. See the pair resolution below.

## Excluded on full text (1)

- **R0003**. Interview study of patients whose clinicians took part in a pragmatic trial. The full text is qualitative throughout and reports no quantitative outcome from protocol section 4. Protocol section 3.1 excludes qualitative studies of that kind from the synthesis. Exclude. The parent trial is in the set in its own right (R0235 and R0257 report trial programmes at other centres; this record adds no extractable data).

## The same-title pair: one study, two reports (1 flagged record)

- **R0363 and R0516 are two reports of one study.** Evidence: R0516 carries DOI 10.2196/preprints.64993, the JMIR preprint of manuscript 64993; R0363 carries DOI 10.2196/64993, the published version of the same manuscript number, in JMIR, 2025. Titles match word for word apart from the word Preprint in R0516, and the abstract text is the same. Decision: one study. The published report, R0363, is the report of record and is included. R0516 was not retrieved as a full text and adds no study. The same pattern was found three more times inside the assessed set, and those preprints were excluded as duplicate reports: R0323 (of R0257), R0332 (of R0245), R0407 (of R0030), R0424 (of R0206).

## Not retrieved (4)

- **R0138**. Retrieved file was the publisher abstract page only. The abstract describes a field evaluation in two real public health units with a documentation time result stated per unit (mean change of minus 12.9 minutes at one unit, plus 10.4 minutes at the other). That reads as an eligible field study, but without the full text it cannot be assessed or extracted to the standard this stage set. Held in not retrieved, and named here as the first record to chase if a lawful copy appears. Not counted as included.
- **R0279**. Retrieved file was a Europe PMC JavaScript stub page. The Stage 2 question, whether the 7 against 7 carpal tunnel note comparison was systematic or a set of observations, stays open. Not retrieved.
- **R0458**. JCO meeting abstract (e13722). No full text retrieved; the record is a conference abstract. Under the Stage 3 data rule, a retrieved conference abstract without extractable outcome data would go to awaiting classification; this record was never retrieved, so it is recorded as not retrieved with that note.
- **R0513**. Conference abstract (abstract 533, BJS supplement). No full text retrieved, only the abstract, which does not settle whether the Heidi arm took ambient encounter audio as input. Not retrieved; the eligibility question stays open and is recorded here.

## Stage 2 excludes confirmed (10)

Full texts were not sought for Stage 2 excludes, so the basis stays the abstract recorded in flagged-for-author-v2.md. The Stage 3 tests were applied to the three records where a test could have changed the call, and none changed.

- **R0039**: coding and revenue outcomes only, no protocol outcome.
- **R0096**: simulation study measuring documentation time in simulated encounters, no note output audit. The Stage 3 note audit test confirms the exclude.
- **R0103**: handoff education co-design study, not encounter documentation.
- **R0144**: students in an OSCE setting; participants are not documenting clinicians in care.
- **R0157**: implementation case report, no measured protocol outcome in the abstract.
- **R0302**: trial operations playbook, no scribe outcome results.
- **R0383**: ASR word error rate only, no generated note audited. Confirmed: transcription accuracy of an engine is not a note error outcome as the protocol defines it.
- **R0399**: unedited word share only. Confirmed as not a protocol outcome: it is neither a time, a quality score, nor an error measure as defined.
- **R0517**: dictation based prototype in simulated encounters; wrong intervention and simulation only.
- **R0525**: no abstract, title only benchmark; Stage 2 exclude stands, and no full text was sought.
