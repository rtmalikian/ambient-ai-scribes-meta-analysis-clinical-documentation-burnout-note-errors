#!/usr/bin/env python3
"""
Stage 5 meta-analysis for Review 1: ambient AI scribes.
Input files are read only for study metadata (design, vendor class, product)
and risk of bias judgements. Effect sizes are encoded in SELECTED below, one
effect per study per outcome, each with its derivation recorded. Every number
in analysis-results.md is produced by this script.
Methods: REML random effects, inverse variance. Hartung-Knapp interval where
k >= 3, normal interval where k = 2. Prediction interval where k >= 3 using
t with k-2 df and the model based standard error. Hedges g used for SMDs
computed from group means. Binary burnout counts converted to SMD by the Cox
transformation (d = log OR * sqrt(3) / pi). Error proportions pooled on the
logit scale.
"""
import json, math, os
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BASE = os.path.expanduser("~/workspace/publications/weekly-series/meta-analysis-ambient-scribes/review1")
OUT = os.path.join(BASE, "stage5")
os.makedirs(OUT, exist_ok=True)

ext = pd.read_csv(os.path.join(BASE, "extraction.csv"), dtype=str).fillna("")
rob = pd.read_csv(os.path.join(BASE, "rob-assessments.csv"), dtype=str).fillna("")
EXT = {r.record_id: r for r in ext.itertuples()}
ROB = {(r.record_id, r.outcome_group): r.ADJ_overall for r in rob.itertuples()}

def meta_from_raw(m1, sd1, n1, m2, sd2, n2, paired=False):
    """Hedges g, scribe minus comparator. Variance uses the independent
    samples formula; for paired designs without a printed CI this is the
    conservative choice and is flagged in the selection note."""
    dfree = n1 + n2 - 2
    sp = math.sqrt(((n1 - 1) * sd1**2 + (n2 - 1) * sd2**2) / dfree)
    d = (m1 - m2) / sp
    J = 1 - 3 / (4 * dfree - 1)
    g = J * d
    var_d = (n1 + n2) / (n1 * n2) + d**2 / (2 * dfree)
    return g, math.sqrt(J**2 * var_d), sp

def se_from_ci(lo, hi):
    return (hi - lo) / (2 * 1.959963984540054)

# Each entry: record, outcome, effect kind, yi, sei, n_units, product_group,
# selection note. Design, vendor class and RoB are joined from the files.
S = []
def add(outcome, record, yi, sei, n_units, product_group, note, kind="SMD"):
    S.append(dict(outcome=outcome, record_id=record, yi=float(yi), sei=float(sei),
                  n_units=int(n_units), product_group=product_group, note=note, kind=kind))

# ---------------- Documentation time, SMD (negative favours scribe) -------
# R0023 raw means
g, se, sp = meta_from_raw(6, 2.2, 15, 14, 11.2, 98)
add("time_smd", "R0023", g, se, 113, "Abridge", "Raw group means and SDs, Table 1. Pooled SD 10.44 min.")
# R0043 paired median difference +0.17, CI -1.00 to 1.55, n 164 paired.
sd_diff = se_from_ci(-1.00, 1.55) * math.sqrt(164)
add("time_smd", "R0043", 0.17 / sd_diff, se_from_ci(-1.00, 1.55) / sd_diff, 164, "Abridge",
    "Printed paired median difference and CI. Standardised by the SD of paired differences derived from the CI and n (dz).")
# R0068 raw means, encounters
g, se, sp = meta_from_raw(12.03, 3.73, 55, 15.06, 5.40, 57)
add("time_smd", "R0068", g, se, 112, "DAX", "Raw encounter means and SDs. Pooled SD 4.63 min.")
# R0102 adjusted MD -72.6 s, CI -81.4 to -63.8; pooled raw SD 173.2 s
sp = math.sqrt(((1881 - 1) * 131**2 + (8463 - 1) * 183**2) / (1881 + 8463 - 2))
add("time_smd", "R0102", -72.6 / sp, se_from_ci(-81.4, -63.8) / sp, 10344, "DAX",
    "Printed adjusted mixed model difference, standardised by the pooled raw SD of seconds per encounter (173.2 s). Encounter level analysis units.")
# R0123 paired subanalysis, ambient vs manual, seconds
g, se, sp = meta_from_raw(219, 115, 48, 336, 118, 48)
add("time_smd", "R0123", g, se, 96, "Abridge", "Paired subanalysis, ambient AI vs manual documentation, administrative time per patient. Independent samples variance used, which is conservative for a paired contrast.")
# R0181 RCT raw means
g, se, sp = meta_from_raw(11.76, 3.55, 139, 13.90, 3.87, 140)
add("time_smd", "R0181", g, se, 279, "Other", "Surgeon note completion time, raw means and SDs, letters as units. Product Heidi, grouped as Other for the product subgroup.")
# R0111 Harvey, per appointment, direct CI standardised by pooled SD
sp = math.sqrt((3.50**2 + 3.54**2) / 2)
add("time_smd", "R0111", (5.63 - 7.14) / sp, se_from_ci(-2.07, -0.37) / sp, 90, "Abridge",
    "High user group, time in notes per appointment. Effect from group means, SE from the printed CI for the difference, standardised by pooled SD 3.52 min.")
