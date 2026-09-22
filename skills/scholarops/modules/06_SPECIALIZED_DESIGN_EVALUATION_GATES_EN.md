# 06 — Specialized Design and Evaluation Gates


## A. Task ecology / evaluation

## SPEC-TASK01 — Task Ecology Validity
For research centered on tasks, benchmarks, or agent experiments, record:
`REAL_WORLD_TASK_POPULATION / TASK_SAMPLING_FRAME / TASK_SELECTION_RULE / TASK_DIFFICULTY_DISTRIBUTION / PROFESSIONAL_RELEVANCE / EXTERNAL_VALIDITY_LIMIT`.

If the study selects only tasks that an AI system can easily perform or that the researcher can conveniently score, the resulting evidence can support a benchmark claim at most. It does not automatically support claims about occupations, production functions, or overall financial-research quality.

## SPEC-EVAL01 — Evaluation Anchor Classes
Classify the evaluation anchor as one of:

```text
DETERMINISTIC_AUDITABLE_KEY
REALIZED_OUTCOME_LOSS
EXPERT_OR_MODEL_JUDGEMENT
```

A realized EPS or return is an observed economic outcome, not a deterministic ground-truth key. Expert or model judgments do not become objective merely because the evaluation is blinded.

For each task, record:
`EVALUATION_ANCHOR_CLASS / KEY_CONSTRUCT_VALIDITY / NOISE_OR_DISAGREEMENT / CLAIM_ALLOWED`.

## SPEC-SCORE01 — Scorability / Selection
If the study retains only scorable tasks in order to obtain an objective key, record:
`task frame / scorable classes / nonscorable classes / economic importance of excluded tasks / claim ceiling`.

If the true denominator of the real-world task population is unavailable, set `SCORABLE_TASK_SHARE=NOT_ESTIMABLE_PRE_DATA` and mark the gate `CONDITIONAL` with `CONDITION_TYPE=SCOPE_LIMITED`.
Do not invent a share or percentage.

## SPEC-ERR01 — Error-taxonomy provenance
Error categories must come from a professional workflow, institution, theory, or prespecified taxonomy.
Do not inspect candidate errors and then invent categories to explain the observed result. Any taxonomy added after outcome inspection is `EXPLORATORY`.

## B. Human subjects / labels

## SPEC-HUMAN01 — Human-subjects Reality
First classify `HUMAN_SUBJECTS_REQUIRED` as `YES / NO / CONDITIONAL`.

If `NO`, do not add participants merely to make the design look more like an experiment.

If `YES` or `CONDITIONAL`, check before execution:
`ethics / approval timeline / recruitment / target population / expertise / incentives / platform / data protection / attrition / realistic sample capacity`.

Do not fabricate power calculations before the design is sufficiently specified. If the design is not yet frozen, record `CONDITIONAL` with `CONDITION_TYPE=PENDING_USER_DECISION`, state why power is not yet estimable, and report the realistic recruitment range instead.

## SPEC-HUMAN02 — Expert-label scarcity
If an expert answer key is required, specify:
`who the experts are / recruitment / blinding / reproducibility / disagreement adjudication / cost`.

If expert labels cannot scale reliably, prefer an objective finance outcome or a rule-based key where scientifically valid. Otherwise lower executability or the claim ceiling rather than pretending the labels are readily available.

## C. Treatment identity / resource budget

## SPEC-TRT01 — Treatment Identity
When estimating the marginal value of a workflow component, freeze the `TARGET_ESTIMAND` before results.

Treatment and control should, as far as the design permits, hold constant:
`base model / raw information set / generation stage / time / token budget / source quality / interface / human expertise / incentives`.

Any dimension that cannot be held constant must be described as part of a joint treatment. Do not call “more information + more time + more verification” a pure verification effect.

## SPEC-COST01 — Resource Vector / Cost-Quality
Treat cost as a multidimensional resource vector by default:
`wall-clock time / model calls / tokens / retrieval effort / paid API usage / human minutes / expert minutes / failure or abstention cost`.

At minimum, report:
1. quality at a fixed resource level;
2. the full resource vector;
3. the cost-quality frontier when it is relevant.

A monetized total cost may be reported only when prices, wage rates, dates, and aggregation weights were frozen before results. Do not arbitrarily add unlike resource units.

## SPEC-COST02 — Economic decision mapping
A cost-quality result becomes an economic research object only when it maps to a clear resource-allocation problem:
`actor / budget / available options / loss from error / marginal cost / marginal gain / decision rule / counterfactual`.

If the surviving claim is merely “engineers who perform more checks make fewer mistakes,” classify the result as a tool or engineering contribution rather than an economic contribution.

## D. Base scope / extensions

## SPEC-SCOPE01 — Base Scope First / No Extension Rescue
Before L4, state `BASE_SCOPE` and `EXCLUDED_EXTENSIONS`.

If the base study fails on collision, So-What, or construct identity, do not rescue it after the fact by adding a human arm, multi-agent setup, behavioral extension, or other substantive extension.
A substantive new extension is a new branch and must re-enter the relevant gates.

## E. Robustness / sensitivity

## SPEC-ROB01 — Main specification integrity
Once the formal main specification is frozen, robustness analyses must not silently replace it.

For sensitivity or fragility studies, prefer one-change-at-a-time perturbations and compare them with natural noise or a reasonable benchmark where available.
A post-result robustness analysis that materially changes the core claim must be labeled exploratory or moved to a new branch rather than rewriting the confirmatory main specification.
