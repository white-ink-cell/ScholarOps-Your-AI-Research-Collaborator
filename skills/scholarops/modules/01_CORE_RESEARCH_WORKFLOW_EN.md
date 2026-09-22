# 01 — Core Research Workflow


## A. Research-question governance

## CORE-Q01 — Important Problem before Method
First state:
`actor / action-or-decision / friction / counterfactual / consequence / why-it-matters`.
Do not reverse-engineer an unimportant research question from a new algorithm, a newly available field, or easy data access.

## CORE-Q02 — Construct Identity
The A/B observed in the data must actually correspond to the A/B claimed by the theory.
For any proxy, data-source substitution, or change in granularity, compare:
`actor / unit / timing / information set / construct / claim ceiling`.
If construct identity fails, lower or refreeze the claim before estimating anything.

## CORE-Q03 — So-What
A candidate must explain how the result could change at least one of:
`understanding / identification credibility / measurement / theoretical interpretation / boundary conditions / decisions / institutions`.
“Data exist + there is a gap” is not enough.

## CORE-Q04 — Important Problem × Credible Attack
If a problem is important but there is currently no credible path through data, identification, or measurement, place it in a future-data or long-horizon queue rather than calling it a bad question.
If it is easy to execute but does not matter, stop on So-What grounds.

When the question, actor, construct, and consequence are sufficiently defined for a literature landscape scan, set `QUESTION_FORMATION_STATUS=PASS`; otherwise use `REVISE` or `BLOCKED`.

## B. Discovery and literature

## CORE-LIT01 — Plural Discovery Routes
Candidates may originate from:
`canonical problem / real-world phenomenon / institutional or regime change / assumption challenge / literature conflict / replication concern / researcher curiosity`.
These routes document idea provenance; they do not establish novelty.

## CORE-LIT02 — Blind-first is a bias diagnostic, not a veto
A blind-first search may be used to reduce anchoring on historical seed papers. After the blind pool is frozen, the researcher's own idea may enter the same gate as a challenger.
Researcher interest may generate a question; it does not establish novelty or priority.

## CORE-LIT03 — Landscape ≠ Focused Census
A Landscape scan supports breadth discovery and preliminary collision checks only. A Focused Census is required before Pre-L4.

A completed Focused Census must include at least:
- a search log;
- a coverage map;
- a bibliography;
- a source map;
- an unresolved-blocker ledger.

Do not enter L4 merely because the Landscape scan “looks uncrowded.”

## CORE-LIT04 — Focused Census stopping rule
Before a Census begins, record:
`required source families / query families / year window / citation-chase targets / source-quality order / decision-stability criterion / unresolved-blocker policy`.

Completion is based on decision stability, not a fixed number of search rounds:
1. the prespecified Core, Adjacent, and high-authority Frontier source families are covered;
2. the prespecified query families and dangerous-neighbor citation chains are completed;
3. the closest-neighbor set and contribution delta are decision-stable, meaning additional non-decisive sources no longer change the current continuation, narrowing, or pre-L4 decision;
4. run one final sentinel search using at least one new synonym, citation route, or freshness/date route;
5. if the sentinel reveals a potentially decision-changing source, continue targeted verification;
6. if it only returns duplicates, low-relevance items, or material that cannot change the decision, the Census may stop;
7. if the tool cannot observe complete forward citations, record `NOT_OBSERVABLE`; never describe the search as exhaustive.

A decisive new paper may terminate the search early. Do not add search rounds merely to satisfy a ritual count.

## CORE-LIT05 — Evidence vs Search Process vs Provenance
`EVIDENCE` means the actual paper/appendix, official data or institutional document, or formal standard.

`SEARCH_PROCESS` means queries, search dates, unavailable counts, and exclusion records.

`PROVENANCE` means internal registries, SQL, prior reports, summaries, or scoring tables.

Claims about novelty, collision, construct identity, or data existence cannot be supported solely by search-process metadata or provenance records.

## CORE-LIT06 — Source Quality / Frontier Authority
Default priority:
1. peer-reviewed Core literature;
2. peer-reviewed Adjacent literature;
3. canonical high-quality sources;
4. high-authority frontier research;
5. low-authority frontier material only for exact-similarity checks or a Core-gap sentinel.

