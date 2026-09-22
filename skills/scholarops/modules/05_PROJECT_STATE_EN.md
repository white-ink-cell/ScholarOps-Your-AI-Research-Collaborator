# 05 — Project State and Isolation


## PROJ-01 — Project state schema
Each active project should record, when relevant:

```text
PROJECT_ID
PROJECT_STATUS
AGENDA_ROLE
CURRENT_QUEUE_ROLE
LAST_COMPLETED_GATE
CURRENT_IN_PROGRESS_TASK
ALLOWED_NEXT_GATE
CURRENT_CANONICAL_ARTIFACT
SEEN_DATA_BOUNDARY
```

If a project regresses to an earlier stage, record:

```text
STAGE_REGRESSION_REASON / EVIDENCE / SUPERSEDES
```

Project state must not be overwritten by a newly generated landscape table, a chat summary, or the state of another project.

## PROJ-02 — Project-specific values live outside ScholarOps Core
Event universes, provider admissions, measurement thresholds, screen/pilot results, data versions, code versions, freezes, failure diagnoses, and current empirical results belong to the project artifact set. ScholarOps defines the schema and governance, not the user's project values.

## PROJ-03 — Project isolation
Different research projects must not inherit one another's status, results, freezes, Seen Data state, claims, or failure verdicts.

When a data asset is reused, record `ASSET_REUSED=YES` and make clear that only the asset is reused. No project result or design state is inherited automatically.

## PROJ-04 — Inactive, blocked, held, and closed projects remain isolated
An inactive, blocked, held, or closed project does not block low-cost discovery for a different project. If it is reconsidered, restore its own prior stage and blocker rather than restarting it as if no prior work existed or inheriting another project's current state.

A `CLOSED_PROJECT` cannot silently re-enter the active pipeline. Reopening requires a documented reopen condition and new evidence that satisfies it.

## PROJ-05 — Generalized multi-project roles
When several research efforts are managed at once, keep roles such as the following separate:

```text
PRIMARY_PROJECT
ACTIVE_CHALLENGER
ALTERNATIVE_PROJECT
LONG_HORIZON_RESEARCH_AGENDA
HOLD_FOR_FUTURE_DATA
CLOSED_PROJECT
```

A literature map or candidate scan does not automatically replace the primary project. A project switch requires a separate comparison of the research problem, contribution, evidence maturity, executability, time cost, and fallback value.

## PROJ-06 — Cross-project asset reuse
Before reusing an asset across projects, check:

```text
identity / date range / construct compatibility / point-in-time legality /
hash-or-reference / licensing
```

Asset reuse does not imply that measurement, sample construction, estimand, or treatment rules are transferable without a separate decision.
