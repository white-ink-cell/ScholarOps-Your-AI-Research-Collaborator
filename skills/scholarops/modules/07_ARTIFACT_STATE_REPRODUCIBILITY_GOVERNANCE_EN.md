# 07 — Artifact, State and Reproducibility Governance


## A. Artifact identity, fixity, and verification

## GOV-ART00 — Selective Hash / Fixity Policy
Hashing is not a ritual requirement for every intermediate file.

By default, hash or fingerprint two classes of assets:

1. **Milestone artifacts.** If the current delivery has a milestone class other than `NOT_APPLICABLE`, the canonical artifacts required by that milestone need fixity evidence.
2. **Non-regenerable inputs**, including:

```text
RAW_OR_EXTERNALLY_ACQUIRED_INPUT
NON_REGENERABLE_MANUAL_LABEL_OR_GOLD_DATA
```

These inputs require special treatment because they cannot be recreated from `raw + frozen code` even when they are not themselves milestone deliverables.

Files that are mechanically regenerable from `raw + frozen code`, such as scratch files, caches, temporary merges, ordinary diagnostic tables, and disposable intermediates, do not require individual hashes by default.

Upgrade an intermediate to a hashed asset when it is reused directly by downstream formal results, is costly or impossible to regenerate, or carries a material version-confusion risk.

Principle:
`fixity effort ∝ irreproducibility or version-confusion risk`.

## GOV-ART01 — Artifact identity
Deduplicate artifacts using:
`canonical location / hash / content identity`.

Allowed states:
`ORIGINAL / RESTORED / GENERATED_LATER / MISSING / SUPERSEDED`.

Do not infer identical content merely because two files have similar names.

## GOV-ART02 — Verification reuse / re-check triggers
`GOV-ART00` controls verification intensity; this rule controls verification frequency.

Core principle:

> A recorded verification remains valid within its stated scope until a re-verification trigger occurs. Re-verification is triggered by change, not by the fact that a new task has begun.

Repeatedly redoing file identity, parsing, or field checks on unchanged data is not additional rigor; it multiplies fixed cost without adding evidence.

First classify asset mutability:

```text
ASSET_MUTABILITY = FROZEN_SNAPSHOT / LIVE_SOURCE / UNKNOWN
```

- `FROZEN_SNAPSHOT`: content and location are fixed and a hash has been recorded; prior verification may be reused within scope.
- `LIVE_SOURCE`: an API, live database query, shared location that others may overwrite, or rolling directory; prior verification cannot be assumed to remain valid.
- `UNKNOWN`: treat as live until classified during the current task.

If the same live asset is repeatedly reused, the preferred fix is often to freeze a snapshot and record its hash rather than accept repeated full verification forever.

Re-verify when any of the following occurs:

```text
1  current file hash differs from verified_hash
2  version, vintage, or period changes, including vendor restatements or redownloads
3  canonical location changes and content identity is not established by hash
4  the current use exceeds verification_scope
5  schema, parser, code, or toolchain used to read the asset changes
6  an evidence error or claim drift is discovered
7  no verification record or verified_hash exists where one is required
8  ASSET_MUTABILITY=LIVE_SOURCE
```

Verification scope must be stated in a way that later users can compare against the new use. “Verified” without a defined scope is not reusable verification.

Record one of:

```text
FIRST_VERIFICATION
REUSED_UNCHANGED
REVERIFIED_TRIGGERED
BLOCKED_UNVERIFIABLE
```

`REUSED_UNCHANGED` may skip repeated parsing and profiling, but it does not skip identity comparison.
`BLOCKED_UNVERIFIABLE` may still permit exploration, but the asset cannot support formal results unless the freeze layer explicitly resolves or accepts the limitation.

Interfaces:
- `GOV-ART00` determines whether a hash should exist;
- `GOV-ART01` supplies location/hash/content identity;
- prior-asset resolution should hand candidate artifacts to this rule rather than automatically repeating full QA;
- completed verification is completed work and must not regress merely because a new task begins.

## GOV-PATH01 — Location identity
Use the controlled `PATH_TYPE` vocabulary.
For an unknown location, record:
`UNKNOWN — DO NOT GUESS`.

## B. State and registries

## GOV-STATE02 — Stage non-regression
A completed gate does not regress because a new conversation or summary begins.
Return to an earlier stage only for:
`evidence error / claim drift / superseding artifact`,
and record:
`reason / evidence / supersedes`.

## GOV-REG01 — Registry Identity / Drift
Project IDs must align across master registry, lineage, and current state.
An ID with no documented provenance is `UNREGISTERED_CANDIDATE` or `DISCOVERY_ID`; do not silently promote it to the formal primary project.