# R0127 Olson, GEE MD -1.43, CI -2.23 to -0.63, pooled SD 5.79
sp = math.sqrt((6.11**2 + 5.45**2) / 2)
add("time_smd", "R0127", -1.43 / sp, se_from_ci(-2.23, -0.63) / sp, 60, "Abridge",
    "Printed GEE difference in minutes per encounter, standardised by pooled SD 5.79 min. Paired pre-post, 30 pharmacists counted in both periods.")
# R0186 Tan, adjusted MD -0.8, CI -1.5 to -0.05, pooled SD 2.57
sp = math.sqrt(((78 - 1) * 2.4**2 + (91 - 1) * 2.7**2) / (78 + 91 - 2))
add("time_smd", "R0186", -0.8 / sp, se_from_ci(-1.5, -0.05) / sp, 169, "Other",
    "Printed adjusted difference, standardised by pooled SD 2.57 min. Product Note Buddy, grouped as Other.")
# R0206 van Linschoten, MD -42.72 s, CI -56.29 to -30.78; SD derived from SE and ns
se_md = se_from_ci(-56.29, -30.78)
sd_imp = se_md / math.sqrt(1 / 271 + 1 / 264)
add("time_smd", "R0206", -42.72 / sd_imp, se_md / sd_imp, 535, "Other",
    "Printed difference in seconds per consultation. No SD printed; the standardiser (75.3 s) is derived from the printed CI and the two group sizes on an independent samples basis. Product Juvoly, grouped as Other.")
# R0270 North, MD -0.95 from group CIs
se1 = se_from_ci(3.86, 4.46); se2 = se_from_ci(4.75, 5.47)
sd1 = se1 * math.sqrt(332); sd2 = se2 * math.sqrt(332)
sp = math.sqrt((sd1**2 + sd2**2) / 2)
se_md = math.sqrt(se1**2 + se2**2)
add("time_smd", "R0270", -0.95 / sp, se_md / sp, 664, "Abridge",
    "Time in notes per note. Group means with printed CIs give the pooled SD (3.08 min) and the SE of the difference.")
# R0346 Stults, MD -0.91, CI -1.20 to -0.62, pooled SD 3.76
sp = math.sqrt((3.5**2 + 4.0**2) / 2)
add("time_smd", "R0346", -0.91 / sp, se_from_ci(-1.20, -0.62) / sp, 182, "Abridge",
    "Time in notes per appointment, printed difference and CI, standardised by pooled SD 3.76 min.")
# R0360 Duggan, adjusted beta -1.6, CI -2.3 to -0.8, pooled SD 8.06
sp = math.sqrt((6.8**2 + 9.2**2) / 2)
add("time_smd", "R0360", -1.6 / sp, se_from_ci(-2.3, -0.8) / sp, 92, "DAX",
    "Printed adjusted model estimate, standardised by pooled SD 8.06 min per appointment.")

# ---------------- After-hours time, SMD (uncontrolled only) --------------
add("afterhours_smd", "R0111", (23.89 - 27.47) / math.sqrt((24.96**2 + 35.72**2) / 2),
    se_from_ci(-5.77, 1.20) / math.sqrt((24.96**2 + 35.72**2) / 2), 90, "Abridge",
    "Pajama time, high users. Effect from group means, SE from the printed CI for the difference.")
add("afterhours_smd", "R0127", -0.73, se_from_ci(-1.128, -0.324), 60, "Abridge",
    "Printed Cohen d for after-hours documentation, with its printed CI.")
sp = math.sqrt((((0.16 * math.sqrt(263))**2) + ((0.18 * math.sqrt(263))**2)) / 2)
add("afterhours_smd", "R0295", -0.90 / sp, 0.19 / sp, 526, "Abridge",
    "Documentation after hours, hours per week. Printed difference 0.90 (SE 0.19); group SEs and n give the pooled SD (2.76 h).")
g, se, sp = meta_from_raw(39.8, 42.9, 91, 38.2, 42.0, 91)
add("afterhours_smd", "R0346", g, se, 182, "Abridge",
    "Off-hour EHR activities, raw means and SDs. Independent samples variance used for a paired contrast, which is conservative.")
sp = math.sqrt((52.0**2 + 64.3**2) / 2)
add("afterhours_smd", "R0360", -8.6 / sp, se_from_ci(-15.7, -1.4) / sp, 92, "DAX",
    "After-hours work per scheduled day, printed adjusted estimate, standardised by pooled SD 58.6 min.")
sp = math.sqrt(((25 - 1) * 2.25**2 + (28 - 1) * 2.74**2) / (25 + 28 - 2))
add("afterhours_smd", "R0392", -1.4 / sp, se_from_ci(-2.9, -0.6) / sp, 53, "Other",
    "Hours per week on notes outside clinic, printed difference (1.4 h lower) and CI, standardised by pooled SD 2.51 h. Two unnamed products, grouped as Other.")