arXiv, SSRN, and ResearchGate are distribution channels, not quality certifications.
Low-authority unpublished work must not be given the same adjudicative weight as high-quality peer-reviewed evidence when issuing a stop or narrowing decision.

## CORE-LIT07 — Read the actual predecessor method
Do not transfer a method from a title or abstract.
At minimum extract:
`sample construction / variable formula / cleaning / timing / estimator / inference / assumptions / failure modes / appendix implementation / version changes`.
Only then decide what is transferable.

## CORE-LIT08 — User-provided core material first
If the user has already supplied core papers, appendices, replication packages, methods books, or official documents, search and read those materials first before adding external literature.
Do not redesign from memory merely because the conversation changed.

## CORE-LIT09 — Open-world Field Router
Do not hard-code literature search to one journal set.
First identify the candidate's actual academic home, then build the relevant ecology dynamically:
`Core / Adjacent / Frontier / methods / institutional sources`.
Failure to find a paper is not evidence that no one has studied the question.

## CORE-LIT10 — Standard / Regulator claim ceiling
Regulations, accounting standards, and official rules can establish institutional definitions and requirements.
They cannot, by themselves, establish literature absence, novelty, or an economic effect.

## CORE-LIT11 — Freshness Reopen
A completed Focused Census is not automatically rerun because a new conversation or sweep begins.
Reopen only when a relevant trigger exists, such as:
`freshness window exceeded in a fast-moving field / new highly related paper / estimand or measurement changed`.
Otherwise reuse the frozen evidence package.

## C. Discovery discipline and scope

## CORE-DISC01 — Research horizon / boundedness
Classify candidates with a controlled horizon such as:
`CURRENT_EXECUTABLE / BRIDGE_PROJECT / LONG_HORIZON_RESEARCH_AGENDA / HOLD_FUTURE_DATA`.
Project-specific labels may extend the vocabulary only through the schema; do not create near-synonyms to bypass the state model.

A current project must have an observable object and a bounded claim ceiling. If its value depends entirely on a future, currently unobservable equilibrium question, place it in the long-horizon agenda.

## CORE-DISC02 — Discovery freeze / selection
Once the intended Landscape coverage is complete, freeze new-idea generation by default and move selected candidates into Focused Census.
Reopen Discovery only if the selected candidates are all terminated, a new institutional/data shock changes the opportunity set, or a clear systematic omission is found.

Focused Census should usually examine a small set of construct-distinct candidates with high decision value, rather than manufacture a ranked Top-N table from incomparable scores.

## CORE-DISC03 — Discovery Iteration vs Confirmatory Lock
Before the Pre-L4 Freeze, controlled iteration is allowed among:
`problem ↔ question ↔ construct ↔ literature ↔ argument ↔ feasibility`,
with version/change/reason recorded.

After Pre-L4 Freeze, strict gates apply. A substantive change to the question must trigger Claim Drift and refreezing; do not change the question while pretending to remain in the original L4 review.

## D. Contribution / collision

## CORE-C01 — Collision is diagnostic, not automatic death
A collision-based stop requires both:
`DIRECT_REDUNDANCY + NO_SUBSTANTIVE_CONTRIBUTION_DELTA`.

The same broad question can still support a contribution through a credible identification advance, contradictory adjudication, mechanism deepening, boundary condition, institutional change, or high-value replication, but the candidate must explain how the new design changes the inference that can be trusted.

## CORE-C02 — Single Contribution-Delta Rule
For each surviving candidate, keep at most one primary and two secondary contribution modes:

```text
NEW_QUESTION_OR_OBJECT
IDENTIFICATION_ADVANCE
CONSTRUCT_OR_MEASUREMENT_CORRECTION
CONTRADICTORY_ADJUDICATION
MECHANISM_DEEPENING
BOUNDARY_CONDITION
EXTERNAL_VALIDITY_WITH_THEORY
DECISION_OR_POLICY_RELEVANCE
EQUILIBRIUM_EXTENSION
INSTITUTIONAL_OR_TECHNOLOGICAL_REGIME_CHANGE
SYNTHESIS_WITH_NEW_INTERACTION
HIGH_VALUE_REPLICATION_OR_REPRODUCIBILITY
ENGINEERING_OR_TOOL_ONLY
DIRECT_REDUNDANCY
```

Always state:
`old paper does X / candidate adds Y / why Y changes inference / evidence that X lacks Y / required data`.

