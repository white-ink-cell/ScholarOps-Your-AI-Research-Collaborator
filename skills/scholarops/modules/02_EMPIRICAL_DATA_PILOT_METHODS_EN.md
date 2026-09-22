# 02 — Empirical Data, Pilot, Screen & Formal Methods


## A. Empirical execution class and entry

## EMP-GATE00 — Empirical Execution Class / Risk Trigger Router
Record one execution class before empirical work:

```text
EMPIRICAL_EXECUTION_CLASS =
TECHNICAL_PROBE
PREOUTCOME_MEASUREMENT_VALIDATION
OUTCOME_DECISION_SCREEN
FORMAL_STUDY
```

### TECHNICAL_PROBE
Prefer synthetic, dummy, or non-candidate inputs. Validate only technical matters such as API/schema/parser/file/identifier/rate-limit behavior. A technical probe does not advance the research state machine, does not require Freeze A, economic thresholds, multiplicity treatment, or B3 effect-open status, and does not produce a `SCREEN_VERDICT`.

### PREOUTCOME_MEASUREMENT_VALIDATION
This is a feasibility/measurement pilot in ScholarOps. Candidate observations may be used, but the research effect remains masked at B0–B2. It belongs to the measurement-validation stage and does not generate a screen verdict. The pilot/feasibility rationale is adapted from feasibility-study guidance; the finance/business workflow remains a ScholarOps adaptation rather than a direct clinical-trial prescription.

### OUTCOME_DECISION_SCREEN
This is an optional effect-open resource-allocation screen, not a mandatory step. Its sole purpose is to decide whether further research effort should be allocated under prespecified progression criteria. It requires the screen-data reuse policy and progression criteria to be frozen before B3. It may produce `SCREEN_STATUS` and `SCREEN_VERDICT`, but it does not establish that an economic effect is absent.

### FORMAL_STUDY
Formal confirmatory/economic inference begins only after the formal main specification is frozen. Equivalence, minimum-effect, and economic-null claims belong here, not in a small outcome screen.

Risk gates are activated only when their substantive trigger is present. Examples include economic-threshold, within-study multiplicity, specification-search, screen-reuse, missing-data, influence-audit, and post-clean QA gates. An untriggered gate is `NOT_APPLICABLE`; do not generate empty artifacts merely to show that the gate exists.

## EMP-ENTRY01 — Empirical entry anchor before results
A pipeline is ineffective if entry into the pipeline is not enforced.

Before producing any estimate that could be read as a research result—such as a coefficient, test statistic, portfolio return, Sharpe ratio, model-performance metric, or event-window effect—record:

```text
EMPIRICAL_ENTRY_STATUS =
RESOLVED / UNRESOLVED_BLOCKED / USER_OVERRIDE_EXPLORATORY / NOT_APPLICABLE
```

A resolved entry anchor is one short record, not a new audit package:
`current state / last upstream state supported by an artifact / supporting artifact`.
The cost of this rule must remain small.

If the upstream state is claimed as complete but no artifact supports it, set `UNRESOLVED_BLOCKED` and return to the earliest missing state rather than “running one version to see what happens.”

Data description and blind distribution review precede cleaning; cleaning/transform rules must be frozen before estimation. A user's request to “run the regression” does not implicitly waive upstream state requirements.

If the user explicitly asks to skip required upstream steps, the work may proceed only as `USER_OVERRIDE_EXPLORATORY`, with the skipped states documented, all resulting outputs marked exploratory, and any opened effect recorded in the Seen Data Register.

Pure code debugging, data-dictionary lookup, method discussion, or literature work that produces no research estimate is `NOT_APPLICABLE`.

## B. Execution responsibility and research code

## EMP-EXEC01 — Assistant-first execution
When the host environment can access the required user-provided data and execute the needed operations, the agent should directly perform:
`QA / cleaning / merge / variable construction / descriptive statistics / panel build / validation / code execution / result packaging`.

Ask the user to perform only the minimum acquisition step that is genuinely blocked by a private account, institutional login, paid entitlement, local-only resource, CAPTCHA, or unavailable connector.

Before asking for a redownload or rerun, inspect available attachments, persistent project assets, data registries, caches, manifests, and hashes where the host permits access.

## EMP-EXEC02 — Research code minimalism
Use the execution environment that is actually available. Do not install packages, create broad compatibility layers, or mutate the user's environment unless the task genuinely requires it and the user or host policy permits it.

Avoid:
- unnecessary automatic package installation;
- multiple speculative import fallbacks;
- broad `except Exception: pass` handling;
- silent field guessing;
- converting missing values to zero without a construct-based rule;
- large compatibility branches for hypothetical schemas that have not been observed.

Prefer:
`explicit schema / dtype checks / hashes where relevant / assertions / fail-fast behavior / minimal repair after a real error is observed`.

## C. Data asset intake

## EMP-ASSET01 — Existing asset first
For each reusable data asset, record as needed:
`DATA_ASSET_ID / source / version / time coverage / unit / fields / canonical or reference location / hash or identity evidence / acquisition provenance / reuse eligibility`.

Do not redownload merely because the agent forgot that an existing verified asset is available.

## EMP-ASSET02 — Acquisition scope follows estimand
Define the required:
`unit / target / frequency / dates / windows / fields / matching dependencies`
before acquisition.
“Download as much as possible first” is not the default strategy.

## D. Concrete-data escalation and raw-to-clean pipeline

## EMP-DATA00 — Concrete-data escalation
This module supplies a general empirical skeleton, not a universal formula for every special dataset.

If the project has special data structure, missingness, institutional semantics, ratio construction, human-AI data, event sampling, clustering, or interference that the module does not explicitly cover, set:
`CONCRETE_PROBLEM_SPECIAL_CASE=YES`.
Then invoke `CORE-M01/M02`: inspect the actual data and professional precedent, map assumptions, and freeze a project-specific rule. Do not invent data semantics or mechanically extrapolate a generic textbook recipe.

## EMP-DATA01 — Raw Structural QA
At the raw-data stage, correct data-identity and encoding problems without outcome-driven tail surgery.
Check as relevant:
- file identity and hash;
- schema and dtypes;
- date range;
- primary keys and duplicates;
- special missing codes;
- units, sign conventions, and currency;
- impossible values;
- source seams;
- identifier/link validity;
- vendor-specific adjustment and corporate-action semantics.

Field semantics require the official data dictionary or transition guide when one exists. A textbook cannot substitute for vendor-specific semantics.
Record `RAW_DATA_QA_STATUS`.

## EMP-DATA02 — Construct-first variable definition
Variable formulas are determined by the economic construct and credible precedent, not by whichever field is easiest to download.
For ratios, liquidity, turnover, volatility, text measures, and similar constructs, preserve:
`raw components / denominator / unit / aggregation rule / point-in-time logic`.

## EMP-DATA03 — Derived Variable Construction
Use the canonical state:
`DERIVED_VARIABLE_CONSTRUCTION_STATUS`
with sub-statuses such as:

```text
COVARIATE_CONSTRUCTION_STATUS
EXPOSURE_CONSTRUCTION_STATUS
OUTCOME_CONSTRUCTION_STATUS
```

Construct variables from the frozen economic definition before the full distribution/tail review. This replaces ambiguous labels such as “pretreatment variable construction” when the rule applies more broadly.

## EMP-DATA04 — Two-end QA sandwich
Use the sequence:

```text
Raw Structural QA
↓
construct-defined derived variables
↓
Blind Distribution / Tail / Missingness Audit
↓
cleaning / transformation decision
↓
rebuild clean data
↓
post-clean QA
```

Do not allow raw errors to propagate unchecked, and do not winsorize or transform a final construct before the construct has actually been built.

## EMP-DATA05 — Blind Distribution / Tail Audit
Without opening the treatment effect, inspect at least the relevant distributional diagnostics, including sample size, missingness, zeros, central tendency, dispersion, robust dispersion, skewness, kurtosis, extrema, and sufficiently detailed tail quantiles for the context.

Where useful, inspect stability over time or legitimate sample dimensions that do not reveal the treatment effect.
For abnormal constructed values, perform an `EXTREME_OBSERVATION_TRACE` back to the underlying raw components and event/entity identity.

## EMP-DATA06 — Outlier taxonomy / distributional tail

Classify extreme observations first at the variable/data layer:

```text
INVALID_CODE_OR_SENTINEL
UNIT_OR_SCALE_ERROR
DUPLICATE_OR_LINK_ERROR
INVALID_DENOMINATOR
CORPORATE_ACTION_OR_MECHANICAL_BREAK
TRUE_ECONOMIC_TAIL
UNKNOWN_REQUIRES_REVIEW
```

Correct verified data errors. Preserve a raw archive for genuine economic tails and decide any transformation or tail treatment from construct identity, vendor semantics, blind distributional evidence, and the eventual estimator.

Do not conflate this layer with regression influence. A value can be economically extreme without dominating an estimate, and an observation can be influential without being an invalid data point.

Bali, Engle, and Murray (2016, §1.2) document winsorization and truncation as common practices in empirical asset pricing while describing this style of tail handling as comparatively ad hoc. Their discussion supports the statement that such treatments are conventions, not a proof that a fixed cutoff is correct. It does not establish 1/99, 0.5/99.5, or any other universal cutoff.

Where influence on an estimator is the actual concern, use the influence-diagnostic layer (`EMP-INFL01`) rather than treating winsorization/truncation as an automatic influence solution.

Therefore:

```text
winsorization/truncation != influence diagnosis
common practice != project-specific justification
```

Any cutoff or transform must be justified for the current construct and design rather than solely by citation to common practice.

## EMP-DATA07 — Cleaning / Transformation / Scale Decision
A cleaning or transformation decision should jointly consider:
1. construct identity;
2. canonical variable literature;
3. vendor semantics;
4. treatment-blind distributional evidence;
5. tail/influence diagnosis at the appropriate stage;
6. the needs and assumptions of the eventual estimator.

Different variables may require different handling. Do not force all outcomes to use the same winsorization rate, log transform, or pooled scale merely for cosmetic uniformity.

## EMP-DATA08 — Post-clean QA: change-triggered
Record:

```text
CLEAN_DATA_CHANGE_STATUS =
NO_DATA_CHANGE
VALUES_CHANGED
SAMPLE_CHANGED
TRANSFORMATION_CHANGED
AGGREGATION_CHANGED
MULTIPLE_CHANGES
```

If the blind audit leads to no deletion, value modification, transformation, or aggregation change, do not rerun a full second descriptive audit merely for ritual symmetry. Confirm input/output identity, row/entity counts, schema, and key coverage.

If values, sample, transformation, or aggregation actually changed, rerun the affected distribution, missingness, tail, balance, correlation, support, and panel-cell checks needed to validate the changed data.
If the change creates a new discontinuity, sample collapse, or construct drift, return to `EMP-DATA07`.

Principle: the second QA validates actual changes; it is not a mandatory duplicate computation.

## EMP-DATA08A — Missing Data Cheap Triage
Before opening the full missing-data gate, run a low-cost triage on key variables:
`missing count / missing rate / always-missing entities / mechanically required history missingness / linkage missingness`.

If missingness is absent, purely mechanical and outside the target sample by design, or clearly unable to change the estimand, sample composition, or key construct, record:

```text
MISSING_DATA_STATUS=NOT_APPLICABLE
MISSING_FULL_AUDIT_TRIGGER=NO
```

and keep only the short triage result.

If there is non-mechanical missingness, entity/time blocks, linkage/source gaps, material complete-case selection, or a need for imputation, set `MISSING_FULL_AUDIT_TRIGGER=YES` and enter `EMP-DATA09`.

## EMP-DATA09 — Missing-data reality / selection / imputation gate

Missingness is not summarized by a single percentage. When the full missing-data gate is triggered, create a `MISSING_DATA_MAP` that distinguishes, where relevant:

```text
MECHANICAL_HISTORY_REQUIRED
ENTRY_OR_NOT_YET_ELIGIBLE
EXIT_OR_TERMINAL_MISSING
MID_SAMPLE_BLOCK
SOURCE_NOT_REPORTED
LINKAGE_FAILURE
NOT_APPLICABLE
OTHER_STRUCTURAL
UNKNOWN
```

For each key variable, audit at least the observation-level missing rate, entity-level ever/always missingness, time pattern, observable differences in missingness, complete-case sample loss, economically weighted loss when relevant, and changes in sample composition.

Little and Rubin (2020, 3rd ed., §3.2) establish the core boundary: validity of complete-case analysis depends jointly on the missingness mechanism and the estimand. In their examples, complete-case estimation of a mean can be biased when complete and incomplete units have different means, while regression coefficients can remain unbiased under some selection patterns that depend on covariates but not on the outcome conditional on those covariates. Missing-data validity is therefore **estimand-specific**, not a fixed property of a dataset.

Little and Rubin (2020, Chs. 4–5) also distinguish single imputation from methods that account for missing-data uncertainty. Their 3rd edition describes multiple-imputation standard errors as approximately valid under broad classes of imputation procedures, while special single-filled-data corrections lack comparable generality. ScholarOps therefore must not treat any single imputation recipe as a universal default.

Record:

```text
MISSING_DATA_STATUS =
PASS / CONDITIONAL / BLOCKED / NOT_APPLICABLE
```

Generic missing-data principles govern the Core workflow. Domain-specific finance evidence, such as systematic missingness in firm-characteristic panels, may strengthen the case for a particular finance application but must not be generalized beyond its transfer scope.

`DROP_ALL_MISSING`, complete-case analysis, zero imputation, median imputation, and industry-median imputation are not universally safe or universally invalid. Their admissibility must be justified against the current mechanism, estimand, timing, and downstream analysis.

## EMP-DATA09A — Imputation decision

If missingness is irrelevant to the estimand and a justified complete-case design does not change the target population, `IMPUTATION_DECISION=NO_IMPUTATION` is allowed, but the selection audit remains required.

If imputation is required, freeze at least:

```text
IMPUTATION_TARGET
INFORMATION_SET_AT_T
LOOKAHEAD_ALLOWED = NO / DIAGNOSTIC_ONLY
MODEL_FAMILY
FALLBACK_RULE
MASKING_VALIDATION_DESIGN
DOWNSTREAM_ESTIMAND_VALIDATION
```

For point-in-time pretreatment variables, future information is not allowed in the formal imputation. Future information may be used only for a clearly labeled diagnostic upper bound.

This field set is a ScholarOps governance implementation derived from the missing-data principles; it is not a verbatim prescription from Little and Rubin.

## EMP-DATA09B — Imputation validation

Do not validate an imputation model only by randomly masking values under an artificial MCAR design when the real missingness is structured. Where feasible, mimic the observed missingness process using block missingness, entry/exit patterns, observable-characteristic-dependent masking, empirical propensity masking, or documented source gaps.