# ---------------- Documentation time, relative change (percent) ----------
REL = [
    # record, effect %, lo, hi, n_units, product_group, note
    ("R0023", -57.1, -74.9, -39.4, 113, "Abridge", "Raw means 6 vs 14 min; CI from the raw difference divided by the comparator mean."),
    ("R0043", 0.9, -5.4, 8.4, 164, "Abridge", "Paired median difference +0.17 min on a comparator median of 18.4 min."),
    ("R0068", -20.1, -31.5, -8.8, 112, "DAX", "Raw means 12.03 vs 15.06 min; CI from the raw difference."),
    ("R0102", -28.6, -32.0, -25.1, 10344, "DAX", "Adjusted difference -72.6 s on a raw comparator mean of 254 s per encounter."),
    ("R0111", -21.2, -29.0, -5.2, 90, "Abridge", "Time in notes per appointment, high users; printed CI for the difference over the baseline mean."),
    ("R0123", -34.8, -48.7, -21.0, 96, "Abridge", "Paired subanalysis, ambient vs manual administrative time per patient."),
    ("R0127", -10.0, -15.6, -4.4, 60, "Abridge", "GEE difference -1.43 min on a baseline mean of 14.32 min per encounter."),
    ("R0148", -29.7, -38.4, -19.9, 1615, "DAX", "Mixed model log minutes beta -0.353 (CI -0.484 to -0.222), converted to a ratio of means. Analysis units are appointments (414 DAX, 1201 comparator)."),
    ("R0181", -15.4, -21.7, -9.1, 279, "Other", "Surgeon note completion time, raw means; CI from the raw difference."),
    ("R0186", -15.0, -28.3, -0.9, 169, "Other", "Printed adjusted difference -0.8 min (CI -1.5 to -0.05) on a baseline mean of 5.3 min."),
    ("R0257", -5.6, -12.3, 1.1, 159, "DAX", "December relative differences, DAX -1.7% and Nabla -9.5% averaged to one study effect; SE allows for the shared control (assumed correlation 0.5 between the two contrasts)."),
    ("R0270", -18.6, -27.8, -9.4, 664, "Abridge", "Time in notes per note, 0.95 min saved on a baseline mean of 5.11 min."),
    ("R0292", -15.9, -21.2, -10.4, 603, "Abridge", "Propensity overlap weighted effect on time in notes per appointment, as printed."),
    ("R0346", -14.7, -19.4, -10.0, 182, "Abridge", "Printed difference -0.91 min (CI -1.20 to -0.62) on a baseline mean of 6.2 min per appointment."),
    ("R0360", -15.2, -22.3, -7.8, 92, "DAX", "Printed model estimate -15.2%; CI from the beta CI over the baseline mean of 10.3 min."),
]
for rec, eff, lo, hi, n, pg, note in REL:
    add("time_relative", rec, eff, se_from_ci(lo, hi), n, pg, note, kind="percent")

# ---------------- Burnout / work exhaustion, continuous SMD --------------
# Afshar: MD -0.44 (CI -0.62 to -0.25) on PFI; baseline SD 0.96 (extraction-outcomes).
add("burnout_smd", "R0235", -0.44 / 0.96, se_from_ci(-0.62, -0.25) / 0.96, 66, "Abridge",
    "PFI work exhaustion and interpersonal disengagement. Printed model difference standardised by the study baseline SD of 0.96 points.")
# Lukac: combined two arms. SD of change derived from the unadjusted
# regression SEs and respondent counts (65, 65, 61); shared control
# correlation 0.164 from the derived variance components.
se_arm = se_from_ci(-0.55, -0.08)
sd_change = se_arm / math.sqrt(1 / 65 + 1 / 61)
var_arm = se_arm**2
cov = sd_change**2 / 61
se_comb = math.sqrt((var_arm + var_arm + 2 * cov) / 4)
add("burnout_smd", "R0257", (-0.32 + -0.23) / 2 / sd_change, se_comb / sd_change, 191, "DAX and Nabla",
    "PFI work exhaustion, DAX -0.32 and Nabla -0.23 averaged to one study effect. SE allows for the shared control. Standardiser is the derived SD of change, 0.67 points.")
# Olson JAMA Network Open: burnout score, difference 0.47 (SE 0.12) on a
# 10 point scale; group SE 0.15 with n 186 gives SD 2.05.
sd_o = 0.15 * math.sqrt(186)
add("burnout_smd", "R0295", -0.47 / sd_o, 0.12 / sd_o, 372, "Abridge",
    "Burnout score on a 10 point scale, printed paired difference 0.47 (SE 0.12); standardiser from the printed group SE and n.")
# Pollak: CBI personal burnout, raw means and SDs.
g, se, sp = meta_from_raw(38.72, 25.31, 25, 47.55, 25.31, 28)
add("burnout_smd", "R0392", g, se, 53, "Other", "Copenhagen Burnout Inventory personal subscale, raw means and SDs.")

# PFI mean difference, controlled trials only (same instrument family)
add("burnout_pfi_md", "R0235", -0.44, se_from_ci(-0.62, -0.25), 66, "Abridge",
    "Printed model difference on the PFI work exhaustion composite.", kind="MD")
add("burnout_pfi_md", "R0257", -0.275, se_comb, 191, "DAX and Nabla",
    "DAX and Nabla contrasts averaged; SE allows for the shared control.", kind="MD")

# Binary burnout, converted to SMD (Cox), sensitivity set only
def add_binary(record, a, n1, b, n2, pg, note):
    orr = (a / (n1 - a)) / (b / (n2 - b))
    lor = math.log(orr)
    se_lor = math.sqrt(1 / a + 1 / (n1 - a) + 1 / b + 1 / (n2 - b))
    conv = math.sqrt(3) / math.pi
    add("burnout_binary_smd", record, lor * conv, se_lor * conv, n1 + n2, pg, note)