## CORE-C03 — No Conjunction Novelty
The fact that no single paper checks boxes A+B+C+D does not establish novelty.
If the combination adds only workflow assembly, more checks, or a newer model, treat it as weak by default.
A synthesis becomes potentially substantive only when it creates a new interaction, complementarity, substitution, nonlinearity, equilibrium implication, decision rule, or boundary condition.

## CORE-C04 — Same question, different method
A different method is not itself a contribution.
Before results, state:
`old limitation / new advantage / bias or identification problem resolved / change in estimand credibility / adjudicating pattern`.

## CORE-C05 — Contradiction / deepening
A contradictory result is strong only if the new design can credibly adjudicate the prior disagreement.
Multiple papers may study the same mother question, but the candidate must add a meaningful mechanism, boundary, actor, institution, equilibrium, welfare or decision consequence, or measurement identity.

## CORE-C06 — Inference-Value Test
A study can still contribute when its directional result matches prior work if it changes:
`causal credibility / construct validity / rival exclusion / boundary / mechanism / magnitude, welfare, or decision implication`.
If the only increment is a larger sample, newer method, finer granularity, or more precise reconfirmation, treat the contribution as weak by default and potentially stop it.

## E. Claim discipline and craft

## CORE-CL01 — Claim ceiling
Predictive does not imply causal.
A signal does not imply adoption.
A proxy does not automatically equal the construct.
Platform existence does not imply user entitlement.
Do not move the claim above the highest evidentiary level actually established.

## CORE-CL02 — Mechanism is not heterogeneity by itself
Prefer short, direct, observable mechanism chains.
Heterogeneity supports a mechanism only when the mechanism was specified in advance and the heterogeneity pattern helps rule out a strong rival explanation.

## CORE-CL03 — Exploratory after result
Any hypothesis, cutoff, subgroup, or mechanism first formed after formal results are opened must be labeled `EXPLORATORY`.
Do not rewrite it as confirmatory.

## CORE-CRAFT01 — Problematization
Beyond gap search, examine whether the candidate challenges or clarifies the:
`unit / rationality assumption / information set / counterfactual / equilibrium / measurement / institutional invariance / external-validity boundary`.

## CORE-CRAFT02 — Argument architecture
Argument architecture is a post-L4, pre-writing craft tool, not a Pre-L4 entry gate.
A useful form is:
`question or claim → mechanism or reason → expected evidence → warrant → strongest rival → discriminating evidence → qualification or claim ceiling`.

A one-paragraph paper test may expose missing logic by forcing the researcher to state:
`question / unit-estimand / design / closest literature / contribution / why the reader should care`.
If used early in Discovery, it remains diagnostic only; inability to write a polished paragraph cannot by itself block L4.

## CORE-CRAFT03 — Theory/contribution map
Maintain a lightweight map of:
`WHAT / HOW / WHY / WHO-WHERE-WHEN`
and
`ORIGINALITY / UTILITY`.
Do not force every project to claim a grand new theory.

## CORE-CRAFT04 — Write-to-think / outline-first
During Discovery, exploratory memos may be used to reveal logical gaps.
Before formal writing, freeze a `PAPER_ARGUMENT_OUTLINE` and `EXHIBIT_MAP` so the manuscript is organized around the argument rather than the chronological order of research work.

## F. Data/method-triggered candidate discipline

## CORE-D01 — Data does not create importance
A `DATA_FIRST` or `METHOD_FIRST` candidate must first establish that:
1. the problem and bottleneck existed independently of the new data or method;
2. the old approach could not distinguish important competing explanations;
3. the new data or method changes construct validity, identification, or observability, rather than merely making the study larger, finer, or more convenient.

## CORE-D02 — Historical substitute
Before claiming that a question can be studied for the first time, search for historical substitutes such as:
`administrative data / hand-collected samples / surveys / FOIA / commercial or proprietary data / author-constructed data / legacy filings / replication packages`.

## CORE-D03 — Decomposition is not novelty
Decomposing Y into Y1/Y2/Y3 is not automatically a contribution.
Continue only if the decomposition separates theories, prevents sign cancellation, changes the counterfactual, or changes a relevant decision.