Validate at the level relevant to the study:
1. value-level error, such as RMSE or MAE;
2. ranking/quantile recovery when the study depends on ranks;
3. **downstream estimand distortion**.

The third item must be defined for the current project, for example:

```text
DID            -> treatment effect, pre-trends, sample composition
Event study    -> abnormal response and event aggregation
Asset pricing  -> risk premium and portfolio-sort implications
Forecasting    -> out-of-sample loss and ranking
```

A good imputation prediction metric does not by itself establish low distortion in the downstream estimand.

The masking design, validation outcomes, and any transfer from an external missing-data method must be recorded with its assumptions and scope.

## EMP-DATA09F — Finance firm-characteristic special case
Bryzgalova, Lerner, Lettau, and Pelger study systematic missingness in panels of firm characteristics in asset-pricing applications, including implications for risk premia, cross-sectional anomalies, and portfolio construction. This provides strong domain-specific evidence that missing firm-characteristic data can be systematic and that complete-characteristic requirements can induce material selection.

The transfer scope is therefore limited to finance firm-characteristic panels. It is not a universal authority for arbitrary missing-data problems. Outside that setting, record `PRECEDENT_TRANSFER_STATUS=TRANSFERABLE_WITH_ADAPTATION` and explicitly map assumptions under `CORE-M01`.

The official RFS bibliographic identity for this source uses DOI `10.1093/rfs/hhae036`.

## E. Blind-analysis boundary

## EMP-BLIND01 — Four-level data-access firewall
Use four access levels:

### B0 — `STRUCTURE_ONLY`
Allowed: schema, identifiers, dates, coverage, units, missing codes, raw components, and support counts. Research outcome values need not be opened.

### B1 — `MARGINAL_OUTCOME_BLIND`
Allowed for data reality: the marginal or otherwise legally prespecified distribution of the outcome itself, tails, denominators, missingness, and univariate extreme-value tracing.
Treatment, event, exposure, or hypothesis-group identity must be masked or not joined, and no grouping may reveal recoverable effect direction.

B1 does not include regression influence diagnostics. Cook's distance, DFFITS, DFBETA, leverage, or robust-regression weights depend on a fitted outcome model and belong after B3 under `EMP-INFL01`.

### B2 — `DESIGN_SUPPORT_EFFECT_MASKED`
Allowed: design-support structure such as exposure/treatment support, overlap, usable-sample counts, matching quality, and counts of independent variation units, while the joint outcome-treatment/exposure relationship remains hidden.
Different designs implement B2 differently; ScholarOps does not require an event-study template.

### B3 — `EFFECT_OPEN`
First level at which the workflow may reveal the joint outcome-treatment/exposure relation, treatment-group outcome summaries, event-time outcome plots, outcome-exposure associations, or formal effect estimates/tests.

`BLINDNESS_LEVEL` must use the controlled values:
`B0_STRUCTURE_ONLY / B1_MARGINAL_OUTCOME_BLIND / B2_DESIGN_SUPPORT_EFFECT_MASKED / B3_EFFECT_OPEN`.

The general principle is supported by blind-analysis literature: when discretionary analysis choices remain, the analyst should avoid knowing the answer the analysis is intended to determine. ScholarOps' four-level firewall is its own workflow implementation, not a published taxonomy.

## EMP-BLIND01A — Blinding is a principle, not an event-study template
Blind analysis is a bias-control principle: while discretionary analysis choices remain, avoid revealing the study answer in a form that can steer those choices. It does not require an event calendar.

Klein and Roodman describe multiple families of blind-analysis strategies rather than one mandatory implementation. ScholarOps therefore records the project-specific implementation using a controlled field such as:

```text
BLINDING_IMPLEMENTATION_MODE =
TREATMENT_LABEL_MASKED
OUTCOME_MASKED
SHUFFLED_LABEL
SYNTHETIC_OUTCOME
HOLDOUT
LOCKED_SPEC_ONLY
NOT_FEASIBLE
```

`NOT_FEASIBLE` is allowed, but the reason must be documented and the claim or procedural protection adjusted accordingly; `LOCKED_SPEC_ONLY` may be used when the specification can be frozen before effect inspection even if stronger masking is infeasible.

Blinding is not proof of correctness. Analysis may continue after unblinding, but decisions first made after the effect is seen must be recorded as post-effect decisions and feed the Seen Data and Claim Drift governance.

## EMP-BLIND01B — Background familiarity ≠ effect-open
Track separately:

```text
BACKGROUND_DATA_FAMILIARITY =
NONE / GENERAL_DISTRIBUTIONAL / EXTENSIVE_PRIOR_USE
```

and

```text
SEEN_DATA_STATUS =
NONE / BLIND_DIAGNOSTIC_ONLY / EFFECT_SEEN / UNKNOWN
```

Knowing the typical distribution of a familiar finance variable is background familiarity, not automatically a blindness failure. Blindness concerns the current study answer, not whether the researcher has ever seen the variable before.
Only observation of the current study's joint outcome-treatment/exposure relation creates `EFFECT_SEEN`.
Extensive prior use increases the value of stronger prespecification or `LOCKED_SPEC_ONLY`; it does not itself block the study.

## EMP-BLIND02 — Forbidden leakage before B3
Before B3, treat the following as effect-open even if no regression has been run:
- treated-versus-control outcome summaries;
- outcome paths around the event;
- event-time-aligned outcome plots;
- outcome summaries by high/low exposure;
- comparing winsorization/log/scale variants by which produces a more favorable event difference;
- changing cleaning, sample, window, or threshold because of coefficient sign or significance.

## EMP-BLIND02A — Analyst-coding blindness

Polit (2011) documents that analysts make consequential discretionary choices during data analysis, including missing-data handling, outlier/distributional handling, transformations, variable recoding and cutpoints, subgroup analyses, covariate selection, repeated-outcome/endpoint choices, and sensitivity/validity analyses. The paper argues that treatment-code knowledge can influence these choices.

ScholarOps transfers the underlying principle beyond the paper's RCT setting with explicit adaptation: where an empirical design contains treatment/exposure identities and material analytic discretion remains at B1/B2, separate the analyst from the semantic identity of the groups whenever feasible.

Operationally:
- if group identifiers are required in scripts, prefer random or semantically neutral coding;
- keep the real treatment/exposure mapping separate;
- decode only after the primary analysis choices governed by the blind phase are frozen;
- if group identity is unnecessary for B1/B2 work, do not join it merely for convenience.

This rule does **not** claim that every finance design is an RCT or that Polit directly studied finance. It transfers the narrower bias-control principle: separate discretionary analytic choices from knowledge of the comparison identity when that knowledge can change those choices.

## EMP-BLIND03 — Already-seen data
If an outcome/effect was seen in a prior pilot, conversation, report, or analysis, do not pretend to regain blindness.
Record:

```text
SEEN_DATA_STATUS =
NONE
BLIND_DIAGNOSTIC_ONLY
EFFECT_SEEN
UNKNOWN
```

`BLIND_DIAGNOSTIC_ONLY` means only diagnostics permitted under the blind boundary were viewed. `EFFECT_SEEN` means any effect information forbidden before B3 was observed.
The Seen Data registry schema is governed centrally rather than redefined here.

Legitimate remedies may include a holdout, new events, a new sample, masking, or blind diagnostics generated by an independent data manager. Forgetting or renaming prior results is not a remedy.

## F. Aggregation, sample, and measurement support

