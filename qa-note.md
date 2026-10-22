# QA note, Stage 5 (analysis, GRADE, manuscript), 22 October 2026

## De-AI audit (rules: ~/workspace/rules/de-ai-copy-rules.md)

Audit question asked of the finished text: "What makes this read as AI-generated?" Findings and fixes:

- Em dashes: 0 in manuscript.md, analysis-results.md and summary-of-findings.md (full character scan). En dashes: 0. Ranges are written with "to".
- Banned vocabulary scan over the same three files, using the full list in the rules file: one hit. The word "streamline" appears once, inside a verbatim study title in the references ("The STREAMLINE Pilot Study on Time Reduction and Efficiency in AI-Mediated Logging for Improved Note-Taking Experience", R0355). It is the study's own acronym, kept as data. No banned word appears in prose written for this review.
- Negative parallelisms: 0 hits for "not only", "not just", "it's not". Template scaffolding: 0 hits for "in conclusion", "serves as", "stands as". No forced rule-of-three passages were left standing; where three items appear (the three error types, the three quantities in the vigilance trade), they are the data, not decoration.
- Sentence length: 446 sentences in the main text, median 18 words, 57 sentences at 6 words or fewer. Short sentences sit next to long ones throughout, per the burstiness rule.
- Strong claims: checked paragraph by paragraph. Each strong claim in the abstract, discussion and conclusions carries its number in the same paragraph (time -18.9% and SMD -0.52/-0.31; exhaustion SMD -0.44; omissions 18.0%, hallucinations 11.5%; Bergman detection split 6.2% vs 24.4%; retrieval gap 74 of 157). Attributions are named (Zhao 2025; Lukac 2025; NHS England 27 April 2025; Joint Commission and CHAI 17 September 2025; FDA 6 November 2025). No vague attributions remain.

## Numbers audit

- Every pooled estimate in the three documents was produced by stage5/meta_analysis.py and written to stage5/analysis-results.json. A script cross-check compared 11 headline pools, the error proportion pool and both Egger tests against the documents: all matched after rounding corrections below.
- Rounding corrections found by the cross-check and fixed in all three documents: after-hours pooled SMD is -0.2546, printed as -0.25 (an earlier pass wrote -0.26); the PFI mean difference interval lower bound is -0.5248, printed as -0.52 (was -0.53); Kashiouris 2026 workload g is -2.657, printed as -2.66 (was -2.65); Olson 2025 workload SMD is -1.597, printed as -1.60 (was -1.59). The Abridge after-hours subset (-0.2554, printed -0.26) was checked and is correct as printed.
- Visual inspection of the rendered forest plots caught a real bug: pooled diamonds were drawn as slanted slivers (wrong vertex pairing in the plot function). Fixed in meta_analysis.py, script rerun, all pooled estimates identical after the rerun, plots regenerated, PDF re-rendered. The fixed time SMD plot was inspected directly and the diamonds render correctly.
- Selection integrity: one effect per study per outcome in stage5/selected-effects.csv (63 rows), each with its derivation. Studies that could not be standardised honestly (Husa, Rotenstein, Afshar time, Wright 2025 time, Prasser after-hours) are in the narrative record with the reason stated, not in the pools.

## Structure and rendering checks

- Abstract: 597 words (limit 1,000). Main text, title page through declarations, excluding references and appendices: 9,287 words (target under 12,000). Total file: 16,143 words including references and appendices.
- Summary of findings table sits before the Background, as the protocol's structure requires. Seven outcomes.
- PDF: manuscript.pdf, 43 pages, A4, rendered from manuscript.md with Python Markdown and WeasyPrint 70.0. All 8 figures are embedded (pdfimages lists 8 images on pages 11 to 17). Pages 3 (summary of findings) and 11 (first forest plot) were inspected as rendered pages: tables and plots render cleanly, no missing image placeholders.
- Author framing: the manuscript describes the author as an independent researcher, healthcare founder and operator, and clinical AI builder. Scan for "former physician" and licensure claims: 0 hits. Conclusions contain no clinical recommendation, no medication recommendation and no instruction to deploy any product.
- References: only works cited in the text. Included studies are listed with the DOI or PMID exactly as recorded in extraction.csv. Methods and guidance sources are listed as named in protocol.md and concept-and-protocol.md; no identifier was invented for a source whose file record carries none.

## Known weaknesses carried into the manuscript, declared there

- 74 of 157 sought reports were not retrieved; eight prepared database searches were not run (no licensed access); OpenAlex and Semantic Scholar were blocked by rate limits.
- Stage 1 screening was too permissive and was corrected by a strict Stage 2 abstract pass; both steps are reported with counts.
- The any-error pooled proportion (59.8%) rests on two studies with different error definitions and 93 notes; it is graded very low and is not used as a headline.
- The workload pool mixes four constructs; the review's stated reading leans on the one lower risk study (SMD -0.39) rather than the pooled -1.46.
- The quality pool's weight sits 78.7% on one preprint (Bergman 2026); stated in the text.
- Protocol deviations declared in the manuscript: analysis in Python rather than R; prediction intervals reported from k 3 rather than k 10; specialty, clinician type and follow-up subgroups not run (no poolable strata).

## Files

- stage5/meta_analysis.py (rerunnable analysis), stage5/selected-effects.csv, stage5/analysis-results.json, stage5/analysis-results.md
- stage5/summary-of-findings.md
- stage5/summarise_characteristics.py, stage5/characteristics-summary.json, stage5/characteristics-of-included-studies.csv
- stage5/forest-time-smd.png, forest-time-relative.png, forest-afterhours-smd.png, forest-burnout-smd.png, forest-workload-smd.png, forest-quality-smd.png, forest-errors-any.png, funnel-time-smd.png
- manuscript.md and manuscript.pdf in the review1 folder