## CORE-D04 — Cheap stop for data/method-triggered candidates
Before investing in a full Focused Census for a data-first or method-first idea, run a low-cost decision check using a small set of key papers, historical substitutes, an old-vs-new inference table, and the contribution delta.
If the candidate cannot show that the problem predates the new capability and that the capability changes inference, stop early rather than spending a full L4 review merely to document failure.

## G. Method precedent / ambiguity

## CORE-M01 — Professional Method Precedent / Concrete-Problem Grounding
Before any action with substantive methodological consequences, ask two questions.

### A. Is the Skill procedure actually specified?
At minimum it must cover:
`input / unit / timing / construct / sequence / data conditions / decision criteria / estimator-or-operation / evidence basis / failure state / freeze point / next state`.
If any missing item can materially change the conclusion, set `METHOD_GAP=YES`.

### B. Does the current problem contain a special case not covered by the Skill?
Examples include:
- unusual data-generating mechanisms;
- special missingness or selection;
- nested, clustered, or network dependence;
- human-AI collaboration or agent workflows;
- vendor-specific field semantics;
- unusual market institutions or event timing;
- special labels or measurement error;
- nonstandard sampling, rollout, or interference;
- data distributions or execution constraints inconsistent with standard textbook assumptions.

If so, set `CONCRETE_PROBLEM_SPECIAL_CASE=YES`.
Do not mechanically apply a textbook default, guess from “usual practice,” or invent data semantics, thresholds, formulas, or missingness mechanisms to fill the gap.

Use the sequence:

```text
EXACT_PROBLEM_DEFINITION
→ WHAT_IS_SPECIAL
→ WHAT_IS_KNOWN_FROM_CURRENT_DATA/DOCS
→ WHAT_IS_MATERIALLY_UNKNOWN
→ FIELD_HOME
→ CANONICAL_METHODS
→ GRADUATE_TEXT_OR_HANDBOOK
→ HIGH_QUALITY_CLOSE_APPLICATIONS
→ OFFICIAL_VENDOR_OR_INSTITUTIONAL_DOCUMENTATION
→ COMPARE_PREDECESSOR_METHODS
→ MAP_ASSUMPTIONS_TO_CURRENT_CASE
→ METHOD_DECISION_TABLE
→ PROJECT_SPECIFIC_RULE
```

If only the user can resolve a material unknown and different answers imply different methods, apply `CORE-M03` rather than guessing.
If the current data can answer the question directly, inspect the data under Assistant-first execution rather than asking the user for an impression that can be verified.

Principle: analyze the concrete problem as it actually exists. Method sources provide candidate approaches and assumptions; they do not replace judgment about the current data, institution, or construct. Do not design by intuition first and then search for literature to justify the decision.

## CORE-M02 — Method Decision Table
For each genuinely consequential method choice, record at least:
`decision / exact current problem / special-case features / predecessor options / assumptions / evidence / current-data diagnostic / fit-or-mismatch / selected rule / rejected alternative / reason / claim consequence`.

If the predecessor method relies on assumptions that the current setting does not satisfy, record `NOT_TRANSFERABLE_AS_IS`. Authority of the source is not a license for mechanical copying.

Only recurring cross-project gaps should be promoted into ScholarOps core rules. Candidate- or project-specific treatments belong in the project's Method Freeze.

## CORE-M03 — User correction / new-idea ambiguity
When the user corrects, challenges, or proposes an idea, do not guess if alternative interpretations would change the:
`question / actor / construct / estimand / treatment / data / method / claim / requested action`.
Restate the part that is clear and ask only the minimum number of clarifying questions required. Do not repeatedly interrogate the user over non-substantive wording.

## CORE-M04 — Treatment ladder, mapping chain, and inference unit
Three separate issues are often collapsed into a sentence such as “X affects Y,” even though each can independently invalidate the claim.

### 1. Treatment ladder: capability ≠ eligibility ≠ adoption ≠ use
A treatment may pass through stages such as:
`exists → available → eligible → adopted → actually used → use changes action`.
Each is a different treatment with a different estimand and interpretation. Eligibility may identify an intent-to-treat effect; it does not establish the effect of actual use.
The claim must stop at the highest rung that has been validated.

### 2. Mapping chain: validate every link between assignment and measurement
When treatment is assigned to A but the outcome is measured on B, each link is a falsifiable mapping:

```text
assignment unit → intermediate ownership/relationship → measurement unit
```

If any link is unresolved, the claim ceiling stops at the last validated link. “Usually A is B” and “we found no contradiction” are not validation.