## EMP-PANEL01 — Aggregation is part of measurement
Before converting daily/high-frequency data into weekly, monthly, or event-level panels, freeze decisions about:
`zero vs missing / non-trading, halt, and holiday treatment / partial periods / minimum valid observations / sum vs mean vs median vs compounding / overlapping stock-week or event windows / numerator-denominator timing / generated-regressor leakage / within-between variation / fixed-effect support / residual dependence and cluster unit`.

Aggregation is part of construct measurement, not a neutral file-formatting step.

## EMP-PANEL02 — Effective information is not raw row count

Do not treat a large raw row count as equivalent to a large number of independent information units.

Wooldridge's cluster-sampling discussion shows why inference can be driven by the number of independent clusters rather than the number of observations inside clusters, especially when key variation is cluster-level and the number of clusters is small. Hasbrouck likewise notes that microstructure datasets can contain very many observations while spanning only days or months, and that standard asymptotic approximations still rely on appropriate model specification.

Record the study's `INDEPENDENT_VARIATION_UNIT`, such as:

```text
event / cluster / firm / date / provider / shock
```

Also report the corresponding counts needed to evaluate the design. Do not use millions of high-frequency rows to justify conventional cluster asymptotics when the identifying variation comes from a small number of events, dates, providers, or clusters.

This rule is about effective independent variation and dependence structure, not a universal minimum cluster count.

## EMP-SAMPLE01 — Four execution sample concepts
### TECHNICAL_PROBE_SAMPLE
Use the smallest heterogeneous sample needed to expose technical problems in schema/API/parser/file/identifier behavior. Do not run research-power calculations for this sample.

### PREOUTCOME_MEASUREMENT_VALIDATION_SAMPLE
Choose sample size around the precision needed for coverage, classification, error, missingness, or gold-label accuracy, accounting for rare classes and material heterogeneity. Do not use a few convenient cases merely because they are easy to inspect.

### OUTCOME_DECISION_SCREEN_DECISION_SAMPLE
Design the sample around the prespecified progression/resource-allocation criterion and the precision needed to make that screen decision. A screen criterion may be economically motivated, but it is not a formal `ECONOMIC_MINIMUM`, SESOI, equivalence bound, or economic-null test. Formal economic-magnitude adjudication belongs to `FORMAL_STUDY`. Do not import a formal SESOI merely to make a resource screen look confirmatory.

### FORMAL_STUDY_SAMPLE
Use formal power, precision, or inference logic. If the event universe is fixed, report attainable precision, MDE, or power rather than pretending that N is freely chosen.

## EMP-SAMPLE02 — No rule-of-thumb N
There is no universal pilot sample size such as 12, 30, 40, or 100. Pilot/feasibility sample-size rationale must match the pilot objective.

For `PREOUTCOME_MEASUREMENT_VALIDATION`, justify N around the measurement target. For `OUTCOME_DECISION_SCREEN`, justify N around the prespecified progression criterion. Neither should use effect significance as a stop rule merely to imitate a formal study.

## EMP-SAMPLE03 — Event-study / finance-specific calibration

For event-study designs, sample adequacy and power depend jointly on the effect magnitude, abnormal-return variance, number of event observations, event timing, and sampling interval.

Campbell, Lo, and MacKinlay (1997, Ch. 4) show that event-study power changes with effect size, variance, and sample size. They also show that, when event timing is precise, using a shorter sampling interval can improve power by reducing abnormal-return variance without mechanically increasing the effect. When event timing is uncertain, a wider event window may be required. Intraday designs introduce additional microstructure complications rather than delivering a free precision gain.

Accordingly, an event-study pilot or formal design should justify sample/precision using blind empirical variance, a canonical event-study calculation, or simulation under the frozen design. Do not determine adequacy from the stock count alone.

## EMP-SAMPLE04 — Cluster/event count

When identifying variation occurs at an event, provider, date, treatment-shock, or cluster level, effective information is constrained by the number and structure of those independent units.

Wooldridge's small-G discussion warns that conventional cluster-robust asymptotics can be poorly justified when the number of clusters is small even if within-cluster sample size is large. Hasbrouck's microstructure discussion similarly separates large observation counts from short calendar span and model-specification risk.

Whenever this issue is material, the screen/formal sample table should report the relevant dimensions rather than only raw N:

```text
raw rows / firms / dates / events / treatment shocks / clusters
```

Do not convert this rule into an arbitrary universal cluster-count cutoff; the appropriate inference must be justified for the actual dependence structure.

## EMP-SAMPLE05 — Required artifact
When sample size or precision can change an execution decision, create an execution-sample/precision justification containing at least:
- empirical execution class;
- objective;
- target estimand or feasibility parameter;
- independent variation unit;
- precision target appropriate to that objective;
- variance/source when relevant;
- N/events/clusters;
- analytical or simulation method when relevant;
- constraints;
- why the sample is sufficient for the stated objective.

For `OUTCOME_DECISION_SCREEN`, record the prespecified progression/resource criterion and the operating characteristics needed to make that resource-allocation decision. A formal `ECONOMIC_MINIMUM`, SESOI, equivalence bound, or economic-null operating characteristic is required only when `FORMAL_STUDY` actually adjudicates economic magnitude. Do not attach an irrelevant SESOI to a technical probe, measurement validation, or resource screen for appearance's sake.

## G. Failure, repair, and identification

## EMP-FAIL01 — Failure classification
Use one controlled `FAILURE_CLASS` taxonomy.

### Project-level conceptual
`NOVELTY_OR_REDUNDANCY`
`SO_WHAT_OR_CONCEPTUAL`
These can terminate a branch before a pilot.

### Execution/input
`ACCESS / IMPLEMENTATION / DATA_IDENTITY / DATA_QUALITY`
These do not, by themselves, justify an economic verdict.

### Measurement/support
`MEASUREMENT / SAMPLE_SUPPORT_OR_PRECISION / CONSTRUCT`
Diagnose measurement or precision first. A construct-changing repair requires refreezing or a new branch.

### Design/inference
`IDENTIFICATION / ESTIMATOR_OR_INFERENCE`
These are not economic nulls.

### Economic
`ECONOMIC_CRITERION`
An economic stop is allowed only when all upstream layers satisfy the requirements frozen for the relevant formal decision.

## EMP-FAIL02 — Mandatory diagnosis / evidence proportional to failure layer
For an anomalous, sparse, unstable, or adverse pilot result, create a `PILOT_FAILURE_DIAGNOSIS` in this order:
1. reproduce the failure;
2. locate the failure layer;
3. build the cause tree;
4. run the decisive diagnostic;
5. identify legal repair paths;
6. audit Seen Data and Claim Drift;
7. issue the verdict.

Match evidence to the failure layer:
- ACCESS → entitlement/subscription/vendor/user-verified access evidence;
- IMPLEMENTATION/DATA_IDENTITY/DATA_QUALITY → code, logs, schema tests, hashes, vendor dictionaries, technical documentation;
- MEASUREMENT/CONSTRUCT → canonical construct literature, high-quality applications, and data/vendor semantics under `CORE-M01`;
- IDENTIFICATION/ESTIMATOR_OR_INFERENCE/SAMPLE_SUPPORT_OR_PRECISION → econometric/method sources and design-specific applications when method assumptions are genuinely at issue;
- ECONOMIC_CRITERION → first determine the execution class. For `OUTCOME_DECISION_SCREEN`, check the frozen progression/resource criterion only; a screen stop is a resource-allocation decision, not an economic-null conclusion. For `FORMAL_STUDY`, check the Freeze-B economic threshold/decision rule first, with additional method literature only if the threshold method itself is disputed.