## GOV-REG02 — Registry minimum schemas
Maintain at least the following logical schemas when the corresponding governance risk is active.

### PROJECT
`project_id / project_status / agenda_role / queue_role / last_gate / next_gate / canonical_artifact / updated_at`

### DATA ASSET
`asset_id / source / version / period / fields / unit / location_type / location / hash / acquisition / reuse / asset_mutability / verified_at / verified_hash / verification_scope / verification_result`

The final five fields provide the landing place for `GOV-ART02`; without them, verification cannot be reused safely.

### ACCESS
`provider / source / entitlement / history / API_UI_bulk / cost / usability / tested_at / verification`

### SEEN DATA
`candidate / dataset / outcome_or_effect_seen / what_seen / when / by_whom / consequence`

### LITERATURE
`source_id / bibliographic identity / version / source_role / authority / candidate / read status`

Extend registries through schema extension. Do not create ad hoc near-synonym columns to bypass the canonical schema.

## C. Upstream packages and schema migration

## GOV-UP01 — Upstream transition audit
Before moving to the next gate, inspect the actual upstream package:
`manifest / canonical files / required audit files / freeze / source map`.
Do not rely on a README sentence that merely claims completion.

## GOV-UP02 — Schema migration
If an old package is missing only a column name, normalized row, or a field that can be reconstructed losslessly from existing evidence, a `SCHEMA_ONLY_REPAIR` is allowed together with a migration/supersession map.

For values that were never evidenced, use `NOT_RECORDED` or `NOT_OBSERVABLE`; do not guess.
If the missing item is substantive completion evidence rather than schema form, keep the prior stage and repair only the exact evidence gap.

## D. Claim drift

## GOV-DRIFT01 — Claim-changing return
If continuing after an L4, Method, or Pilot repair requires changing the:
`actor / estimand / field wedge / evaluation anchor / base scope / claim ceiling / core treatment`,
set:

```text
CLAIM_DRIFT=YES
RETURNED_FOR_REFREEZE
```

and record:
`old claim → trigger evidence → proposed new claim`.

Do not change the study while continuing through the old gate as if the original claim were unchanged.

## E. Seen Data

## GOV-SEEN01 — Seen Data Register
Record any result that can consume confirmatory flexibility, including treatment coefficients, event-time outcome plots, treatment-group summaries, high/low-exposure outcome differences, candidate outcomes after alternative cleaning, and pilot progression results.

Legal blind diagnostics at B0/B1 are not automatically effect-seen events.
Once an effect is seen, renaming or moving the file does not restore blindness.
Opening the effect also sets the irreversible-action status required by the governance layer; a later execution failure does not undo the fact that the result was observed.

### Seen status is scoped
Each record must state which outcome family, module, and units were seen.
Opening one module does not automatically destroy blindness for a genuinely unseen sister module. Conversely, an ambiguous scope is treated conservatively.

### Recording is not error-rate repair
The register documents consumed flexibility; it does not restore type-I-error control. “It was logged” is not a basis for treating already-seen data as confirmatory. Any legitimate reuse must follow a prespecified reuse design rather than retrospective bookkeeping.

### No unseen units means no new out-of-sample confirmation
If a provider, stratum, or subsample contains no unseen units, it may still supply development or descriptive evidence, but it must not be described as a new out-of-sample confirmation layer. Previously seen units may be reported separately but cannot be merged into a new confirmatory sample and counted as fresh evidence.

## F. Reproducibility and replicability

## GOV-REP01 — Reproducibility
Reproducibility asks whether the same data, code, and conditions can regenerate the same result.
Formal results must be traceable at least along:
`Result → Code → Processed Data → Raw or Source Data`.

## GOV-REP02 — Replicability
Replicability asks whether new data, a new sample, or an independent implementation addressing the same scientific question yields a consistent result or an interpretable difference.
A high-value replication of an influential claim may itself be a scientific contribution and must not be terminated automatically merely because the broad question is the same.

## G. Delivery and task closure

## GOV-CLOSURE01 — Task Closure Self-Validation
Apply the invariant:

```text
CLAIMED_COMPLETE ≤ VERIFIED_COMPLETE
```

A conversational statement that work is complete cannot exceed the actual verification status.

### Ordinary delivery
Use `TASK_CLOSURE_DEPTH=LIGHT`. No dedicated closure artifact is required; the agent performs the relevant checks before the final response.

### Milestone delivery
Use `TASK_CLOSURE_DEPTH=MILESTONE` when a milestone class is active. The milestone should retain or update enough evidence to demonstrate completion, including execution/result artifacts, necessary QA, current state/verdict, and any manifest/hash/package required by the milestone.
Do not create a redundant long “self-check report” when existing QA and logs already prove the same point.

