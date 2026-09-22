# 06 — Specialized Design and Evaluation Gates（简体中文正式译本）

> 英文 `06_SPECIALIZED_DESIGN_EVALUATION_GATES_EN.md` 是唯一 canonical semantic source。

## A. Task ecology / evaluation

## SPEC-TASK01 — Task Ecology Validity
对于以 tasks、benchmarks 或 agent experiments 为核心的研究，记录：
`REAL_WORLD_TASK_POPULATION / TASK_SAMPLING_FRAME / TASK_SELECTION_RULE / TASK_DIFFICULTY_DISTRIBUTION / PROFESSIONAL_RELEVANCE / EXTERNAL_VALIDITY_LIMIT`。

如果研究只选择 AI 容易完成或研究者容易评分的任务，所得证据最多支撑 benchmark claim，不能自动外推到 occupations、production functions 或整体金融研究质量。

## SPEC-EVAL01 — Evaluation Anchor Classes
将 evaluation anchor 分类为：

```text
DETERMINISTIC_AUDITABLE_KEY
REALIZED_OUTCOME_LOSS
EXPERT_OR_MODEL_JUDGEMENT
```

已实现 EPS 或 return 是 observed economic outcome，不是 deterministic ground-truth key。Expert/model judgement 不会因为 evaluation 被 blinded 就自动变成客观真值。

每个 task 记录：
`EVALUATION_ANCHOR_CLASS / KEY_CONSTRUCT_VALIDITY / NOISE_OR_DISAGREEMENT / CLAIM_ALLOWED`。

## SPEC-SCORE01 — Scorability / Selection
如果为了获得 objective key 而只保留可评分任务，记录：
`task frame / scorable classes / nonscorable classes / economic importance of excluded tasks / claim ceiling`。

如果无法获得 real-world task population 的真实 denominator，设置 `SCORABLE_TASK_SHARE=NOT_ESTIMABLE_PRE_DATA`，并把 gate 标记为 `CONDITIONAL`，`CONDITION_TYPE=SCOPE_LIMITED`。不要编造比例或百分比。

## SPEC-ERR01 — Error-taxonomy provenance
Error categories 必须来自 professional workflow、institution、theory 或 prespecified taxonomy。
不能先看 candidate errors，再发明分类解释已观察结果。Outcome inspection 后新增的 taxonomy 必须标记 `EXPLORATORY`。

## B. Human subjects / labels

## SPEC-HUMAN01 — Human-subjects Reality
先把 `HUMAN_SUBJECTS_REQUIRED` 分类为 `YES / NO / CONDITIONAL`。

如果 `NO`，不要为了让设计“看起来更像实验”而人为加入 participants。

如果 `YES` 或 `CONDITIONAL`，执行前检查：
`ethics / approval timeline / recruitment / target population / expertise / incentives / platform / data protection / attrition / realistic sample capacity`。

设计尚未充分规定时，不要伪造 power calculation。若 design 还未 freeze，记录 `CONDITIONAL` 与 `CONDITION_TYPE=PENDING_USER_DECISION`，说明为何 power 尚不可估，并报告现实可行的 recruitment range。

## SPEC-HUMAN02 — Expert-label scarcity
如果需要 expert answer key，说明：
`who the experts are / recruitment / blinding / reproducibility / disagreement adjudication / cost`。

如果 expert labels 无法可靠规模化，且科学上可行，应优先使用 objective finance outcome 或 rule-based key。否则降低 executability 或 claim ceiling，而不是假装 labels 容易获得。

## C. Treatment identity / resource budget

## SPEC-TRT01 — Treatment Identity
估计某个 workflow component 的 marginal value 时，在看结果前冻结 `TARGET_ESTIMAND`。

在设计允许的范围内，treatment 与 control 应保持以下内容一致：
`base model / raw information set / generation stage / time / token budget / source quality / interface / human expertise / incentives`。

无法保持一致的维度必须作为 joint treatment 的组成部分说明。不能把“更多信息 + 更多时间 + 更多 verification”称为纯粹 verification effect。

## SPEC-COST01 — Resource Vector / Cost-Quality
默认把 cost 视为多维 resource vector：
`wall-clock time / model calls / tokens / retrieval effort / paid API usage / human minutes / expert minutes / failure or abstention cost`。

至少报告：
1. 固定 resource level 下的 quality；
2. 完整 resource vector；
3. 相关时的 cost-quality frontier。

只有 prices、wage rates、dates 与 aggregation weights 在结果前已经冻结，才能报告 monetized total cost。不得任意把不可比资源单位相加。

## SPEC-COST02 — Economic decision mapping
Cost-quality 结果只有映射到清楚的 resource-allocation problem 时，才成为 economic research object：
`actor / budget / available options / loss from error / marginal cost / marginal gain / decision rule / counterfactual`。

如果最终只剩“做更多检查的工程师更少犯错”，则归类为 tool/engineering contribution，而不是 economic contribution。

## D. Base scope / extensions

## SPEC-SCOPE01 — Base Scope First / No Extension Rescue
L4 前明确 `BASE_SCOPE` 与 `EXCLUDED_EXTENSIONS`。

如果 base study 因 collision、So-What 或 construct identity 失败，不能在结果后通过增加 human arm、multi-agent setup、behavioral extension 等实质扩展来“救”原研究。
实质新扩展是新 branch，必须重新进入相关 gates。

## E. Robustness / sensitivity

## SPEC-ROB01 — Main specification integrity
Formal main specification 冻结后，robustness analyses 不得悄悄替代主规格。

对 sensitivity / fragility study，优先 one-change-at-a-time perturbation，并在可能时与 natural noise 或合理 benchmark 比较。
结果后 robustness 若实质改变 core claim，必须标记 exploratory 或迁移到新 branch，不能重写 confirmatory main specification。