Do not turn every parser or schema bug into a literature review. If a technical repair reveals a new construct problem, then escalate to the construct layer.

## EMP-REPAIR01 — Repair legality
Allowed repairs include independently demonstrated implementation bugs, unit/schema/timestamp/linkage errors, and other prespecified construct-preserving repairs.

A new freeze or branch is required when the core sample frame, outcome, treatment, estimand, measurement construct, or identification changes.
Do not change the window, threshold, transformation, sample, or outcome merely because the sign or significance is inconvenient.

## EMP-ID01 — Pre-Pilot Identification Minimum
Before Freeze A, the design must be specific enough to interpret the pilot:
`estimand / treatment / control / counterfactual / timing / sampling frame / interference / main identifying assumptions / strongest rival / discriminating evidence / expected failure modes / inference unit`.

Do not wait until pilot results are visible to decide the core identification design or cluster dimension.

## EMP-ID02 — Formal Identification Strengthening
After a pilot, strengthen the design only within the same core estimand and identification logic—for example through fuller benchmarks, prespecified alternative counterfactuals, formal FE/inference, few-cluster/event procedures, placebos, falsification, robustness, or sensitivity.

If the pilot forces a different core counterfactual or identification strategy, set `CLAIM_DRIFT=YES` and return for refreezing or create a new branch. Do not search post-result for a different identification strategy that happens to deliver a preferred answer.

Use `FORMAL_IDENTIFICATION_STATUS=PASS` only when the formal strengthening remains within the same core identification logic. A changed core identification requires `RETURN_FOR_REFREEZE`.

## EMP-INFL01 — Regression Influence Audit
Influence analysis is effect-open and belongs after B3 because it depends on regression residuals, leverage, weights, or the candidate outcome. It is not the same as B1 univariate tail diagnostics.

Before the effect is opened, specify whether influence analysis will be used, which diagnostics will be run, whether the procedure is primary, prespecified sensitivity, or diagnostic, and how disagreement with the primary estimator will be adjudicated.

Possible diagnostics include:
`Cook's Distance / DFFITS / DFBETA / leverage / robust-regression weights / robust-regression sensitivity`.

Boundaries:
1. B1 tail cleaning cannot be described as having solved regression influence;
2. after B3, do not delete an influential observation merely because it hurts the result and then relabel the new regression as the original confirmatory main;
3. trace influential observations to actual economic events/entities or data errors;
4. independently demonstrated data errors follow repair rules;
5. genuine economic events are not mechanically deleted for being influential;
6. material disagreement between the primary estimator and prespecified robust/influence sensitivity becomes an estimator-or-inference issue and must be adjudicated before a formal economic verdict;
7. robust regression can carry the primary confirmatory role only if it was frozen as the primary estimator before effect inspection.

External precedent may motivate regression influence diagnostics, but no single method is universally valid; current design assumptions still require `CORE-M01` mapping.

## H. Pilot/screen state and freezes

## EMP-PILOT01 — Pilot state / verdict
Use only:

```text
SCREEN_STATUS =
NOT_STARTED / IN_PROGRESS / BLOCKED / REPAIRING / COMPLETE
```

and

```text
SCREEN_VERDICT =
CONTINUE / CONTINUE_WITH_REVISION / STOP_RESOURCE_ALLOCATION / NOT_ADJUDICATED
```

If a technical, measurement, or precision blocker remains unresolved and no legal final adverse decision exists, use `NOT_ADJUDICATED`.

## EMP-PROBE01 — Candidate observation ≠ candidate outcome
The full execution-class definitions live in `EMP-GATE00`; this rule only fixes one boundary:

```text
PREOUTCOME_MEASUREMENT_VALIDATION may use candidate observations.
PREOUTCOME_MEASUREMENT_VALIDATION may not open the candidate research outcome/effect.
```

Real candidate observations may be required to validate coverage, matching, classifier yield, gold-label quality, or construct non-degeneracy. The validation metric must remain distinct from the research outcome, the workflow stays within B0–B2, and no screen verdict is produced.

A technical probe should prefer synthetic, dummy, or noncandidate data because it is only validating technical behavior.

## EMP-FREEZE-A — Outcome-Screen Decision Freeze
Freeze A applies only to `OUTCOME_DECISION_SCREEN`.
Set `FREEZE_LAYER=FREEZE_A_SCREEN_DECISION` and `FREEZE_STATUS=IN_PROGRESS` until all applicable items are frozen.

Before B3, freeze as relevant:
- screen objective, explicitly as resource allocation rather than confirmatory proof;
- input identity;
- sample rule;
- treatment/control;
- outcome/construct;
- aggregation;
- cleaning/transformation/scale;
- estimand;
- minimal estimator;
- the prespecified progression/resource criterion and any screen-specific statistical rule needed to operate that criterion, explicitly without upgrading the screen into formal economic-null/equivalence inference;
- multiplicity family/claim logic/adjustment plan if multiplicity is substantively triggered;
- sample/precision rationale matched to the screen objective;
- progression criteria;
- allowed repair classes;
- blindness boundary;
- stop conditions.

The purpose is to prevent screen results from selecting the screen rules after the fact.

## EMP-FREEZE-A2 — S13 entry and completion
Entry requires the relevant upstream data-identity, measurement, and system-identity gates to be complete under the canonical state semantics.

Completion requires:
- screen applicability resolved as applicable or not applicable;
- screen-data reuse policy frozen where applicable;
- within-study multiplicity resolved as pass or not applicable;
- blindness still within B0–B2;
- for an applicable screen, the screen objective, sample rule, progression criteria, allowed repairs, and stop conditions are frozen.

Economic-threshold status is not automatically part of this screen freeze; formal economic thresholds belong to the formal study unless the screen's prespecified decision rule explicitly and legitimately requires them.

Starting an applicable screen requires explicit user authorization to open the effect. Method discussion, questions, or audit requests are not screen-start authorization.

## EMP-FREEZE-B — Formal Main Specification Freeze
Set `FREEZE_LAYER=FREEZE_B_FORMAL_MAIN_SPEC` and `FREEZE_STATUS=IN_PROGRESS` until the formal main specification is complete.

Freeze B is produced only after the surviving pilot/screen, post-pilot literature freshness/collision recheck, and formal identification strengthening.

It may implement a larger formal sample under prespecified rules, fuller inference, prespecified benchmarks or robustness checks, construct-preserving measurement improvements, and the already frozen multiplicity architecture.

Do not use the pilot result to change the core estimand, primary outcome, treatment, direction, sample frame, or cleaning rule in order to rescue sign or significance.
If these core elements must change, set `CLAIM_DRIFT=YES`, return for refreezing or create a new branch, and record the old pilot result in the Seen Data history.

## EMP-SCREEN01 — Outcome screen is optional
Pilot/feasibility guidance distinguishes feasibility objectives from formal effectiveness testing. ScholarOps transfers that principle to finance/business research with adaptation: not every surviving project should be forced through an outcome decision screen.

At the screen-applicability state, record:

```text
OUTCOME_SCREEN_APPLICABILITY =
APPLICABLE
NOT_APPLICABLE
BLOCKED
```

`NOT_APPLICABLE` is legitimate when, for example, a holdout would materially damage a small formal sample, the real risk is measurement/feasibility already handled pre-outcome, or the value of early effect inspection is smaller than the inferential cost of contaminating the formal study.

