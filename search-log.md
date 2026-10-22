# Search log

All searches run on 22 October 2026 by the information specialist role, through public APIs. Strings below are copied as run. Hit count is the count the source returned. Retrieved is the number of records exported from that run. Every retrieved record sits in search-results-full.json (working file) and, after deduplication, in search-results.csv.

## Runs

### PubMed, through NCBI E-utilities (MEDLINE)
- String as run: `("ambient scribe*"[Title/Abstract] OR "AI scribe*"[Title/Abstract] OR "artificial intelligence scribe*"[Title/Abstract] OR "ambient documentation"[Title/Abstract] OR "ambient clinical documentation"[Title/Abstract] OR "ambient listening"[Title/Abstract] OR "DAX Copilot"[Title/Abstract] OR "Dragon Ambient eXperience"[Title/Abstract] OR "ambient artificial intelligence"[Title/Abstract]) AND ("2019/01/01"[Date - Publication] : "2026/10/22"[Date - Publication])`
- Hit count: 385. Retrieved: 385.
- Retrieval: esearch for the full ID list, then efetch in batches of 100, XML.

### Europe PMC, REST API, result type core
- String as run: `(TITLE_ABS:"ambient scribe" OR TITLE_ABS:"AI scribe" OR TITLE_ABS:"ambient documentation" OR TITLE_ABS:"ambient clinical documentation" OR TITLE_ABS:"ambient listening" OR TITLE_ABS:"DAX Copilot" OR TITLE_ABS:"ambient artificial intelligence") AND FIRST_PDATE:[2019-01-01 TO 2026-10-22]`
- Hit count: 299. Retrieved: 299.
- Retrieval: cursor paging, page size 100, until the cursor closed.

### OpenAIRE search API, run 1, title words ambient scribe
- String as run: title=ambient scribe, fromDateAccepted 2019-01-01 to 2026-10-22. Both words must appear in the title.
- Hit count: 145. Retrieved: 145.
- OpenAIRE indexes Crossref and Europe PMC records. It was used as the Crossref source for this pass.

### OpenAIRE search API, run 2, title words AI scribe
- String as run: title=AI scribe, fromDateAccepted 2019-01-01 to 2026-10-22. Both words must appear in the title.
- Hit count: 201. Retrieved: 201.

### ClinicalTrials.gov, API version 2
- String as run: query.term = ambient scribe OR "AI scribe" OR "ambient documentation" OR "ambient artificial intelligence"
- Hit count: 19. Retrieved: 19.

### Semantic Scholar, Graph API paper search
- String as run: query=ambient scribe, year 2019-2026, limit 100.
- Result: FAILED. HTTP 429 on the test call and again on the run call. Hit count not obtained, records retrieved: 0. This source is logged as attempted and blocked, not as searched. A rerun needs an API key or a later date. No number has been filled in for it.

## Attempted and blocked

### OpenAlex
- Test calls on 22 October 2026 returned HTTP 429. The API message stated that the free daily budget shared by everyone on this network IP address was used up, resetting at midnight UTC, and that a personal API key avoids the limit. No key is held for this review. OpenAlex is logged as attempted and blocked, not as searched.
- Crossref direct was checked as the pair source. Its bibliographic query does not hold a phrase, and returned a total of 1,697,757 for the test string, which is a match count, not a usable result set. OpenAIRE, which indexes Crossref, was used in its place for the two title runs above.

## Totals
- Records retrieved, all runs: 1049.
- Duplicates removed (DOI first, then normalised title, then a near-duplicate pass on title prefix with same year and same first author): 482.
- Records after deduplication, taken to screening: 567.

## Not run in this pass
Embase, CINAHL, PsycINFO, Cochrane CENTRAL, Scopus, Web of Science, ACM Digital Library, WHO ICTRP and a Google Scholar first 200 pass were not run. This environment holds no licensed access to them. Exact strings ready to run sit in search-appendix-pending.md, each marked string prepared, run pending access. The finished review must not claim those databases were searched until a dated run with a hit count is added to this log.