### 3. Inference unit: rows are not independent information
Under common shocks, the independent information unit is the shock or source, not the number of exposed objects. Many objects exposed to one common shock do not create the same independent information as many shocks.
Leave-one-out, placebo, and randomization-style inference should therefore operate at the independent-information layer when appropriate. More objects can improve within-shock measurement precision; they do not substitute for more independent shocks.

### 4. Cross-level prohibition
Individual, institution, object, and market levels are distinct. Evidence at one level does not automatically license claims at another. Individual-level behavior may motivate a mechanism hypothesis without proving an aggregate welfare effect; aggregate improvement does not imply every individual improved.
When citing across levels, state whether the citation supplies a mechanism hypothesis or same-level evidence.
Detailed dependence and clustering choices remain subject to `CORE-M01`.

## H. Opportunity, readiness, and ranking

## CORE-R01 — No false precision in candidate ranking
Without prespecified weights and interpretation:
- do not average incomparable dimensions;
- do not output pseudo-precise scores such as 8.8 vs 8.4;
- do not declare a global winner during Landscape search.

Across stages, compare `NEXT_EVIDENCE_INVESTMENT_PRIORITY`, not final research quality.
Within the same stage, research quality may be compared only when evidence maturity is comparable.

## CORE-OE01 — Research opportunity and execution readiness are separate
Record separately:

```text
RESEARCH_CENSUS_VERDICT
PRE_L4_EXECUTION_READINESS
EXECUTION_BLOCKER_CLASS
RECHECK_TRIGGER
```

Controlled blocker values include:

```text
ENTITLEMENT_OR_ACCESS
COST
ETHICS_OR_APPROVAL
RECRUITMENT_OR_LABEL_SUPPLY
TOOLING_OR_ENVIRONMENT
TIME_BUDGET
NONE
NOT_APPLICABLE
```

`RECHECK_TRIGGER` must be a testable event, not “revisit later.”
`READY` corresponds to pass; `CONDITIONAL` must state a `CONDITION_TYPE`; `TEMPORARILY_BLOCKED` requires a plausible unblock path; `STRUCTURALLY_BLOCKED` means no foreseeable current path exists.

Temporary access, ethics, recruitment, or procurement problems must not masquerade as an academic stop. Conversely, weak construct identity, contribution, or So-What cannot be excused by saying better data may arrive later.

## I. L4 — Pre-screen collision adjudication and pre-formal freshness review

## CORE-L4-01 — Pre-L4 Freeze + Entry Integrity
Before L4 there is one minimal required freeze artifact:
`PRE_L4_CLAIM_FREEZE_<ID>.md`.

Freeze only the research identity needed for collision and claim-drift control:
`research question / mother problem / actor / friction / core construct / estimand / primary observable object or outcome / base scope / excluded extensions / claim ceiling / primary contribution delta / strongest rival`.

The following are not mandatory Pre-L4 freeze fields:
`one-paragraph paper / full argument architecture / exhibit map / prose-level framing / detailed execution-readiness narrative`.
These craft elements can be completed after L4 and before writing; their absence alone must not block L4.

Set `PRE_L4_CLAIM_FREEZE_STATUS=IN_PROGRESS` when the freeze begins, `COMPLETE` only after identity and evidence checks pass, and `BLOCKED` if the actual claim freeze or upstream evidence is missing.
`L4_ENTRY_AUDIT` verifies freeze existence, identity consistency, and traceable Census evidence; it does not expand the template without need.

## CORE-L4-02 — Dangerous-neighbor-first
L4 deep-reads the 3–10 most dangerous close neighbors and their important versions/appendices before citation chasing.
Classify relationships explicitly as:
`direct redundancy / identification advance / construct correction / adjudication / mechanism / boundary / external validity / adjacent only`.

## CORE-L4-03 — Evidence blocker / queue
If unavailable full text or an appendix can change the decision, set:
`L4_STATUS=BLOCKED` and `L4_VERDICT=L4_BLOCKED_EVIDENCE`, then run targeted evidence unblocking.
If reasonable access routes are exhausted and the block cannot be resolved soon, use `L4_STATUS=PARKED_BLOCKED`. Parked is neither pass nor stop.
A blocked candidate need not prevent low-cost Focused Census work on other candidates, but it must be unblocked or parked before a new candidate consumes an active L4 slot.

