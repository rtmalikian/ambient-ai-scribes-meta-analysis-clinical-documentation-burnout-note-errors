# GitHub publication plan for Review 1

Status: plan only. Do not create the repository yet. The repo gets created in one step when the manuscript is finished, checked and signed off by the author. Nothing in the planned name, title or description states a result, because the review has not produced its results yet. The wording asks the question. It does not answer it.

Owner: rtmalikian on GitHub. Visibility: public. That is the point of the series. The work should be easy to find, read and check.

## Repository name

ambient-ai-scribes-meta-analysis-clinical-documentation-burnout-note-errors

Kebab case, 75 characters, inside the GitHub limit. Each term is a search term a clinician, a health system buyer or a researcher would type: ambient AI scribes, meta-analysis, clinical documentation, burnout, note errors.

Shorter fallback, if the long name reads badly at creation time: ambient-ai-scribes-meta-analysis

## Repository title for the README and release

Ambient AI Scribes Meta-Analysis: Documentation Time, After-Hours Work, Clinician Burnout, Note Quality, Note Errors and Hallucinations. A Cochrane-Level Systematic Review Built by an LLM Team

Use this as the first line of the README and as the title of the version 1.0 release. It names the intervention, all five outcome areas in the protocol, the review type and the method, in the order a search engine and a reader meet them.

## Repository description

Set this in the GitHub About field at creation. 304 characters, counted on 22 October 2026.

Cochrane-level systematic review and meta-analysis of ambient AI scribes for clinical documentation: do they cut documentation time and after-hours work, ease clinician burnout, and what note errors and hallucinations do they add? Built by an LLM team, human signed off. Protocol, data and code included.

Website field in the About box: add the Zenodo record link once the DOI exists. Add the medRxiv link in the same field only if the platform allows one link; if it allows one, Zenodo wins, and medRxiv goes in the README links section.

## Topics

Set all of these in the About box at creation, 18 topics:

1. ambient-ai
2. ai-scribes
3. clinical-documentation
4. systematic-review
5. meta-analysis
6. clinician-burnout
7. electronic-health-records
8. clinical-ai
9. healthcare-ai
10. medical-ai
11. large-language-models
12. llm
13. health-informatics
14. note-quality
15. ai-hallucinations
16. prisma
17. evidence-synthesis
18. physician-burnout

## README outline

The README is the front door of the paper. It carries the short forms in full and points to the long forms in the repo. Order:

1. Title, as above. Author line: Raphael Malikian, independent researcher, healthcare founder and operator, clinical AI builder. One line on method: Cochrane-level methods, LLM team, human author accountable for every number.
2. Structured abstract. The manuscript abstract in full, under 1,000 words, in Cochrane order: rationale, objectives, search methods, eligibility, outcomes, risk of bias, synthesis methods, included studies, results per outcome with GRADE ratings, author conclusions, funding (none), registration number.
3. Plain language summary. Written for a clinic manager: what was asked, what was found, what it means for a buying or staffing decision, in plain words, no result stated beyond what the abstract states.
4. The question and PICO. Population, intervention, comparator and outcomes in a small table, taken from the protocol without change.
5. PRISMA 2020 flow. The flow diagram as an image, with the counts under it: identified per database, duplicates removed, screened, excluded, full texts sought and assessed, studies included. Every count in this section must match prisma-flow.md and screening.csv.
6. Summary of findings. The GRADE table, at most seven outcomes: documentation time, after-hours documentation time, burnout and work exhaustion, note errors as omissions, note errors as hallucinations or fabrications, note errors as wrong inclusions, note quality. Effect, interval, studies, participants and certainty per outcome.
7. The LLM team. Role map from the protocol: information specialist, screeners A and B, adjudicator, extractors A and B, risk of bias pair, statistician, GRADE assessor, methods editor. Independence rules in short form. The mechanics numbers: inter-screener agreement rate and Cohen kappa, disagreement count and types, adjudication outcomes, extraction discrepancy rate. Link to llm-team-log.md in the repo.
8. Files in this repo. Map of the folder: manuscript PDF and Markdown, protocol, PROSPERO form copy, search log with strings as run, search results CSV, screening CSV, extraction sheets, risk of bias forms, analysis code in R, figures.
9. Data and code availability. Statement that the search data, screening calls, extraction sheets and analysis code are in this repo under the licence set at creation, and that any reader can rerun the analysis from the posted data. Licence to be picked at creation: CC BY 4.0 for text and data, MIT for code, stated here so creation takes one step.
10. Links. Zenodo record and DOI, medRxiv record if posted, PROSPERO record, conference abstract record if accepted. Placeholder lines stay in the draft README until each record exists. No link is typed from memory; each is pasted from the record page at creation.
11. Declarations. Funding: none. Conflicts of interest: none, fully independent. AI use statement in the RAISE 2025 form used in the manuscript. Scope note: evidence synthesis and policy discussion only, no clinical or medication advice.
12. How to cite. Citation block with author, title, year, version and the Zenodo DOI once it exists, plus a CITATION.cff file in the repo root so GitHub shows its cite button.
13. Version history. Release notes per version: protocol version, preprint version, journal version if accepted, each with a date and a one line note on what changed.

## Creation checklist, for the day the manuscript is done

- Create the repo under rtmalikian with the name above, public, with the description and topics set at creation.
- Push the finished review folder as the repo contents, after a check that no draft file with unproduced numbers sits in it.
- Add CITATION.cff, licence files and the README as set out above.
- Tag version 1.0 as a GitHub release, title as above, notes carrying the structured abstract.
- Add the Zenodo link to the About website field, and check the GitHub to Zenodo link back from the Zenodo record.
- Post the launch drafts for X and LinkedIn that come with the paper report. Nothing auto-posts.