add_binary("R0111", 40, 79, 47, 79, "Abridge", "Providers reporting burnout symptoms, post vs pre counts. The printed OR of 1.4 runs pre over post; the counts give OR 0.70 post over pre, used here.")
add_binary("R0308", 59, 192, 101, 192, "Other", "PFI overall burnout over threshold, latest time point (84 days), post vs pre counts.")
add_binary("R0346", 20, 57, 24, 57, "Abridge", "Mini-Z single item burnout, post vs pre counts.")
add_binary("R0412", 15, 35, 24, 35, "Other", "PFI overall burnout at or over the validated cutoff, post vs baseline counts.")
# Olson pharmacists: printed OR 0.438 (CI 0.154 to 1.243), paired analysis.
lor = math.log(0.438); se_lor = (math.log(1.243) - math.log(0.154)) / (2 * 1.959963984540054)
conv = math.sqrt(3) / math.pi
add("burnout_binary_smd", "R0127", lor * conv, se_lor * conv, 60, "Abridge",
    "Mini-Z binary burnout, printed paired OR 0.438 with CI, converted to SMD. Marginal counts (10/30 vs 20/30) differ from the paired OR and were not used.")

# ---------------- Workload (task load), SMD ------------------------------
g, se, sp = meta_from_raw(31.89, 16.88, 15, 72.13, 13.52, 25)
add("workload_smd", "R0043", g, se, 40, "Abridge", "NASA-TLX total, survey respondents post (n 15) vs pre (n 25), raw means and SDs.")
g, se, sp = meta_from_raw(30.0, 5.3, 5, 40.2, 6.1, 5)
add("workload_smd", "R0068", g, se, 10, "DAX", "NASA-TLX total, clinic days as units (n 5 per period, one surgeon), raw means and SDs.")
add("workload_smd", "R0127", -1.90, se_from_ci(-2.500, -1.318), 60, "Abridge",
    "Documentation burden, NASA-TLX composite of three items. Printed Cohen d -1.90 (Table 3 value; the Discussion prints -1.93) with CI.")
# Lukac PTL combined arms, derivation parallel to PFI above.
se_ptl = se_from_ci(-71.88, -7.90)
sd_ptl = se_ptl / math.sqrt(1 / 65 + 1 / 61)
var_ptl = se_ptl**2; cov_ptl = sd_ptl**2 / 61
se_ptl_comb = math.sqrt((var_ptl + var_ptl + 2 * cov_ptl) / 4)
add("workload_smd", "R0257", (-39.89 + -31.69) / 2 / sd_ptl, se_ptl_comb / sd_ptl, 191, "DAX and Nabla",
    "Four item physician task load, DAX and Nabla contrasts averaged; SE allows for the shared control; standardiser is the derived SD of change.")
sp = math.sqrt(((0.12 * math.sqrt(243))**2 + (0.09 * math.sqrt(243))**2) / 2)
add("workload_smd", "R0295", -2.64 / sp, 0.13 / sp, 486, "Abridge",
    "Note related cognitive task load composite on a 10 point scale. Printed paired difference 2.64 (SE 0.13); standardiser from the printed group SEs and n.")
g, se, sp = meta_from_raw(43.3, 18.1, 37, 56.3, 11.0, 37)
add("workload_smd", "R0324", g, se, 74, "Abridge", "NASA-TLX raw total, paired pre-post surveys, raw means and SDs. Independent samples variance used, which is conservative for a paired contrast.")
sp = math.sqrt((3.7**2 + 4.0**2) / 2)
add("workload_smd", "R0346", -6.12 / sp, se_from_ci(-7.52, -4.72) / sp, 114, "Abridge",
    "NASA-TLX mental demand item (no total score printed). Printed adjusted difference -6.12 with CI, standardised by pooled SD 3.85 points.")

# ---------------- Note quality, SMD (positive favours scribe) -----------
g, se, sp = meta_from_raw(2.89, 0.16, 48, 2.76, 0.23, 48)
add("quality_smd", "R0123", g, se, 96, "Other", "Total documentation score (1 to 3 scale), ambient AI vs manual documentation, paired subanalysis. Independent samples variance used.")
g, se, sp = meta_from_raw(47.3, 1.0, 12, 46.7, 1.2, 12)
add("quality_smd", "R0128", g, se, 24, "Other", "Modified PDQI-9 total (out of 50), ambient workflow vs traditional dictation. Scored by LLM raters with a negative inter-rater agreement statistic in the source; see risk of bias.")
g, se, sp = meta_from_raw(91.86, 3.58, 139, 89.21, 4.42, 140)
add("quality_smd", "R0181", g, se, 279, "Other", "Overall letter quality rating (0 to 100), raw means and SDs.")
g, se, sp = meta_from_raw(44.08, 3.32, 4, 37.42, 9.78, 4)
add("quality_smd", "R0277", g, se, 8, "Other", "Modified PDQI-9 total, top scoring AI scribe vs human documentation, four standardised scenarios per arm.")
add("quality_smd", "R0385", 0.90, math.sqrt(1 / 8 + 0.90**2 / (2 * 8)), 16, "Other",
    "SAIL total quality score. Printed Cohen dz 0.90; SE from the standard dz variance formula with n 8 pairs.")