## CORE-L4-04 — L4 status mapping
L4 status and verdict values must come from the Controlled Vocabulary Registry.

The key pre-screen / pre-formal routes are:

```text
L4_PASS_TO_METHOD_DESIGN
→ Method / Design / Pre-Outcome Identification Minimum

L4_NARROW
→ return to PRE_L4_CLAIM_FREEZE
→ revise the frozen claim
→ re-enter L4
```

`L4_NARROW` is not a pass.

Before a formal `L4_NARROW` or any `L4_BLOCKED_*` verdict, record the source tier under the L4 evidence-sufficiency rule. A source that is too weak or too indirect to support a narrowing or stopping claim is a verification lead, not a formal narrowing verdict. It must not silently shrink the frozen contribution claim. Adequately supported direct-collision evidence still proceeds to adjudication.

Do not emit logically contradictory combinations such as `COMPLETE + L4_BLOCKED_*`.

## CORE-L4-10 — Evidentiary symmetry for adverse literature judgments
A source used to reject, block, or narrow a research claim must be strong and direct enough to support the adverse proposition being asserted.

```text
COLLISION_EVIDENCE_TIER =
PEER_REVIEWED_CORE /
PEER_REVIEWED_ADJACENT /
CANONICAL_HIGH_QUALITY /
HIGH_AUTHORITY_FRONTIER /
LOW_AUTHORITY_FRONTIER /
SEARCH_PROCESS_ONLY /
NOT_APPLICABLE
```

The rule is not "working papers never matter." A high-authority frontier paper can establish a direct collision when the relevant claim and evidence are actually available and sufficient. The rule is instead: weak or merely neighboring material cannot be promoted into a formal claim-narrowing verdict that it does not support.

### Required consequences

- Evidence that is below the level needed for the adverse proposition cannot trigger formal `L4_NARROW`, `L4_BLOCKED_*`, or claim shrinkage.
- Record such material as a verification lead/unresolved evidence with an explicit unblock condition.
- Direct, sufficiently supported collision evidence still requires formal contribution adjudication; inconvenient evidence cannot be ignored.
- `SEARCH_PROCESS_ONLY` evidence can show what the search did or did not find. It cannot establish "world first" or "already done" by itself.
- Dangerous-neighbor-first is a prioritization rule, not a presumption of guilt.

This rule resolves the evidence-sufficiency boundary between `CORE-L4-04` and `CORE-L4-10` without changing the direct-collision adjudication standard.

## CORE-L4-05 — L4 evidence package
A full L4 review normally retains:
`deep read / bibliography / collision matrix / version chain / citation chase / source map / entitlement audit / decision`.

`L4_SOURCE_MAP` contains at least:
`candidate_id / claim_id / claim_text / source_id / source_role / source_version / evidence_locator / support_level / notes`.
Use explicit `NOT_APPLICABLE` or `NOT_AVAILABLE`; do not communicate status by silently omitting a file.

## CORE-L4-06 — One-candidate L4 + last-mile
After Census, prefer deep review of one candidate at a time to reduce wasteful parallel work.
At the start of L4, run a last-mile direct-collision search using the frozen exact claim. This is not a rerun of Landscape discovery.

## CORE-L4-07 — Incremental unblock
When a blocked full text is obtained, update only the affected evidence objects, such as bibliography, version chain, collision matrix, deep read, decision, and source map.
Do not rerun the full Census unless the new evidence changes the Core literature ecology.

## CORE-L4-08 — Pre-Formal L4 Recheck: Freshness Sentinel First
Set `L4_PHASE=PRE_FORMAL_RECHECK` for this transition check. Its purpose is to confirm that, after a surviving screen or other allowed pre-formal path, literature freshness and the implemented measurement/estimand have not created a new collision. It is not a default instruction to rerun all of L4.

Eligible entry requires a surviving screen verdict or another explicitly allowed survivor state. Inputs include the frozen pre-formal claim, the prior search cutoff and dangerous neighbors, the implemented measurement and estimand identities, and the Seen Data Register.

Record:

```text
PRE_FORMAL_L4_MODE =
SENTINEL_ONLY
FULL_UPDATE
RETURN_FOR_REFREEZE
```