In that case, proceed without opening the effect and record screen status/verdict/reuse policy as not applicable under the state model.

## EMP-SCREEN02 — Screen verdict semantics
For an applicable screen, the only verdicts are:

```text
CONTINUE
CONTINUE_WITH_REVISION
STOP_RESOURCE_ALLOCATION
NOT_ADJUDICATED
```

`STOP_RESOURCE_ALLOCATION` means only:

> Under the prespecified screen rule, the current project does not justify additional research resources.

It must never be rewritten as proof that the economic effect is zero, statistically equivalent, or smaller than every meaningful effect.
Formal economic null/equivalence/minimum-effect claims belong to the formal study and their corresponding threshold gate.
A stopped screen enters the terminated-branch archive rather than disappearing.

## EMP-REUSE01 — Freeze `SCREEN_DATA_REUSE_POLICY` before opening the effect

Once observations have been used to inspect an effect and that information influences whether a branch survives, reusing the same observations as if they were untouched confirmatory evidence can invalidate ordinary inference.

Internal-pilot research provides an important but narrow exception. Wittes and Brittain (1990) distinguish nuisance/design parameters such as variance and control-process parameters from treatment-effect parameters, warning against adapting the design on the basis of treatment-effect information. Wittes et al. (1999) show that unblinded interim variance-based sample-size recalculation can still affect type-I error, with the magnitude depending on the design.

Before B3, freeze exactly one:

```text
SCREEN_DATA_REUSE_POLICY =
EXTERNAL_HOLDOUT
BLINDED_INTERNAL_NUISANCE_ONLY
VALID_ADAPTIVE_SEQUENTIAL_REUSE
EXPLORATORY_REUSE_ONLY
```

### `EXTERNAL_HOLDOUT`
Observations/events inspected in the outcome screen do not enter the clean confirmatory estimation. This is the default when no valid reuse design has been frozen.

### `BLINDED_INTERNAL_NUISANCE_ONLY`
Use the interim data only for nuisance/design quantities that do not disclose the treatment-effect direction or magnitude needed for the branch decision, such as variance, coverage, missingness, measurement precision, recruitment, or implementation feasibility when those quantities are genuinely effect-blind.

The stable enum name is retained for compatibility, but "blinded" here means **effect-blind for the decision being adapted**; cited internal-pilot procedures may use treatment labels to form a pooled nuisance estimate. The rule does not claim universal label-blinding.

### `VALID_ADAPTIVE_SEQUENTIAL_REUSE`
If an interim effect is opened and the same observations will remain in formal inference, a specific valid adaptive/sequential procedure and its conditions must be frozen before the effect is opened. "We will adjust later" is not a valid method.

### `EXPLORATORY_REUSE_ONLY`
If the effect was already used to select the branch and no valid adaptive/sequential correction governs reuse, the reused result is exploratory/conditional and must not be presented as a clean confirmatory test.

This four-way classification is ScholarOps governance. The cited clinical-trial sources support the narrower nuisance-versus-effect distinction and the inferential consequences of some internal-pilot reuse designs; they do not establish that these four labels are universal statistical categories.

## EMP-REUSE02 — Inference after data reuse

The final interpretation is constrained by the reuse policy frozen before effect opening:

| Policy | Formal interpretation |
|---|---|
| `EXTERNAL_HOLDOUT` | ordinary confirmatory interpretation on the untouched holdout, subject to the frozen design |
| `BLINDED_INTERNAL_NUISANCE_ONLY` | confirmatory only under the documented internal-pilot/nuisance procedure and its assumptions |
| `VALID_ADAPTIVE_SEQUENTIAL_REUSE` | use the inference/critical values of the frozen valid adaptive/sequential procedure, not ordinary final p-values |
| `EXPLORATORY_REUSE_ONLY` | exploratory/conditional; do not call it clean confirmatory evidence |

Wittes et al. (1999) study a particular two-group normal internal-pilot design with interim variance-based sample-size recalculation. In that setting, the naive final t-test can inflate type-I error because the final pooled variance is biased downward. The size of the distortion is design-dependent:

- in their **restricted** design, for internal-pilot samples above roughly 30 per group, the type-I error over the parameter range examined did not exceed about 0.052;
- in the **unrestricted** design, early recalculation with a very small pilot can produce materially larger inflation.

Their design-specific recommendations also include planning the internal pilot from the start rather than changing sample size ad hoc, using a practical pilot fraction roughly between one-quarter and three-quarters, and—in the restricted normal case studied—using a critical value around 1.99 rather than 1.96 to protect a 5% type-I error over a wide parameter range.

These numbers are **not universal ScholarOps constants**. They apply only when the current design matches the cited normal internal-pilot setting closely enough. Effect-based branch selection is a different problem and those numerical corrections must not be transplanted to it.

If the actual reuse at writing differs from the frozen policy, set `CLAIM_DRIFT=YES` and return through the governance path rather than silently changing the policy.

## I. Formal estimation and result QA

## EMP-FORMAL01 — Formal Main Estimation executes Freeze B, not a new design
Enter formal main estimation only when the execution class is `FORMAL_STUDY` and Freeze B is complete.
Run the already frozen primary sample, treatment/exposure, primary outcome, cleaning/transformation, estimator, FE/control structure, inference/cluster procedure, multiplicity architecture if triggered, and economic-scale interpretation if triggered.
Formal-result execution is not a new design-selection phase.

## EMP-FORMAL02 — Formal Result QA
At minimum record or verify:

```text
FORMAL_MAIN_RESULT_STATUS
INPUT_IDENTITY
CODE_IDENTITY
SAMPLE_N / ENTITY_N / DATE_OR_EVENT_N / CLUSTER_N
ESTIMATOR_COMPLETION
WARNING_OR_CONVERGENCE_STATUS
PRIMARY_ESTIMATE_AND_UNCERTAINTY
MULTIPLICITY_OUTPUT_IF_TRIGGERED
RESULT_OUTPUT_IDENTITY
SEEN_DATA_REGISTER_UPDATED
```

Proceed to mechanism/robustness only when the main result is complete and no unresolved implementation, data, measurement, or inference blocker remains.
A demonstrated implementation/data bug may be repaired and the frozen main rerun. A required construct or identification change triggers Claim Drift. A nonsignificant or inconvenient result is not permission to redesign the main specification.

## EMP-FORMAL03 — Mechanism / robustness is triggered, not automatic
After the formal main result:
- if the design already requires a mechanism test or prespecified robustness checks, complete them under the frozen rules;
- if no mechanism claim and no material robustness risk exists, mark the layer `NOT_APPLICABLE` and proceed to writing;
- any mechanism or specification invented after seeing the result is `EXPLORATORY`.

## J. Multiplicity and specification governance

## EMP-MULT00 — Three multiplicity layers are distinct
Do not collapse three different problems into one adjustment:

```text
A. WITHIN_STUDY_MULTIPLICITY
   multiple outcomes, treatments, subgroups, windows, horizons, etc. within one study

B. SPECIFICATION_SEARCH_DATA_SNOOPING
   repeated use of the same data to choose a window, model, rule, or sample

C. LITERATURE_SELECTION_FACTOR_ZOO
   selection of the research hypothesis from a heavily searched literature universe
```

Within-study FWER/FDR procedures do not repair literature-level factor-zoo selection, and a specification-search correction is not the same problem as outcome multiplicity.
Track the corresponding statuses independently.

## EMP-MULT01 — Define the scientific claim unit before the testing family
Multiplicity can arise from multiple outcomes, treatments, subgroups, event windows, horizons, model/specification variants, or mechanism tests.