add("quality_smd", "R0408", 0.55, se_from_ci(0.46, 0.66), 770, "Other",
    "PDQI-9 total. Printed Cohen dz 0.55 with CI 0.46 to 0.66, 385 paired consultations counted in both arms.")
# PDQI family subset
for rec in ["R0128", "R0277", "R0408"]:
    row = [s for s in S if s["outcome"] == "quality_smd" and s["record_id"] == rec][0]
    add("quality_pdqi_smd", rec, row["yi"], row["sei"], row["n_units"], "Other", row["note"])

# ---------------- Note errors, any error proportion (logit) -------------
def add_prop(record, events, n, pg, note):
    y = math.log(events / (n - events)); se = math.sqrt(1 / events + 1 / (n - events))
    add("errors_any_logit", record, y, se, n, pg, note, kind="logit proportion")
add_prop("R0363", 31, 44, "Other", "Draft notes with at least one error, 31 of 44. Mean 2.9 errors per note in the same study.")
add_prop("R0395", 24, 49, "Other", "Notes with at least one clinically meaningful error, derived as 49 minus the 25 notes the study reports as free of clinically meaningful errors.")

sel = pd.DataFrame(S)
# Join metadata
def design_group(dc):
    if dc in ("RCT", "stepped wedge"): return "randomised"
    if dc in ("non-randomised controlled", "controlled before-after", "interrupted time series"): return "non-randomised controlled"
    if dc == "uncontrolled before-after": return "before-after"
    return "other"
rows = []
for r in sel.itertuples():
    e = EXT[r.record_id]
    og = {"time_smd": "time", "time_relative": "time", "afterhours_smd": "time",
          "burnout_smd": "burnout", "burnout_pfi_md": "burnout", "burnout_binary_smd": "burnout",
          "workload_smd": "burnout", "quality_smd": "quality", "quality_pdqi_smd": "quality",
          "errors_any_logit": "errors"}[r.outcome]
    rows.append(dict(outcome=r.outcome, record_id=r.record_id,
                     study=f"{e.first_author} {e.year}", design_class=e.design_class,
                     design_group=design_group(e.design_class),
                     controlled=("controlled" if design_group(e.design_class) in ("randomised", "non-randomised controlled") else "uncontrolled/other"),
                     product_group=r.product_group, product_reported=e.product,
                     vendor_class=e.vendor_class, report_type=e.report_type,
                     rob_overall=ROB.get((r.record_id, og), ""), yi=r.yi, sei=r.sei,
                     n_units=r.n_units, kind=r.kind, note=r.note))
sel = pd.DataFrame(rows)
sel.to_csv(os.path.join(OUT, "selected-effects.csv"), index=False)

# ---------------- Meta-analysis engine ----------------------------------
def reml_tau2(y, v):
    y = np.asarray(y, float); v = np.asarray(v, float)
    k = len(y)
    if k < 2: return 0.0
    def negll(t2):
        w = 1 / (v + t2); mu = np.sum(w * y) / np.sum(w)
        return 0.5 * (np.sum(np.log(v + t2)) + np.sum((y - mu)**2 / (v + t2)) + np.log(np.sum(w)))
    grid = np.concatenate([[0.0], np.logspace(-6, 2, 400)])
    vals = [negll(t) for t in grid]
    t2 = float(grid[int(np.argmin(vals))])
    # golden section refine around the grid minimum
    lo = t2 / 3 if t2 > 0 else 0.0; hi = t2 * 3 if t2 > 0 else 0.01
    for _ in range(200):
        m1 = lo + (hi - lo) * 0.381966; m2 = lo + (hi - lo) * 0.618034
        if negll(m1) < negll(m2): hi = m2
        else: lo = m1
    return float((lo + hi) / 2)

def meta(df):
    y = df.yi.to_numpy(float); v = df.sei.to_numpy(float)**2
    k = len(y)
    wf = 1 / v
    mu_f = np.sum(wf * y) / np.sum(wf)
    Q = float(np.sum(wf * (y - mu_f)**2))
    I2 = max(0.0, (Q - (k - 1)) / Q * 100) if Q > 0 else 0.0
    t2 = reml_tau2(y, v)
    w = 1 / (v + t2)
    mu = float(np.sum(w * y) / np.sum(w))
    se_model = math.sqrt(1 / np.sum(w))
    if k >= 3:
        q_hk = float(np.sum(w * (y - mu)**2) / (k - 1))
        se_hk = math.sqrt(q_hk / np.sum(w))
        crit = stats.t.ppf(0.975, k - 1)
        lo, hi = mu - crit * se_hk, mu + crit * se_hk
        p = 2 * (1 - stats.t.cdf(abs(mu / se_hk), k - 1)) if se_hk > 0 else float("nan")
        se_ci = se_hk
    elif k == 2:
        se_ci = se_model; crit = 1.959963984540054
        lo, hi = mu - crit * se_ci, mu + crit * se_ci
        p = 2 * (1 - stats.norm.cdf(abs(mu / se_ci)))
    else:
        se_ci = float(df.sei.iloc[0]); lo, hi = mu - 1.96 * se_ci, mu + 1.96 * se_ci
        p = 2 * (1 - stats.norm.cdf(abs(mu / se_ci))) if se_ci > 0 else float("nan")
    if k >= 3:
        tcrit = stats.t.ppf(0.975, k - 2)
        pi = (mu - tcrit * math.sqrt(t2 + se_model**2), mu + tcrit * math.sqrt(t2 + se_model**2))
    else:
        pi = (None, None)
    return dict(k=int(k), n_units=int(df.n_units.sum()), mu=mu, se_model=se_model, se_ci=float(se_ci),
                lo=float(lo), hi=float(hi), p=float(p), Q=Q, I2=float(I2), tau2=float(t2),
                pi_lo=pi[0], pi_hi=pi[1])