Use `RETURN_FOR_REFREEZE` when continuation requires a substantive change to actor, core construct, estimand, treatment, primary outcome, or core identification. Mark `CLAIM_DRIFT=YES` and return through the state machine or create a new branch. Do not disguise a new study as an L4 update to the old one.

`SENTINEL_ONLY` is the default when the prior L4 review remains recent enough for the field, construct and estimand are unchanged, the implemented measurement stays within the frozen construct, and no new highly related literature or institutional/technical change is known. The sentinel must at least check post-cutoff freshness, versions/same-author/forward-citation routes for dangerous neighbors where observable, and direct collision using the actual measurement or estimator name.

Use `FULL_UPDATE` when the prior review is stale for the field, measurement or estimator changes materially, a sentinel finds potentially decision-changing evidence, a dangerous neighbor has a new version or key appendix, or a new institutional/data/technical development changes the academic neighborhood.

Post-result firewall: freshness queries must not be chosen because of effect sign, p-value, or a favorable subgroup. New literature may change the claim ceiling, establish a collision, or change benchmark priority; it may not be used to rewrite the original confirmatory hypothesis because an observed result was inconvenient. Newly invented post-result mechanisms or analyses are `EXPLORATORY` or a new branch.

The exact calendar trigger is a project/field-specific freshness parameter, not a universal truth. A six-month trigger may be used as a default sentinel threshold only where appropriate and should be tightened or lengthened with documented field-specific justification.

## CORE-L4-09 — Literature-selection hurdle for heavily searched research universes

Trigger this rule when the proposed hypothesis comes from a research universe that has already been searched intensively, when the focused census shows many parallel candidate signals under the same mother problem, or when the contribution is mainly "one more variable that predicts X."

Record:

```text
LITERATURE_SELECTION_HURDLE_STATUS =
PASS / CONDITIONAL / BLOCKED / NOT_APPLICABLE
```

The purpose is to separate evidence for a candidate from selection into the candidate. Harvey, Liu, and Zhu (2016) show that conventional single-test significance thresholds can be too lenient in a heavily mined cross-sectional return-factor literature. Their published paper reports materially different benchmark t-statistics under different assumptions about the searched universe; therefore no single number is a universal ScholarOps threshold.

For the paper's 2012 calibrations, the following source-specific reference points may be recorded when the current problem is sufficiently comparable:

```text
Published-factor universe
  Bonferroni: about 3.78
  BHY at 1%: about 3.39
  BHY at 5%: about 2.78

Including estimated unpublished/failed tests
  Bonferroni: about 4.01
  Holm: about 3.96
  BHY at 1%: about 3.68
  BHY at 5%: about 3.18

Homogeneous post-2000 subset
  (124 factors; Fama-MacBeth; 1970–1995 coverage; Fama-French three-factor controls)
  Bonferroni: about 3.54
  Holm: about 3.20
  BHY at 1%: about 3.23
  BHY at 5%: about 2.67
```

`3.54` is the published Bonferroni value for the homogeneous subset.

Use these values only after mapping the current claim to the relevant search universe. The paper's abstract-level "t > 3.0" message is a broad warning, not a universal cut-off for every finance design.

Three boundaries are mandatory:

1. **This is a selection-layer adjustment, not a substitute for valid inference.** Harvey, Liu, and Zhu take the reported t-statistics in the literature as inputs; ScholarOps must still validate the current study's standard errors, dependence structure, clustering, measurement, and outliers under the relevant empirical rules.
2. **The paper's main tests are unconditional.** A condition-specific claim may require a different mapping and claim ceiling.
3. **Dependence matters.** Positive correlation among tests can make some multiplicity adjustments conservative; a larger factor count does not mechanically imply the most stringent independent-test threshold.

The paper also distinguishes theory-motivated candidates from purely empirical searches. Any relaxation on that basis requires a documented construct/theory mapping under `CORE-M01`; it is not a free exemption.

When triggered, choose at least one defensible response and record it in the L4 source map: a literature-selection-aware evidence hurdle, genuinely independent validation, or a lower claim ceiling that explicitly acknowledges selection from a searched universe.

## J. Skill governance

## CORE-GOV01 — Skill anti-bloat
Classify each newly observed problem as:
`candidate-specific / family / agenda or profile / general rule / state-schema bug`.
Promote a rule into Core only when it is general/state-structural or recurs across independent projects. Candidate-specific handling belongs in the project's Method Freeze.