The external source directly identifies outcomes, subgroups, and treatments as multiplicity sources. ScholarOps extends the same decision logic to windows, horizons, and mechanism tests; specification search is separately governed and must not be misrepresented as directly covered by the source.

For independent tests at alpha 0.05, the familywise probability of at least one false positive is `1-(1-alpha)^N`; this illustrates why multiplicity becomes material as the number of tests grows. The source also documents that multiple outcomes are common in experimental-economics practice. These facts motivate an active multiplicity gate rather than a purely discretionary warning.

Before applying the source directly, check its design assumptions, including treatment assignment, subgroup structure, and family size. If the current sampling or dependence structure differs materially, use `CORE-M01` before choosing the procedure.

Before Freeze A, each confirmatory hypothesis records:

```text
HYPOTHESIS_ID
SCIENTIFIC_CLAIM_ID
HYPOTHESIS_ROLE
OUTCOME
TREATMENT_OR_EXPOSURE
SUBGROUP_IF_ANY
HORIZON_OR_WINDOW
SPECIFICATION_ROLE
MULTIPLICITY_FAMILY_ID
```

A family is defined by which rejections jointly support the same confirmatory scientific claim, not by whether tests appear in the same table. Do not split an unfavorable test into a new family after results are visible.

## EMP-MULT02 — Claim logic
Freeze one claim logic before results:

```text
ANY_OF_MANY
ALL_CO_PRIMARY_REQUIRED
ORDERED_HIERARCHY
OMNIBUS_OR_INDEX_FIRST
DISCOVERY_FAMILY
SEPARATE_SCIENTIFIC_CLAIMS
```

The appropriate error treatment depends on the logic. Do not inspect results and then choose the logic that makes the surviving pattern easiest to report.

When success requires every co-primary endpoint to pass, the type-I-error logic differs from an any-of-many family; the cost shifts toward joint power/precision rather than a simple multiplicity penalty. Confirm the exact design assumptions before applying a numerical example from another field.

## EMP-MULT03 — Error criterion / method selection
### Confirmatory any-rejection family
Record `MULTIPLICITY_ERROR_CRITERION=FWER` by default unless a different confirmatory criterion is explicitly prespecified and methodologically justified.

`Holm` is a transparent strong-FWER baseline that does not require independent p-values. Where the dependence/resampling structure is valid and independent variation units are sufficient, a resampling step-down method such as Romano-Wolf or Westfall-Young style procedures may improve power while keeping the same FWER objective. Do not apply them mechanically to few-event, clustered, or nonstandard designs without validating the resampling assumptions under `CORE-M01`.

When only published unadjusted p-values are available rather than individual-level data, simple procedures such as Bonferroni/Holm may be the only directly implementable options.

### Large exploratory/discovery family
FDR control may be appropriate for exploratory screening. The Benjamini-Hochberg 1995 result defines and controls FDR under its stated independence conditions; it is not a dependence-robust universal license.

FDR and FWER answer different error questions. A discovery family controlled by FDR remains `EXPLORATORY/DISCOVERY`; it does not automatically become the original confirmatory claim.

### Assumption discipline
Bonferroni/Holm provide broad dependence-robust baselines, whereas more powerful methods may require stronger dependence/distribution/resampling assumptions. Choose the method only after mapping those assumptions to the current sampling and cluster structure.

## EMP-MULT04 — Primary / secondary / exploratory hierarchy
Before Freeze A, classify hypotheses as:

```text
PRIMARY
CO_PRIMARY
SECONDARY_CONFIRMATORY
EXPLORATORY
```

The transferable principle from formal multiple-endpoint guidance is to order conclusion-bearing endpoints before multiplicity treatment. ScholarOps does not import clinical regulatory rules wholesale into finance/business research.

An exploratory endpoint does not support the confirmatory conclusion and therefore should not be given a cosmetic multiplicity correction merely to make it look confirmatory. Secondary confirmatory claims should be interpreted under the prespecified hierarchy and familywise logic, and an excessively long secondary list can destroy power or make late hypotheses practically unreachable under ordered procedures.

Do not promote a secondary or exploratory result to the “real primary finding” after the primary result fails.

## EMP-MULT05 — Reporting
Formal reporting should include, as relevant:
- effect estimate;
- compatible confidence interval or uncertainty measure;
- unadjusted inferential quantity;
- multiplicity-adjusted result;
- family definition;
- adjustment method;
- number of hypotheses;
- dependence/resampling assumptions.

Adjusted and unadjusted results should be presented together when that comparison is scientifically informative. Report how the adjustment changes the rejection pattern rather than summarizing the table as “some results remain significant.”

## EMP-MULT06 — Gate status / automatic short-circuit
Count `N_CONFIRMATORY_TESTS_PER_SCIENTIFIC_CLAIM` first.

If a confirmatory claim has one substantive test and there are no multiple primary outcomes/treatments/subgroups/windows/specification choices jointly supporting that claim, set:

```text
WITHIN_STUDY_MULTIPLICITY_STATUS=NOT_APPLICABLE
MULTIPLICITY_LEDGER_REQUIRED=NO
```

Do not create a family ledger or apply Holm/FDR merely for formality.

If real multiplicity exists, require the ledger and enter the relevant multiplicity rules. If the family is unfrozen, claim logic is undefined, or the adjustment is incompatible with the sampling/cluster structure, set `WITHIN_STUDY_MULTIPLICITY_STATUS=BLOCKED`; the relevant freeze cannot complete.

## EMP-SPECSEARCH01 — Specification search on one dataset

Record:

```text
SPECIFICATION_SEARCH_STATUS =
PASS / CONDITIONAL / BLOCKED / NOT_APPLICABLE
```

Trigger this rule when the same dataset is repeatedly used to choose among windows, models, estimators, trading rules, sample filters, thresholds, or other specifications that were not frozen in advance.

White (2000) formalizes a specific data-snooping problem: among an enumerable collection of searched models, test the null that the best model encountered has no predictive superiority over a named benchmark. A Reality-Check-style claim therefore requires, at minimum:

```text
BENCHMARK
PERFORMANCE_MEASURE
PREDICTION_SAMPLE
SEARCHED_SPECIFICATION_SET
```

The benchmark, performance criterion, prediction sample, and searched model family must be defined well enough to reconstruct what was searched. The procedure evaluates whether the apparent best relative performance could arise from the search; it does not establish that the winning model is structurally true.

White's S&P 500 example illustrates how ignoring the search can materially understate uncertainty: for directional accuracy the naive p-value was about 0.0036 while the Bootstrap Reality Check p-value was about 0.2040; for prediction MSE the corresponding values were about 0.1068 and 0.3674. In the paper's setup, a large naive p-value is already sufficient to stop because the Reality Check p-value will not rescue it.

Permissible ScholarOps responses to a triggered specification search include:
- freeze the complete confirmatory specification before formal estimation and label later variants exploratory;
- use a validated data-snooping / multiplicity procedure whose assumptions match the sampling and dependence structure;
- separate search and formal inference with an untouched holdout when scientifically and statistically appropriate.

If extensive search has already occurred and no defensible correction, holdout, or refreeze path remains, set `SPECIFICATION_SEARCH_STATUS=BLOCKED` for clean confirmatory inference.

Source boundaries are mandatory:

1. White's procedure corrects for the model set that can be enumerated/replayed; unobserved or unreconstructable prior searches are not automatically included.
2. The paper's core asymptotics are developed for dependent time-series settings under stated regularity/mixing conditions. Extensions to other data structures require their own justification.
3. The paper notes that directional-accuracy statistics with estimated parameters are not covered by the simplest smooth corollary; its directional-accuracy example relies on additional reasoning and supporting simulation evidence.
4. The Reality Check can be conservative and is not a general certificate of robustness.
5. White discusses holdout/test data directly, but treats full cross-validation extensions as plausible future work rather than a proved general result.

The implementation values used in White's illustration—such as 500 bootstrap resamples and a particular stationary-bootstrap smoothing parameter—are example choices, not universal ScholarOps defaults.

## K. Economic thresholds and effect interpretation

## EMP-THRESH00 — Execution-class activation
### TECHNICAL_PROBE
`ECONOMIC_THRESHOLD_STATUS=NOT_APPLICABLE`.

### PREOUTCOME_MEASUREMENT_VALIDATION
`ECONOMIC_THRESHOLD_STATUS=NOT_APPLICABLE`. A measurement precision target may exist, but it is not an economic SESOI.

### OUTCOME_DECISION_SCREEN
The formal economic-threshold gate is not automatically activated because the screen does not make a formal economic-null claim. Its go/no-go rule is the prespecified progression criterion.

### FORMAL_STUDY
Use an economic magnitude interpretation when the formal estimand and claim require it. If the scientific claim does not depend on a minimum-meaningful-effect judgment, the full threshold gate may remain not applicable with a documented method reason.

## EMP-THRESH01 — Keep three thresholds separate
Do not conflate:
1. `ECONOMIC_MINIMUM` or SESOI—the smallest economically/theoretically meaningful effect;
2. `STATISTICAL_EVIDENCE_RULE`—CI, alpha, equivalence, minimum-effect, or related inferential rule;
3. `MDE_OR_PRECISION_TARGET`—the smallest effect the design can detect or exclude at the stated operating characteristics.

None can substitute for the others.

## EMP-THRESH02 — Evidence order for an economic minimum

Define an economic minimum in the original economic units whenever possible rather than starting from an arbitrary standardized effect such as "0.1 SD."

Preferred evidence order:
1. a substantive threshold tied to the actor, decision, institution, payoff, or cost;
2. a theory- or mechanism-based minimum;
3. the economic magnitude in high-quality close precedent;
4. a defensible domain-expert, regulator, or professional convention;
5. treatment-blind clean-sample distributional scales **only for translating** the raw-unit effect into SD/IQR/percentile language, not for creating substantive importance.

If the raw-unit effect is hard to interpret, report one or more scale translations such as:
- a one-standard-deviation change;
- an interquartile or other percentile contrast;
- a robust dispersion contrast;
- a high-minus-low portfolio characteristic contrast when the asset-pricing design makes that meaningful.

Bali, Engle, and Murray (2016, §6.2) provide examples of translating Fama-MacBeth coefficients into economic magnitudes using a cross-sectional standard deviation, percentile differences such as IQR or 95–5, and high-minus-low portfolio-characteristic spreads. Their discussion supports multiple interpretable **scales**; it does not define a universal smallest economically important effect.

Therefore:

```text
scale translation != economic-minimum definition
```

The evidence hierarchy above is ScholarOps governance. Bali, Engle, and Murray support the translation step, not the substantive ordering in items 1–4.

## EMP-THRESH03 — A formal economic-null conclusion cannot come from nonsignificance
This rule belongs to `FORMAL_STUDY` economic-magnitude adjudication, not to `OUTCOME_DECISION_SCREEN`. A nonsignificant result does not establish that a meaningful effect is absent. Formal absence/irrelevance claims require a prespecified equivalence or minimum-effect framework with defensible bounds and adequate precision.

When significance and equivalence/minimum-effect logic are jointly considered, the result can be substantively nonzero, substantively small, statistically inconclusive, or compatible with a null-like range. “Undetermined” is a valid scientific conclusion and must not be rewritten as “no effect.”

Equivalence bounds must be reported with the equivalence claim. Bounds may come from theory, practice, decision costs, or—when explicitly justified—the smallest effect the design can meaningfully resolve at the feasible sample size. A resource-derived bound is project-specific and does not establish universal irrelevance.

The conclusion applies only to the operationalization and design actually studied. Measurement changes, confounding, or a different intervention can change the result. Independent replication remains relevant because evidence for the absence of a meaningful effect carries a different burden from merely failing to detect one.

## EMP-THRESH04 — No arbitrary convention
Do not freeze an economic minimum merely because a number is conventionally called “small,” because a standardized effect such as 0.1 SD is common, or because the estimate looks numerically small.

If no defensible `ECONOMIC_MINIMUM` can be established before the relevant formal freeze, set `ECONOMIC_THRESHOLD_STATUS=BLOCKED` for economic-magnitude adjudication. The study may still report estimates and uncertainty with a lower claim ceiling.

## EMP-THRESH05 — Threshold Source Registry
For each candidate economic minimum, record:

```text
THRESHOLD_ID
RAW_UNIT
TARGET_CONSTRUCT
TARGET_ACTOR_OR_DECISION
POPULATION
TIME_HORIZON
SOURCE_CLASS
SOURCE_CITATION
SOURCE_QUALITY
INDEPENDENT_OF_CURRENT_EFFECT
TRANSLATION_REQUIRED
```

At minimum distinguish source classes such as:

```text
DIRECT_DECISION_OR_COST_ANCHOR
THEORY_BASED
HIGH_QUALITY_CLOSE_LITERATURE
DOMAIN_OR_REGULATORY_CONSENSUS
EMPIRICAL_EXPECTED_EFFECT
STANDARDIZED_CONVENTION
```

Treatment-blind SD/IQR/MAD can translate units; they do not by themselves define what is economically meaningful.

## EMP-THRESH06 — Threshold commensurability
Before comparing thresholds from different sources, check whether they refer to the same:
`construct / actor / population / horizon / raw unit / decision consequence`.

If not, mark `NOT_COMMENSURABLE`; do not average or vote across them.
If conversion to a common economic unit is defensible, retain the original values and the translation rule.

## EMP-THRESH07 — Formal economic-threshold conflict resolution
This rule applies when `FORMAL_STUDY` uses economic thresholds; it does not turn an `OUTCOME_DECISION_SCREEN` into an economic-null test. When multiple high-quality, construct-aligned threshold sources disagree, record:

```text
THRESHOLD_CONFLICT_STATUS =
NONE
RESOLVED_PRE_B3
THRESHOLD_SET_FROZEN
UNRESOLVED
NOT_APPLICABLE
```

If one threshold directly maps to the current actor/decision/cost-benefit problem and others are generic conventions, it may be frozen as primary before B3 with the others retained as sensitivity thresholds. The choice must follow substantive relevance, not which threshold produces the preferred verdict.

If no principled ordering exists, freeze an admissible threshold set rather than forcing a single value. Report whether the decision is robust across the set; if different admissible thresholds imply different decisions, mark the conclusion threshold-sensitive and use the prespecified revision path rather than selecting a favorable threshold.

If no defensible admissible set can be constructed, the study may report effect/precision evidence but cannot issue a formal economic-null/stop decision based on that threshold gate.

## EMP-THRESH08 — Required artifact
When the economic-threshold gate is active, create an `ECONOMIC_THRESHOLD_LEDGER_<ID>.csv` before effect inspection containing candidate thresholds, commensurability assessment, primary-or-set decision, rejected thresholds and reasons, and effect-open status.