def egger(df):
    y = df.yi.to_numpy(float); se = df.sei.to_numpy(float)
    z = y / se; prec = 1 / se
    X = np.column_stack([np.ones_like(prec), prec])
    beta, *_ = np.linalg.lstsq(X, z, rcond=None)
    resid = z - X @ beta
    dof = len(y) - 2
    s2 = float(resid @ resid) / dof
    cov = s2 * np.linalg.inv(X.T @ X)
    tstat = beta[0] / math.sqrt(cov[0, 0])
    p = 2 * (1 - stats.t.cdf(abs(tstat), dof))
    return dict(intercept=float(beta[0]), t=float(tstat), p=float(p))

RESULTS = {}
def run(name, df, label):
    if len(df) == 0:
        RESULTS[name] = dict(label=label, k=0)
        return None
    m = meta(df); m["label"] = label
    m["studies"] = df.study.tolist(); m["records"] = df.record_id.tolist()
    RESULTS[name] = m
    return m

def sub(df, **kw):
    out = df
    for kkey, val in kw.items():
        out = out[out[kkey] == val]
    return out

ANALYSES = [
    ("time_smd", "time_smd"),
    ("afterhours_smd", "afterhours_smd"),
    ("time_relative", "time_relative"),
    ("burnout_smd", "burnout_smd"),
    ("burnout_pfi_md", "burnout_pfi_md"),
    ("workload_smd", "workload_smd"),
    ("quality_smd", "quality_smd"),
    ("quality_pdqi_smd", "quality_pdqi_smd"),
    ("errors_any_logit", "errors_any_logit"),
]
for name, oc in ANALYSES:
    d = sub(sel, outcome=oc)
    run(f"{name}_all", d, f"{oc} all studies")
    run(f"{name}_controlled", sub(d, controlled="controlled"), f"{oc} controlled studies only")
    run(f"{name}_uncontrolled", sub(d, controlled="uncontrolled/other"), f"{oc} uncontrolled or other designs only")
    keep = d[~d.rob_overall.isin(["serious", "critical"])]
    run(f"{name}_lowrob", keep, f"{oc} excluding serious or critical risk of bias")
    run(f"{name}_journalonly", d[d.report_type.str.contains("journal article")], f"{oc} journal articles only (preprints removed)")

# Design split for the combined burnout set (continuous + binary sensitivity)
cont = sub(sel, outcome="burnout_smd")
binx = sub(sel, outcome="burnout_binary_smd")
both = pd.concat([cont, binx], ignore_index=True)
run("burnout_combined_all", both, "burnout SMD, continuous plus binary converted (sensitivity)")
run("burnout_combined_binaryonly", binx, "burnout SMD, binary measures converted only (sensitivity)")

# Subgroup pools and interaction tests
def interaction(name, df, column, groups):
    pools = {}
    for gname in groups:
        d = df[df[column] == gname]
        if len(d) >= 1:
            pools[gname] = (meta(d), len(d))
    RESULTS[name] = dict(label=f"interaction by {column}", pools={g: {kk: vv for kk, vv in m.items() if kk not in ('studies', 'records')} | {"k": kk} for g, (m, kk) in pools.items()})
    if len(pools) == 2:
        (g1, (m1, _)), (g2, (m2, _)) = list(pools.items())
        z = (m1["mu"] - m2["mu"]) / math.sqrt(m1["se_ci"]**2 + m2["se_ci"]**2)
        RESULTS[name]["test"] = dict(kind="Wald z on subgroup pooled estimates", stat=float(z), p=float(2 * (1 - stats.norm.cdf(abs(z)))), groups=[g1, g2])
    elif len(pools) > 2:
        mus = np.array([m["mu"] for m, _ in pools.values()]); ses = np.array([m["se_ci"] for m, _ in pools.values()])
        w = 1 / ses**2; grand = np.sum(w * mus) / np.sum(w)
        Qb = float(np.sum(w * (mus - grand)**2)); dfree = len(pools) - 1
        RESULTS[name]["test"] = dict(kind="Wald omnibus on subgroup pooled estimates", stat=Qb, df=dfree, p=float(1 - stats.chi2.cdf(Qb, dfree)), groups=list(pools.keys()))
    return pools

t = sub(sel, outcome="time_smd")
interaction("time_smd_by_design", t, "design_group", ["randomised", "non-randomised controlled", "before-after"])
interaction("time_smd_by_product", t, "product_group", ["Abridge", "DAX", "Other"])
interaction("time_smd_by_vendor", sub(t, vendor_class="vendor").append(sub(t, vendor_class="independent")) if False else t[t.vendor_class.isin(["vendor", "independent"])], "vendor_class", ["vendor", "independent"])
for pg in ["Abridge", "DAX", "Other"]:
    run(f"time_smd_leaveout_{pg}", t[t.product_group != pg], f"time SMD leaving out {pg}")