### Repair closure
Any result- or state-changing modification made after the last validation invalidates the earlier closure pass. Set `REVALIDATE_AFTER_LAST_CHANGE=YES` and validate the final post-change version before delivery.

## GOV-DELIV01 — Milestone-Triggered Deliverable
For an ordinary intermediate task, QA check, or one-off diagnostic, default delivery is:
- the code actually used, where relevant;
- result tables, figures, or logs;
- a short note stating the input, action, finding, and next step.

Do not require the full `README + MANIFEST + SHA256SUMS + ZIP` bundle for every intermediate task.

For an actual milestone, produce the complete release-style package required by the milestone, including canonical Markdown, necessary CSV/JSON logs, README, manifest, hashes for assets selected under `GOV-ART00`, and a ZIP or equivalent bundle where appropriate.
Do not individually hash every mechanically regenerable intermediate.

Package names should remain identifiable outside the conversation, for example:
`project_stage_purpose_date_version.zip`.
A manifest must not self-reference the ZIP that contains it.

## GOV-DELIV02 — Completion summary
At the end of a formal research task, report:
`VERDICT / ALLOWED_NEXT_STEP / FORBIDDEN_NEXT_STEPS / REGISTRY_UPDATES`.
`ALLOWED_NEXT_STEP` must contain one next action, not an unprioritized list.
Ordinary explanatory Q&A does not require the full state template.

## H. Failure assets and reopening

## GOV-FAILASSET01 — Failure Asset Extraction
A terminated research branch is not erased. It enters the terminated-branch archive rather than disappearing from project history.
This applies to research-census termination, L4 termination, a screen decision to stop allocating resources, and structurally blocked access when the branch is being closed.

The archive records at least:

```text
TERMINATION_REASON
FAILURE_CLASS
TERMINATION_STAGE
EVIDENCE_SNAPSHOT
SEEN_DATA_STATUS
REUSABLE_ASSETS
COOLDOWN_KEY
REOPEN_CONDITIONS
TERMINATED_BRANCH_FINGERPRINT
TERMINATION_ARCHIVE_STATUS=COMPLETE
```

`COOLDOWN_KEY` must identify the stable claim or estimand, not a display name. Renaming a failed idea must not bypass the cooldown.
One pass of reusable-data/code/method/source extraction is allowed after termination. Reusable assets do not automatically reopen the terminated hypothesis.

## GOV-COOLDOWN01 — Reopen
When a claim/estimand has accumulated the required termination history, check the terminated-branch archive by `COOLDOWN_KEY` before restarting a similar candidate.
Ask mechanically whether this is a legitimate reopen supported by new evidence or merely the same terminated idea under a new name.

A reopen requires an auditable trigger such as new data, a new shock, stronger identification, construct correction, adjudicating evidence, mechanism, boundary condition, regime change, or high-value replication opportunity, and must record whether the prespecified `REOPEN_CONDITIONS` are met.
Do not continue speculative data expansion after closure when no surviving research question requires it.

## I. Research-relevant QA

## GOV-QA01 — Research-relevant QA
Only QA that can affect the research conclusion, data integrity, citation traceability, or file readability changes the research verdict.
Browser quirks, styling, and presentation-only issues are tracked separately and do not change a research gate by themselves.

## J. Skill release identity and validation

## GOV-VERSION01 — Skill release identity / fixity
A ScholarOps release is itself a traceable artifact.
Each stable release records release metadata and a canonical fingerprint whose algorithm and scope are defined by the public maintenance specification. Declared fingerprints are never trusted merely because they are written down; validators recompute them and compare values mechanically.

The fingerprint is for version identity and fixity, not a general anti-tamper security guarantee. If multiple copies with the same nominal version exist, differing content must produce a different identity so the canonical-version decision does not depend on modification time or visual inspection.

Release metadata stores identity facts, not a self-issued validation certificate. The object being validated must not certify itself as valid.

Once a version is publicly released, do not silently modify its contents. Any content change requires a new release version. This immutability principle is consistent with Semantic Versioning 2.0.0 section 3. ScholarOps' own major/minor/patch policy, fingerprint algorithm, and manifest rules are local engineering choices and must not be attributed to SemVer.

## GOV-VERSION02 — Stable release requires validator PASS
A release may be marked stable only after all required release checks for the current public architecture pass, including:
- structural validation;
- semantic-invariant validation;
- recomputation of the canonical fingerprint;
- regeneration of manifest/checksum material after the last in-package modification;
- a final check-only validation pass;
- detached attestation of the final immutable package, including the final validator result and package checksum where the release process uses such a bundle.

Do not publish a known-failing stable package with a promise to repair it in a later release.
