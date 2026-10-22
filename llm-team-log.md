# LLM team log

This log is data for the finished review. The review reports these mechanics in its methods and results: how the LLM team was set up, where its members agreed, where they split, and what the splits cost. Tool: Muse (Meta), model Muse Spark, used through the author agent environment on 22 October 2026. Role prompts and decision procedures: prompts version 1, filed as prompts.md in this review folder.

## Roles at work so far
- Information specialist: built the strings in search-log.md, ran five source runs, logged two blocked sources with their errors, and prepared the pending strings in search-appendix-pending.md.
- Screener A (strict pass): separate decision procedure, title and abstract only. Calls: include 233, maybe 207, exclude 127.
- Screener B (sensitive pass): separate decision procedure, applied apart from A, no sight of A calls. Calls: include 339, maybe 122, exclude 106.
- Adjudicator: worked on disagreements only, under the rules in prompts version 1.
- Extractor pair, risk of bias pair, statistician, GRADE assessor, methods editor: not yet at work. Their stages come after full text retrieval. Nothing is logged for them until they run.

## Title and abstract screening mechanics, 22 October 2026
- Records screened: 567.
- Agreements: 439. Agreement rate: 0.7743.
- Cohen kappa: 0.6439.
- Disagreements: 128, by pair:
  - maybe vs include: 97
  - exclude vs maybe: 15
  - exclude vs include: 11
  - include vs exclude: 2
  - maybe vs exclude: 3
- Adjudication outcomes:
  - include/maybe settled as include: 97
  - maybe/exclude settled as maybe: 15
  - include/exclude settled as maybe, flagged for author: 13
  - maybe/exclude settled as exclude (hard bar): 3
- Final calls after adjudication: include 328, maybe 135, exclude 104.
- Flagged for the human author: 13 records, where one screener said include and the other exclude. They sit in the maybe group for full text, and the author settles each one at full text stage. Record IDs: R0128, R0136, R0198, R0201, R0339, R0401, R0493, R0509, R0520, R0527, R0528, R0534, R0547.

## Extraction mechanics
- Not started. Extraction discrepancy rate per field will be logged here once extractor A and extractor B have both worked on the included studies and the sheets have been compared field by field.

## Prompt changes
- Version 1, 22 October 2026: first version, used for the search and title and abstract screening above. A mid-course fix to the screening procedures was made before the counted run and is part of version 1 as counted: publication type parts split on semicolons were checked as separate types, the words review and protocol in a title were treated as the review type bar, and a near-duplicate pass was added at deduplication. The counted run used the fixed procedures throughout, so the numbers above belong to one consistent pass.

## Disclosure line for the manuscript, RAISE 2025
A team of large language model roles (Muse Spark, Meta, October 2026) carried out the team tasks of this review under named roles and independence rules set in the protocol. The human author set the question and eligibility rules, and is accountable for every judgement, every checked number and the final text.