tr = sub(sel, outcome="time_relative")
interaction("time_relative_by_design", tr, "design_group", ["randomised", "non-randomised controlled", "before-after"])
ah = sub(sel, outcome="afterhours_smd")
interaction("afterhours_by_vendor", ah[ah.vendor_class.isin(["vendor", "independent"])], "vendor_class", ["vendor", "independent"])
run("afterhours_abridge", sub(ah, product_group="Abridge"), "after-hours SMD, Abridge studies only")
bs = sub(sel, outcome="burnout_smd")
interaction("burnout_by_design", bs, "design_group", ["randomised", "before-after"])
wl = sub(sel, outcome="workload_smd")
interaction("workload_by_design", wl, "design_group", ["randomised", "non-randomised controlled", "before-after"])
interaction("workload_by_vendor", wl[wl.vendor_class.isin(["vendor", "independent"])], "vendor_class", ["vendor", "independent"])
qs = sub(sel, outcome="quality_smd")
interaction("quality_by_vendor", qs[qs.vendor_class.isin(["vendor", "independent"])], "vendor_class", ["vendor", "independent"])

# Egger tests where k >= 10
for name, oc in [("time_smd", "time_smd"), ("time_relative", "time_relative")]:
    d = sub(sel, outcome=oc)
    if len(d) >= 10:
        RESULTS[f"egger_{name}"] = egger(d)

# Back-transform the error proportion pool
m = RESULTS["errors_any_logit_all"]
m["pooled_proportion"] = float(1 / (1 + math.exp(-m["mu"])))
m["prop_lo"] = float(1 / (1 + math.exp(-m["lo"]))); m["prop_hi"] = float(1 / (1 + math.exp(-m["hi"])))
if m["pi_lo"] is not None:
    m["prop_pi_lo"] = float(1 / (1 + math.exp(-m["pi_lo"]))); m["prop_pi_hi"] = float(1 / (1 + math.exp(-m["pi_hi"])))

# Study level error proportions with Wilson intervals (table, not pooled)
def wilson(x, n, z=1.959963984540054):
    p = x / n; den = 1 + z**2 / n
    cen = (p + z**2 / (2 * n)) / den
    half = z * math.sqrt(p * (1 - p) / n + z**2 / (4 * n**2)) / den
    return p, cen - half, cen + half
ERR_TABLE = []
for label, x, n, basis in [
    ("Taylor 2026, omissions, notes with at least one omission", 64, 356, "notes"),
    ("Taylor 2026, hallucinations, notes with at least one hallucination", 41, 356, "notes"),
    ("Taylor 2026, wrong inclusions, notes with at least one accidental inclusion", 33, 356, "notes"),
    ("Taylor 2026, serious errors, notes with an error rated severity 4 to 5", 19, 356, "notes"),
    ("Biro 2025, notes with at least one error", 31, 44, "notes"),
    ("De John 2026, notes with at least one clinically meaningful error", 24, 49, "notes"),
    ("Bergman 2026, notes with at least one Critical+High error, clinician adjudication (AI notes)", 24, 385, "notes"),
    ("Bergman 2026, notes with at least one Critical+High error, calibrated automated reviewer (AI notes)", 94, 385, "notes"),
    ("Menz 2026, omission errors as a share of data points", 10, 2160, "data points"),
    ("Menz 2026, incorrect data points, all types", 46, 2160, "data points"),
]:
    p, lo, hi = wilson(x, n)
    ERR_TABLE.append(dict(label=label, events=x, n=n, basis=basis, proportion=p, lo=lo, hi=hi))
RESULTS["error_proportions_table"] = ERR_TABLE

with open(os.path.join(OUT, "analysis-results.json"), "w") as f:
    json.dump(RESULTS, f, indent=2, default=str)

# ---------------- Forest plots --------------------------------------------
def forest(df, title, xlabel, fname, pooled_names):
    d = df.sort_values("yi")
    fig_h = max(3.2, 0.42 * (len(d) + len(pooled_names) + 2))
    fig, ax = plt.subplots(figsize=(9.2, fig_h))
    ypos = list(range(len(d) + len(pooled_names)))[::-1]
    labels, ys, xs, los, his, is_pool = [], [], [], [], [], []
    for (_, r), y in zip(d.iterrows(), ypos[:len(d)]):
        labels.append(f"{r.study} ({r.record_id})"); ys.append(y); xs.append(r.yi)
        los.append(r.yi - 1.96 * r.sei); his.append(r.yi + 1.96 * r.sei); is_pool.append(False)
    for j, (nm, m) in enumerate(pooled_names):
        y = ypos[len(d) + j]
        labels.append(nm); ys.append(y); xs.append(m["mu"]); los.append(m["lo"]); his.append(m["hi"]); is_pool.append(True)
    for y, x, lo, hi, pool in zip(ys, xs, los, his, is_pool):
        if pool:
            ax.fill([lo, x, hi, x], [y, y + 0.28, y, y - 0.28], color="#333333")
        else:
            ax.plot([lo, hi], [y, y], color="#666666", lw=1.2)
            ax.plot([x], [y], marker="s", color="#1a5276", ms=5)
    ax.axvline(0, color="#999999", lw=0.8, ls="--")
    ax.set_yticks(ys); ax.set_yticklabels(labels, fontsize=8)
    ax.set_xlabel(xlabel, fontsize=9); ax.set_title(title, fontsize=10, loc="left")
    ax.tick_params(axis="x", labelsize=8)
    for s in ["top", "right", "left"]:
        ax.spines[s].set_visible(False)
    fig.tight_layout(); fig.savefig(os.path.join(OUT, fname), dpi=200); plt.close(fig)

