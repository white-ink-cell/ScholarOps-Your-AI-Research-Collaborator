# ScholarOps Runtime Reference — 1.0.0

> Generated from the repository source spec. Do not edit by hand.

## Workflow shorthands
- `RE` → PROJECT_STATE_RECOVERY: Recover canonical project state from structured state and registered artifacts; consult archived conversation evidence only when needed; do not auto-advance when RE is the only request.
- `AU` → CURRENT_WORKFLOW_AUDIT: Audit the current research workflow and identify the earliest material gap or inconsistency; do not auto-advance when AU is the only request.

## Precedence

`CANONICAL_VERSION_RESOLUTION` → `RE` → `AU` → `CONCRETE_RESEARCH_TASK`

## Empirical execution classes

- `TECHNICAL_PROBE`
- `PREOUTCOME_MEASUREMENT_VALIDATION`
- `OUTCOME_DECISION_SCREEN`
- `FORMAL_STUDY`

## Runtime registries

- `runtime/CANONICAL_STATE_MACHINE.csv`
- `runtime/CONTROLLED_VOCABULARY_REGISTRY.csv`
- `runtime/TASK_ROUTER.csv`
- `runtime/GATE_ACTIVATION_POLICY.csv`
- `runtime/RULE_LOCATOR_INDEX.csv`
- `references/METHOD_SOURCE_REGISTRY.csv`