forest(sub(sel, outcome="time_smd"), "Documentation time (SMD, negative favours the scribe)",
       "Standardised mean difference", "forest-time-smd.png",
       [("Pooled, controlled studies", RESULTS["time_smd_controlled"]),
        ("Pooled, uncontrolled before-after", RESULTS["time_smd_uncontrolled"]),
        ("Pooled, all studies (sensitivity)", RESULTS["time_smd_all"])])
forest(sub(sel, outcome="time_relative"), "Documentation time, relative change (percent)",
       "Change in documentation time (%)", "forest-time-relative.png",
       [("Pooled, all studies", RESULTS["time_relative_all"])])
forest(sub(sel, outcome="afterhours_smd"), "After-hours documentation time (SMD, negative favours the scribe)",
       "Standardised mean difference", "forest-afterhours-smd.png",
       [("Pooled, uncontrolled before-after (all poolable studies)", RESULTS["afterhours_smd_all"])])
forest(sub(sel, outcome="burnout_smd"), "Burnout and work exhaustion (SMD, negative favours the scribe)",
       "Standardised mean difference", "forest-burnout-smd.png",
       [("Pooled, controlled trials", RESULTS["burnout_smd_controlled"]),
        ("Pooled, all studies", RESULTS["burnout_smd_all"])])
forest(sub(sel, outcome="workload_smd"), "Workload and task load (SMD, negative favours the scribe)",
       "Standardised mean difference", "forest-workload-smd.png",
       [("Pooled, all studies", RESULTS["workload_smd_all"])])
forest(sub(sel, outcome="quality_smd"), "Note quality (SMD, positive favours the scribe)",
       "Standardised mean difference", "forest-quality-smd.png",
       [("Pooled, all studies", RESULTS["quality_smd_all"]),
        ("Pooled, PDQI family only", RESULTS["quality_pdqi_smd_all"])])
# Error proportion forest (proportion scale)
d = sub(sel, outcome="errors_any_logit")
fig, ax = plt.subplots(figsize=(9.2, 3.4))
props = []
for _, r in d.iterrows():
    p = 1 / (1 + math.exp(-r.yi)); lo = 1 / (1 + math.exp(-(r.yi - 1.96 * r.sei))); hi = 1 / (1 + math.exp(-(r.yi + 1.96 * r.sei)))
    props.append((r.study, p, lo, hi))
m = RESULTS["errors_any_logit_all"]
props.append(("Pooled", m["pooled_proportion"], m["prop_lo"], m["prop_hi"]))
ys = list(range(len(props)))[::-1]
for (lab, p, lo, hi), y in zip(props, ys):
    if lab == "Pooled":
        ax.fill([lo, p, hi, p], [y, y + 0.28, y, y - 0.28], color="#333333")
    else:
        ax.plot([lo, hi], [y, y], color="#666666", lw=1.2); ax.plot([p], [y], marker="s", color="#7b241c", ms=5)
ax.set_yticks(ys); ax.set_yticklabels([p[0] for p in props], fontsize=8)
ax.set_xlim(0, 1); ax.set_xlabel("Proportion of notes with at least one error (study definitions)", fontsize=9)
ax.set_title("Notes with at least one error", fontsize=10, loc="left")
for s in ["top", "right", "left"]:
    ax.spines[s].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, "forest-errors-any.png"), dpi=200); plt.close(fig)

# Funnel plot, primary time SMD (k = 13)
d = sub(sel, outcome="time_smd")
fig, ax = plt.subplots(figsize=(6.4, 5.2))
mu = RESULTS["time_smd_all"]["mu"]
ax.scatter(d.yi, d.sei, color="#1a5276")
ax.axvline(mu, color="#333333", lw=1)
se_grid = np.linspace(0, max(d.sei) * 1.15, 50)
ax.plot(mu - 1.96 * se_grid, se_grid, color="#999999", ls="--", lw=0.9)
ax.plot(mu + 1.96 * se_grid, se_grid, color="#999999", ls="--", lw=0.9)
ax.invert_yaxis(); ax.set_xlabel("Documentation time, SMD"); ax.set_ylabel("Standard error")
ax.set_title("Funnel plot, documentation time (SMD), all studies", fontsize=10, loc="left")
fig.tight_layout(); fig.savefig(os.path.join(OUT, "funnel-time-smd.png"), dpi=200); plt.close(fig)

print(json.dumps({k: {kk: vv for kk, vv in v.items() if kk in ("k", "n_units", "mu", "lo", "hi", "I2", "tau2", "p", "pooled_proportion", "prop_lo", "prop_hi")} for k, v in RESULTS.items() if isinstance(v, dict) and "mu" in v}, indent=1))
