# 02 — Empirical Data, Pilot, Screen & Formal Methods（简体中文正式译本）

> 英文 `02_EMPIRICAL_DATA_PILOT_METHODS_EN.md` 是唯一 canonical semantic source。本译本用于中文阅读；Rule ID、字段、状态、公式与 controlled vocabulary 保留英文规范形式。

## A. Empirical execution class 与进入条件

## EMP-GATE00 — Empirical Execution Class / Risk Trigger Router
进入实证工作前记录一种 execution class：

```text
EMPIRICAL_EXECUTION_CLASS =
TECHNICAL_PROBE
PREOUTCOME_MEASUREMENT_VALIDATION
OUTCOME_DECISION_SCREEN
FORMAL_STUDY
```

### TECHNICAL_PROBE
优先使用 synthetic、dummy 或非候选输入，只验证 API/schema/parser/file/identifier/rate-limit 等技术行为。它不推进 research state machine，不要求 Freeze A、economic threshold、multiplicity treatment 或 B3 effect-open，也不产生 `SCREEN_VERDICT`。

### PREOUTCOME_MEASUREMENT_VALIDATION
这是 ScholarOps 中的 feasibility/measurement pilot。可以使用候选 observations，但 research effect 必须在 B0–B2 保持 masked。它属于 measurement-validation stage，不产生 screen verdict。Pilot/feasibility 的一般思想来自相关方法文献，但金融/商科工作流是 ScholarOps 的适配，而不是临床试验规则的直接照搬。

### OUTCOME_DECISION_SCREEN
这是可选的 effect-open 资源分配 screen，不是必做步骤。唯一目的，是依据 prespecified progression criteria 决定是否继续投入研究资源。B3 前必须冻结 screen-data reuse policy 与 progression criteria。它可产生 `SCREEN_STATUS` 与 `SCREEN_VERDICT`，但不能证明 economic effect 不存在。

### FORMAL_STUDY
正式 confirmatory/economic inference 只有在 formal main specification 冻结后才能开始。Equivalence、minimum-effect 与 economic-null claim 属于这里，而不是小型 outcome screen。

Risk gate 只在实质 trigger 出现时激活，例如 economic-threshold、within-study multiplicity、specification-search、screen-reuse、missing-data、influence-audit、post-clean QA。未触发 gate 记录 `NOT_APPLICABLE`；不要为了证明 gate 存在而生成空 artifact。

## EMP-ENTRY01 — 结果前的 empirical entry anchor
如果 pipeline 的入口没有被执行，pipeline 本身没有意义。

在生成任何可被理解为研究结果的 estimate 前，例如 coefficient、test statistic、portfolio return、Sharpe ratio、model-performance metric 或 event-window effect，记录：

```text
EMPIRICAL_ENTRY_STATUS =
RESOLVED / UNRESOLVED_BLOCKED / USER_OVERRIDE_EXPLORATORY / NOT_APPLICABLE
```

Resolved entry anchor 只需简短记录：`current state / last upstream state supported by an artifact / supporting artifact`，不能把它做成高成本新审计包。

如果上游声称已经完成但没有 artifact 支持，设置 `UNRESOLVED_BLOCKED`，返回最早缺失 state，而不是“先跑一个版本看看”。

Data description 与 blind distribution review 先于 cleaning；cleaning/transform rules 必须在 estimation 前冻结。用户说“跑回归”并不自动豁免上游要求。

若用户明确要求跳过必要上游步骤，只能以 `USER_OVERRIDE_EXPLORATORY` 继续：记录跳过的 states，全部输出标为 exploratory，并把任何被打开的 effect 写入 Seen Data Register。

纯代码调试、data-dictionary lookup、method discussion 或不产生研究 estimate 的 literature work 使用 `NOT_APPLICABLE`。

## B. Execution responsibility 与 research code

## EMP-EXEC01 — Assistant-first execution
宿主能访问用户数据并执行操作时，Agent 应直接完成：
`QA / cleaning / merge / variable construction / descriptive statistics / panel build / validation / code execution / result packaging`。

只有 private account、institutional login、paid entitlement、local-only resource、CAPTCHA 或 connector 缺失真正阻塞时，才要求用户完成最小 acquisition step。

要求重新下载/重跑前，若宿主允许，应先检查现有 attachments、persistent project assets、data registries、caches、manifests 与 hashes。

## EMP-EXEC02 — Research code minimalism
使用现实可用的 execution environment。除非任务确实需要且用户/宿主政策允许，不要自行安装 packages、建立宽泛 compatibility layer 或修改用户环境。

避免：不必要自动安装、多个猜测性 import fallback、宽泛 `except Exception: pass`、silent field guessing、无 construct 依据把 missing 填 0、为未观察 schema 建巨大兼容分支。

优先：`explicit schema / dtype checks / hashes where relevant / assertions / fail-fast behavior / minimal repair after a real error is observed`。

## C. Data asset intake

## EMP-ASSET01 — Existing asset first
可复用 data asset 按需记录：
`DATA_ASSET_ID / source / version / time coverage / unit / fields / canonical or reference location / hash or identity evidence / acquisition provenance / reuse eligibility`。

不能因为 Agent 忘了已有 verified asset 就重新下载。

## EMP-ASSET02 — Acquisition scope follows estimand
获取数据前先定义：
`unit / target / frequency / dates / windows / fields / matching dependencies`。
默认策略不是“先尽量多下载”。

## D. Concrete-data escalation 与 raw-to-clean pipeline

## EMP-DATA00 — Concrete-data escalation
本模块提供一般 empirical skeleton，不是所有特殊数据的通用公式。

项目若存在本模块未明确覆盖的特殊 data structure、missingness、institutional semantics、ratio construction、human-AI data、event sampling、clustering 或 interference，设置 `CONCRETE_PROBLEM_SPECIAL_CASE=YES`，调用 `CORE-M01/M02`：检查真实数据和专业 precedent，映射 assumptions，并冻结项目专属规则。不得凭空发明数据语义，也不得机械外推教材 recipe。

## EMP-DATA01 — Raw Structural QA
Raw-data 阶段先修 data-identity 与 encoding 问题，不做 outcome-driven tail surgery。相关时检查：file identity/hash、schema/dtypes、date range、primary keys/duplicates、special missing codes、units/sign conventions/currency、impossible values、source seams、identifier/link validity、vendor-specific adjustment 与 corporate-action semantics。

存在 official data dictionary/transition guide 时，field semantics 必须以其为依据；教材不能替代 vendor semantics。记录 `RAW_DATA_QA_STATUS`。

## EMP-DATA02 — Construct-first variable definition
Variable formula 由 economic construct 与可信 precedent 决定，不由最容易下载的 field 决定。对 ratio、liquidity、turnover、volatility、text measure 等保留：
`raw components / denominator / unit / aggregation rule / point-in-time logic`。

## EMP-DATA03 — Derived Variable Construction
使用 canonical state `DERIVED_VARIABLE_CONSTRUCTION_STATUS`，以及需要时：

```text
COVARIATE_CONSTRUCTION_STATUS
EXPOSURE_CONSTRUCTION_STATUS
OUTCOME_CONSTRUCTION_STATUS
```

先按 frozen economic definition 构造变量，再进行完整 distribution/tail review。该名称替代只适用于部分场景的含糊“pretreatment variable construction”。

## EMP-DATA04 — Two-end QA sandwich
使用：

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

不得让 raw error 无检查地传递；final construct 尚未构造前，也不要先 winsorize/transform 它。

## EMP-DATA05 — Blind Distribution / Tail Audit
不打开 treatment effect，检查适合当前场景的 distribution diagnostics，至少包括 sample size、missingness、zeros、central tendency、dispersion、robust dispersion、skewness、kurtosis、extrema 与足够详细的 tail quantiles。

相关时检查时间稳定性或不会揭示 treatment effect 的合法 sample dimensions。异常 constructed value 必须做 `EXTREME_OBSERVATION_TRACE`，追溯到 raw components 与 event/entity identity。

## EMP-DATA06 — Outlier taxonomy / distributional tail
先在 variable/data 层分类 extreme observations：

```text
INVALID_CODE_OR_SENTINEL
UNIT_OR_SCALE_ERROR
DUPLICATE_OR_LINK_ERROR
INVALID_DENOMINATOR
CORPORATE_ACTION_OR_MECHANICAL_BREAK
TRUE_ECONOMIC_TAIL
UNKNOWN_REQUIRES_REVIEW
```

确认的数据错误应修正；真实 economic tail 保留 raw archive，是否 transform/tail-treatment 要结合 construct identity、vendor semantics、blind distributional evidence 与最终 estimator。

不要把这一层与 regression influence 混为一谈：经济上极端的值可能并不主导估计；influential observation 也未必是无效数据。

Bali, Engle, and Murray (2016, §1.2) 只能支持 winsorization/truncation 在 empirical asset pricing 中常见、且这种做法相对 ad hoc；不能证明某个固定 cutoff 正确，也不能把 1/99、0.5/99.5 等变成通用规则。

如果真正关心 estimator influence，使用 `EMP-INFL01`，不要把 winsorization/truncation 当成自动解决方案。

因此：

```text
winsorization/truncation != influence diagnosis
common practice != project-specific justification
```

任何 cutoff/transform 必须针对当前 construct 与 design 辩护。

## EMP-DATA07 — Cleaning / Transformation / Scale Decision
Cleaning/transform decision 应联合考虑：construct identity、canonical variable literature、vendor semantics、treatment-blind distribution evidence、适当阶段的 tail/influence diagnosis，以及最终 estimator 的要求/assumptions。

不同变量可以有不同处理。不能为了外观一致强迫所有 outcomes 使用同一 winsorization rate、log transform 或 pooled scale。

## EMP-DATA08 — Post-clean QA：由实际变化触发
记录：

```text
CLEAN_DATA_CHANGE_STATUS =
NO_DATA_CHANGE
VALUES_CHANGED
SAMPLE_CHANGED
TRANSFORMATION_CHANGED
AGGREGATION_CHANGED
MULTIPLE_CHANGES
```

Blind audit 若未导致 deletion、value modification、transformation 或 aggregation change，不要为形式对称重复完整 descriptive audit；只确认 input/output identity、row/entity count、schema 与 key coverage。

真正有变化时，重新运行受影响的 distribution、missingness、tail、balance、correlation、support、panel-cell checks。若变化产生新 discontinuity、sample collapse 或 construct drift，返回 `EMP-DATA07`。

原则：第二次 QA 验证真实变化，不是强制重复计算。

## EMP-DATA08A — Missing Data Cheap Triage
打开完整 missing-data gate 前，对 key variables 做低成本 triage：
`missing count / missing rate / always-missing entities / mechanically required history missingness / linkage missingness`。

如果 missingness 不存在、纯机械且按设计在 target sample 外，或明显不能改变 estimand、sample composition 或 key construct，记录：

```text
MISSING_DATA_STATUS=NOT_APPLICABLE
MISSING_FULL_AUDIT_TRIGGER=NO
```

只保留简短 triage 结果。

若有 non-mechanical missingness、entity/time blocks、linkage/source gaps、material complete-case selection 或需要 imputation，设置 `MISSING_FULL_AUDIT_TRIGGER=YES` 并进入 `EMP-DATA09`。

## EMP-DATA09 — Missing-data reality / selection / imputation gate
Missingness 不能用单一百分比概括。完整 gate 被触发时建立 `MISSING_DATA_MAP`，相关时区分：

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

每个 key variable 至少审计 observation-level missing rate、entity-level ever/always missingness、time pattern、可观察 missingness differences、complete-case sample loss、相关时 economically weighted loss，以及 sample composition change。

Little and Rubin (2020, 3rd ed., §3.2) 的核心边界是：complete-case analysis 的有效性取决于 missingness mechanism 与 estimand 的组合。在其示例中，如果 complete 与 incomplete units 的均值不同，complete-case mean 可有偏；但某些依赖 covariates、在给定 covariates 后不依赖 outcome 的 selection pattern 下，regression coefficients 仍可能无偏。因此 missing-data validity 是 **estimand-specific**，不是 dataset 的固定属性。

Little and Rubin (Chs. 4–5) 也区分 single imputation 与能反映 missing-data uncertainty 的方法。第三版把 multiple-imputation standard errors 描述为在较广类别 procedures 下 approximately valid，而某些 single-filled-data corrections 不具有同等普遍性。因此 ScholarOps 不把任何单一 imputation recipe 设为 universal default。

记录：

```text
MISSING_DATA_STATUS =
PASS / CONDITIONAL / BLOCKED / NOT_APPLICABLE
```

Generic missing-data principles 管 Core；特定 finance evidence 可加强特定应用，但不能超出 transfer scope 泛化。

`DROP_ALL_MISSING`、complete-case、zero imputation、median imputation、industry-median imputation 都不是普遍安全或普遍无效；必须结合当前 mechanism、estimand、timing 与 downstream analysis 论证。

## EMP-DATA09A — Imputation decision
若 missingness 与 estimand 无关，且有理由的 complete-case design 不改变 target population，可使用 `IMPUTATION_DECISION=NO_IMPUTATION`，但仍必须做 selection audit。

需要 imputation 时至少冻结：

```text
IMPUTATION_TARGET
INFORMATION_SET_AT_T
LOOKAHEAD_ALLOWED = NO / DIAGNOSTIC_ONLY
MODEL_FAMILY
FALLBACK_RULE
MASKING_VALIDATION_DESIGN
DOWNSTREAM_ESTIMAND_VALIDATION
```

Point-in-time pretreatment variables 的 formal imputation 不能使用未来信息；future information 只能作为清楚标记的 diagnostic upper bound。

这些字段是 ScholarOps 根据 missing-data principles 设计的 governance implementation，不是 Little & Rubin 原文逐字 prescription。

## EMP-DATA09B — Imputation validation
真实 missingness 具有结构时，不能只用 artificial MCAR random masking 验证 imputation。可行时模拟真实 process，例如 block missingness、entry/exit pattern、observable-characteristic-dependent masking、empirical propensity masking 或 documented source gaps。

验证层级至少包括：
1. value-level error，如 RMSE/MAE；
2. 研究依赖 rank 时的 ranking/quantile recovery；
3. **downstream estimand distortion**。

第三项按项目定义，例如：

```text
DID            -> treatment effect, pre-trends, sample composition
Event study    -> abnormal response and event aggregation
Asset pricing  -> risk premium and portfolio-sort implications
Forecasting    -> out-of-sample loss and ranking
```

Imputation prediction metric 好，不等于 downstream estimand distortion 低。
Masking design、validation outcome 与任何外部 missing-data method transfer 都要记录 assumptions 与 scope。

## EMP-DATA09F — Finance firm-characteristic special case
Bryzgalova, Lerner, Lettau, and Pelger 研究 asset-pricing 中 firm-characteristic panels 的 systematic missingness 及其对 risk premia、cross-sectional anomalies、portfolio construction 的影响，可作为 firm-characteristic missingness 可能系统性、complete-characteristic requirement 可能产生 material selection 的强领域证据。

Transfer scope 仅限 finance firm-characteristic panels，不是 arbitrary missing-data problems 的 universal authority。超出 setting 时记录 `PRECEDENT_TRANSFER_STATUS=TRANSFERABLE_WITH_ADAPTATION`，并按 `CORE-M01` 映射 assumptions。

该 RFS 来源的正式 DOI 为 `10.1093/rfs/hhae036`。

## E. Blind-analysis boundary

## EMP-BLIND01 — Four-level data-access firewall
使用四级访问：

### B0 — `STRUCTURE_ONLY`
允许 schema、identifiers、dates、coverage、units、missing codes、raw components、support counts；无需打开 research outcome values。

### B1 — `MARGINAL_OUTCOME_BLIND`
为了 data reality 可查看 outcome 本身的 marginal 或其他合法预先规定 distribution、tails、denominators、missingness 与 univariate extreme-value tracing。Treatment/event/exposure/hypothesis-group identity 必须 masked 或未 join，任何 grouping 都不能恢复 effect direction。

B1 不含 regression influence diagnostics。Cook's distance、DFFITS、DFBETA、leverage、robust-regression weights 依赖 fitted outcome model，属于 B3 后的 `EMP-INFL01`。

### B2 — `DESIGN_SUPPORT_EFFECT_MASKED`
可查看 exposure/treatment support、overlap、usable-sample counts、matching quality、independent variation unit counts 等 design-support structure，但 joint outcome-treatment/exposure relation 保持隐藏。不同 design 的 B2 实现不同；ScholarOps 不强制 event-study template。

### B3 — `EFFECT_OPEN`
首次允许揭示 joint outcome-treatment/exposure relation、treatment-group outcome summaries、event-time outcome plots、outcome-exposure association 或 formal effect estimate/test。

`BLINDNESS_LEVEL` 只能使用：
`B0_STRUCTURE_ONLY / B1_MARGINAL_OUTCOME_BLIND / B2_DESIGN_SUPPORT_EFFECT_MASKED / B3_EFFECT_OPEN`。

Blind-analysis literature 支持一般原则：仍存在 discretionary analysis choices 时，Analyst 应避免提前知道分析将回答的结果。四级 firewall 是 ScholarOps 自己的 workflow implementation，不是已发表 taxonomy。

## EMP-BLIND01A — Blinding 是原则，不是 event-study 模板
Blind analysis 是 bias-control principle：当分析选择仍有 discretion 时，避免用会引导这些选择的形式暴露 study answer。它不要求 event calendar。

Klein and Roodman 描述了多类 blind-analysis strategy，而非唯一强制实现。因此 ScholarOps 用 controlled field 记录 project-specific implementation：

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

允许 `NOT_FEASIBLE`，但必须记录原因并相应降低 claim/procedural protection；若强 masking 不可行但可在 effect inspection 前冻结 specification，可用 `LOCKED_SPEC_ONLY`。

Blinding 不是正确性的证明。Unblinding 后可以继续分析，但 effect seen 后首次产生的 decisions 必须记录为 post-effect decisions，并进入 Seen Data 与 Claim Drift governance。

## EMP-BLIND01B — Background familiarity ≠ effect-open
分别记录：

```text
BACKGROUND_DATA_FAMILIARITY =
NONE / GENERAL_DISTRIBUTIONAL / EXTENSIVE_PRIOR_USE
```

和：

```text
SEEN_DATA_STATUS =
NONE / BLIND_DIAGNOSTIC_ONLY / EFFECT_SEEN / UNKNOWN
```

熟悉 finance variable 的典型 distribution 属于 background familiarity，不自动构成 blindness failure。Blindness 针对当前 study answer，而不是研究者是否曾见过该变量。
只有观察当前研究的 joint outcome-treatment/exposure relation 才创建 `EFFECT_SEEN`。
Extensive prior use 会提高 stronger prespecification 或 `LOCKED_SPEC_ONLY` 的价值，但不自动阻止研究。

## EMP-BLIND02 — B3 前禁止的 leakage
B3 前即使没有跑回归，看到以下内容也属于 effect-open：treated-vs-control outcome summaries；event 周围 outcome paths；event-time-aligned outcome plots；high/low exposure outcome summaries；根据哪个 variant 产生更有利 event difference 来选择 winsorization/log/scale；因 coefficient sign/significance 改 cleaning、sample、window 或 threshold。

## EMP-BLIND02A — Analyst-coding blindness
Polit (2011) 记录了 data analyst 在 missing data、outlier/distribution、transformations、variable recoding/cutpoints、subgroups、covariates、repeated-outcome/endpoint、sensitivity/validity 等方面存在具有后果的 discretionary choices，并指出知道 treatment code 可能影响这些选择。

ScholarOps 明确以 adaptation 的方式把狭义 bias-control principle 扩展到 RCT 之外：当 empirical design 有 treatment/exposure identities 且 B1/B2 仍有 material analytic discretion 时，在可行范围内把 analyst 与 group semantic identity 分开。

操作上：脚本需要 group identifier 时优先 random/semantically neutral coding；真实 treatment/exposure mapping 分离保存；blind phase 所辖 primary choices freeze 后再 decode；B1/B2 根本不需要 identity 时，不为方便而 join。

本规则不声称每个 finance design 都是 RCT，也不声称 Polit 直接研究 finance；只迁移“当 comparison identity 会改变 discretionary choices 时，将两者分离”这一较窄原则。

## EMP-BLIND03 — Already-seen data
此前 pilot、conversation、report 或 analysis 已看到 outcome/effect 时，不得假装重新获得 blindness。
记录：

```text
SEEN_DATA_STATUS =
NONE
BLIND_DIAGNOSTIC_ONLY
EFFECT_SEEN
UNKNOWN
```

`BLIND_DIAGNOSTIC_ONLY` 表示只看了 blind boundary 允许的 diagnostics；`EFFECT_SEEN` 表示看过任何 B3 前禁止的 effect information。

合法补救可能包括 holdout、new events、new sample、masking 或 independent data manager 生成 blind diagnostics。忘掉、改名或移动旧结果不是补救。

## F. Aggregation、sample 与 measurement support

## EMP-PANEL01 — Aggregation 属于 measurement
把 daily/high-frequency data 转成 weekly、monthly 或 event-level panel 前冻结：
`zero vs missing / non-trading, halt, and holiday treatment / partial periods / minimum valid observations / sum vs mean vs median vs compounding / overlapping stock-week or event windows / numerator-denominator timing / generated-regressor leakage / within-between variation / fixed-effect support / residual dependence and cluster unit`。

Aggregation 是 construct measurement 的组成部分，不是中性的文件格式操作。

## EMP-PANEL02 — Effective information 不等于 raw row count
大 raw N 不等于大量 independent information units。

Wooldridge 的 cluster-sampling 讨论说明，尤其 key variation 在 cluster level 且 cluster 数少时，inference 可能主要受 independent clusters 数量限制；Hasbrouck 也指出 microstructure dataset 可以拥有大量 observations，却只覆盖数日或数月，而且 asymptotic approximation 仍依赖合理 model specification。

记录 `INDEPENDENT_VARIATION_UNIT`，例如：

```text
event / cluster / firm / date / provider / shock
```

并报告评估 design 所需的相应 counts。若 identifying variation 仅来自少数 events/dates/providers/clusters，不能用数百万高频 rows 为 conventional cluster asymptotics 辩护。

本规则讨论 effective independent variation 与 dependence structure，不给 universal minimum cluster count。

## EMP-SAMPLE01 — Four execution sample concepts
### TECHNICAL_PROBE_SAMPLE
使用能够暴露 schema/API/parser/file/identifier 技术问题的最小 heterogeneous sample；不要为它做 research-power calculation。

### PREOUTCOME_MEASUREMENT_VALIDATION_SAMPLE
围绕 coverage、classification、error、missingness 或 gold-label accuracy 所需精度选择 sample size，并考虑 rare classes 与 material heterogeneity；不能仅因少数 case 易检查就使用 convenience sample。

### OUTCOME_DECISION_SCREEN_DECISION_SAMPLE
围绕 prespecified progression/resource-allocation criterion 与作出 screen decision 所需精度设计。Screen criterion 可以有经济动机，但不是正式 `ECONOMIC_MINIMUM`、SESOI、equivalence bound 或 economic-null test。Formal economic-magnitude adjudication 属于 `FORMAL_STUDY`。不能为了让 resource screen 看起来 confirmatory 而强塞 SESOI。

### FORMAL_STUDY_SAMPLE
使用 formal power、precision 或 inference logic。Event universe 固定时，报告 attainable precision、MDE 或 power，而不是假装 N 可自由选择。

## EMP-SAMPLE02 — No rule-of-thumb N
不存在 12、30、40、100 之类 universal pilot sample size。Pilot/feasibility N 必须与 pilot objective 匹配。

`PREOUTCOME_MEASUREMENT_VALIDATION` 围绕 measurement target 论证 N；`OUTCOME_DECISION_SCREEN` 围绕 prespecified progression criterion 论证 N。两者都不能为了模仿 formal study 用 effect significance 当 stop rule。

## EMP-SAMPLE03 — Event-study / finance-specific calibration
Event-study 的 sample adequacy/power 由 effect magnitude、abnormal-return variance、event observations 数、event timing 与 sampling interval 共同决定。

Campbell, Lo, and MacKinlay (1997, Ch.4) 表明 power 会随 effect size、variance、sample size 变化；event timing 精确时，更短 sampling interval 可通过降低 abnormal-return variance 提高 power，而不是机械放大 effect；timing 不确定时可能需要更宽 event window；intraday design 还会引入 microstructure complications。

因此 event-study pilot/formal design 应使用 blind empirical variance、canonical event-study calculation 或 frozen design 下的 simulation 论证 sample/precision，不能只看 stock count。

## EMP-SAMPLE04 — Cluster/event count
Identifying variation 位于 event/provider/date/treatment-shock/cluster level 时，有效信息受这些 independent units 的数量与结构约束。

Wooldridge 的 small-G 讨论提醒：cluster 数小时，传统 cluster-robust asymptotics 即使 within-cluster N 大也可能缺乏依据；Hasbrouck 同样区分 observation count、calendar span 与 model-specification risk。

重要时 sample table 报告：

```text
raw rows / firms / dates / events / treatment shocks / clusters
```

不得变成 arbitrary universal cluster-count cutoff；具体 inference 要针对实际 dependence structure 辩护。

## EMP-SAMPLE05 — Required artifact
当 sample size/precision 会改变 execution decision 时，创建 execution-sample/precision justification，至少包括 execution class、objective、target estimand/feasibility parameter、independent variation unit、与目标匹配的 precision target、相关时 variance/source、N/events/clusters、相关时 analytical/simulation method、constraints，以及为什么 sample 对所声称目标足够。

对 `OUTCOME_DECISION_SCREEN` 记录 prespecified progression/resource criterion 及作出资源决策所需 operating characteristics。只有 `FORMAL_STUDY` 真正裁决 economic magnitude 时，才需要正式 `ECONOMIC_MINIMUM`、SESOI、equivalence bound 或 economic-null operating characteristic。不要为了外观给 technical probe、measurement validation 或 resource screen 附无关 SESOI。

## G. Failure、repair 与 identification

## EMP-FAIL01 — Failure classification
使用单一受控 `FAILURE_CLASS` taxonomy。

Project-level conceptual：`NOVELTY_OR_REDUNDANCY`、`SO_WHAT_OR_CONCEPTUAL`，可在 pilot 前终止 branch。

Execution/input：`ACCESS / IMPLEMENTATION / DATA_IDENTITY / DATA_QUALITY`，这些本身不能支持 economic verdict。

Measurement/support：`MEASUREMENT / SAMPLE_SUPPORT_OR_PRECISION / CONSTRUCT`。先诊断 measurement/precision；改变 construct 的 repair 要重新 freeze 或创建新 branch。

Design/inference：`IDENTIFICATION / ESTIMATOR_OR_INFERENCE`，它们不是 economic null。

Economic：`ECONOMIC_CRITERION`。只有相关正式决策要求的所有 upstream layers 都满足，才允许 economic stop。

## EMP-FAIL02 — Mandatory diagnosis / evidence proportional to failure layer
对 anomalous、sparse、unstable 或 adverse pilot result，按顺序建立 `PILOT_FAILURE_DIAGNOSIS`：复现 failure → 定位 layer → cause tree → decisive diagnostic → legal repair paths → Seen Data/Claim Drift audit → verdict。

证据必须匹配 failure layer：ACCESS 用 entitlement/subscription/vendor/user-verified access；IMPLEMENTATION/DATA_IDENTITY/DATA_QUALITY 用 code/log/schema/hash/vendor docs；MEASUREMENT/CONSTRUCT 用 canonical construct literature + high-quality applications + vendor semantics，并按 `CORE-M01`；IDENTIFICATION/ESTIMATOR_OR_INFERENCE/SAMPLE_SUPPORT_OR_PRECISION 用 econometric/method sources 与 design-specific application；ECONOMIC_CRITERION 先看 execution class。

对 `OUTCOME_DECISION_SCREEN` 只检查 frozen progression/resource criterion；screen stop 是资源分配决策，不是 economic-null。对 `FORMAL_STUDY`，先检查 Freeze-B economic threshold/decision rule，只有 threshold method 本身有争议时再补方法文献。

不要把 parser/schema bug 升级成文献综述；若技术 repair 暴露新的 construct problem，再升级到 construct layer。

## EMP-REPAIR01 — Repair legality
允许 independently demonstrated implementation bug、unit/schema/timestamp/linkage error 与其他 prespecified construct-preserving repairs。

Core sample frame、outcome、treatment、estimand、measurement construct 或 identification 改变时，必须新 freeze/branch。不能因 sign/significance 不方便而改 window、threshold、transformation、sample 或 outcome。

## EMP-ID01 — Pre-Pilot Identification Minimum
Freeze A 前，design 必须具体到足以解释 pilot：
`estimand / treatment / control / counterfactual / timing / sampling frame / interference / main identifying assumptions / strongest rival / discriminating evidence / expected failure modes / inference unit`。

不能等 pilot 结果可见后才决定 core identification 或 cluster dimension。

## EMP-ID02 — Formal Identification Strengthening
Pilot 后，只能在相同 core estimand/identification logic 内加强 design，例如 fuller benchmarks、prespecified alternative counterfactuals、formal FE/inference、few-cluster/event procedures、placebos、falsification、robustness、sensitivity。

若 pilot 迫使采用不同 core counterfactual 或 identification strategy，设置 `CLAIM_DRIFT=YES`，重新 freeze 或开新 branch。不能结果后搜索一个更有利的 identification strategy。

只有 formal strengthening 仍在同一 core identification logic 内时，才使用 `FORMAL_IDENTIFICATION_STATUS=PASS`；改变 core identification 必须 `RETURN_FOR_REFREEZE`。

## EMP-INFL01 — Regression Influence Audit
Influence analysis 依赖 regression residuals、leverage、weights 或 candidate outcome，因此属于 B3 后 effect-open 工作，不等于 B1 univariate tail diagnostics。

打开 effect 前，先规定是否使用 influence analysis、哪些 diagnostics、它是 primary/prespecified sensitivity/diagnostic，以及与 primary estimator 发生 disagreement 时如何裁决。

可能 diagnostics：`Cook's Distance / DFFITS / DFBETA / leverage / robust-regression weights / robust-regression sensitivity`。

边界：B1 tail cleaning 不能被说成已解决 regression influence；B3 后不能因 influential observation 伤害结果就删掉并把新回归称为原 confirmatory main；要追溯到真实 economic event/entity 或 data error；独立确认 data error 按 repair rules；genuine economic event 不因 influential 就机械删除；primary 与 prespecified robust/influence sensitivity 发生 material disagreement 时，在 formal economic verdict 前按 estimator/inference issue 裁决；robust regression 只有 effect inspection 前已冻结为 primary estimator，才能承担 primary confirmatory role。

## H. Pilot/screen state 与 freezes

## EMP-PILOT01 — Pilot state / verdict
仅使用：

```text
SCREEN_STATUS =
NOT_STARTED / IN_PROGRESS / BLOCKED / REPAIRING / COMPLETE
```

以及：

```text
SCREEN_VERDICT =
CONTINUE / CONTINUE_WITH_REVISION / STOP_RESOURCE_ALLOCATION / NOT_ADJUDICATED
```

若 technical、measurement 或 precision blocker 未解决且不存在合法 final adverse decision，使用 `NOT_ADJUDICATED`。

## EMP-PROBE01 — Candidate observation ≠ candidate outcome
完整 execution-class 定义在 `EMP-GATE00`。这里只固定：

```text
PREOUTCOME_MEASUREMENT_VALIDATION may use candidate observations.
PREOUTCOME_MEASUREMENT_VALIDATION may not open the candidate research outcome/effect.
```

真实 candidate observations 可能是验证 coverage、matching、classifier yield、gold-label quality 或 construct non-degeneracy 所必需；validation metric 必须与 research outcome 分开，workflow 保持在 B0–B2，不产生 screen verdict。

Technical probe 只是验证技术行为，因此应优先 synthetic/dummy/noncandidate data。

## EMP-FREEZE-A — Outcome-Screen Decision Freeze
Freeze A 只适用于 `OUTCOME_DECISION_SCREEN`。设置 `FREEZE_LAYER=FREEZE_A_SCREEN_DECISION` 与 `FREEZE_STATUS=IN_PROGRESS`，直到所有适用项被冻结。

B3 前按需冻结：screen objective（明确为 resource allocation 而非 confirmatory proof）、input identity、sample rule、treatment/control、outcome/construct、aggregation、cleaning/transformation/scale、estimand、minimal estimator、prespecified progression/resource criterion 及运行该 criterion 必要的 screen-specific statistical rule（不得升级成 formal economic-null/equivalence inference）、substantively triggered 时的 multiplicity plan、与 screen objective 匹配的 sample/precision rationale、progression criteria、allowed repair classes、blindness boundary、stop conditions。

目的：防止 screen 结果反过来选择 screen rules。

## EMP-FREEZE-A2 — S13 entry and completion
进入要求相关 upstream data-identity、measurement、system-identity gates 已按 canonical state 完成。

完成要求：screen applicability 已判适用/不适用；适用时 screen-data reuse policy 已 freeze；within-study multiplicity 已 pass/not applicable；blindness 仍在 B0–B2；适用 screen 的 objective、sample rule、progression criteria、allowed repairs 与 stop conditions 已 freeze。

Economic-threshold status 不自动属于 screen freeze；formal economic thresholds 属于 formal study，除非 screen 的 prespecified decision rule 明确且合法需要。

启动适用 screen 需要用户明确授权打开 effect。Method discussion、question 或 audit request 都不是 screen-start authorization。

## EMP-FREEZE-B — Formal Main Specification Freeze
设置 `FREEZE_LAYER=FREEZE_B_FORMAL_MAIN_SPEC` 与 `FREEZE_STATUS=IN_PROGRESS`，直到 formal main specification 完成。

Freeze B 只有在 surviving pilot/screen、post-pilot literature freshness/collision recheck 与 formal identification strengthening 后形成。

它可以在 prespecified rules 下实施更大 formal sample、更完整 inference、prespecified benchmarks/robustness、construct-preserving measurement improvements 与已冻结 multiplicity architecture。

不能为了救 sign/significance，使用 pilot result 改 core estimand、primary outcome、treatment、direction、sample frame 或 cleaning rule。若必须改变，设置 `CLAIM_DRIFT=YES`，重新 freeze 或开新 branch，并把旧 pilot result 写入 Seen Data history。

## EMP-SCREEN01 — Outcome screen is optional
Pilot/feasibility guidance 区分 feasibility objective 与 formal effectiveness testing。ScholarOps 将该原则适配到 finance/business：不是每个 surviving project 都必须通过 outcome decision screen。

记录：

```text
OUTCOME_SCREEN_APPLICABILITY =
APPLICABLE
NOT_APPLICABLE
BLOCKED
```

例如 holdout 会严重损伤小 formal sample、主要风险已在 pre-outcome measurement/feasibility 解决，或提前看 effect 的 inferential cost 大于资源决策价值时，`NOT_APPLICABLE` 合法。此时不打开 effect，按 state model 把 screen status/verdict/reuse policy 记为 not applicable。

## EMP-SCREEN02 — Screen verdict semantics
适用 screen 仅允许：

```text
CONTINUE
CONTINUE_WITH_REVISION
STOP_RESOURCE_ALLOCATION
NOT_ADJUDICATED
```

`STOP_RESOURCE_ALLOCATION` 仅表示：按 prespecified screen rule，当前项目不值得继续投入额外研究资源。

绝不能改写成“经济效应为零”“统计等价”“低于所有有意义 effect”。正式 economic null/equivalence/minimum-effect claim 属于 formal study 与对应 threshold gate。
停止的 screen 进入 terminated-branch archive，而不是消失。

## EMP-REUSE01 — 打开 effect 前冻结 `SCREEN_DATA_REUSE_POLICY`
Observation 已用于查看 effect，且该信息影响 branch 是否存活后，再把同一 observations 当成未受影响 confirmatory evidence 可能使 ordinary inference 无效。

Internal-pilot research 提供狭窄例外。Wittes & Brittain (1990) 区分 variance/control-process 等 nuisance/design parameters 与 treatment-effect parameters，并警告不要根据 treatment-effect information 适配 design。Wittes et al. (1999) 进一步表明，unblinded interim variance-based sample-size recalculation 仍可能影响 type-I error，程度取决于具体 design。

B3 前必须冻结一种：

```text
SCREEN_DATA_REUSE_POLICY =
EXTERNAL_HOLDOUT
BLINDED_INTERNAL_NUISANCE_ONLY
VALID_ADAPTIVE_SEQUENTIAL_REUSE
EXPLORATORY_REUSE_ONLY
```

`EXTERNAL_HOLDOUT`：screen 看过的 observations/events 不进入 clean confirmatory estimation；没有合法 reuse design 时默认用它。

`BLINDED_INTERNAL_NUISANCE_ONLY`：interim data 只用于不泄露 branch decision 所需 treatment-effect direction/magnitude 的 nuisance/design quantities，例如 variance、coverage、missingness、measurement precision、recruitment 或 implementation feasibility。这里 “blinded” 指对被适配 decision 的 effect-blind；某些 internal-pilot procedure 可能用 treatment labels 形成 pooled nuisance estimate，不代表 universal label-blinding。

`VALID_ADAPTIVE_SEQUENTIAL_REUSE`：interim effect 已打开且同一 observations 要留在 formal inference 时，必须在 effect open 前冻结具体 valid adaptive/sequential procedure 及其 conditions。“以后再 adjustment”不是方法。

`EXPLORATORY_REUSE_ONLY`：effect 已用于 branch selection，又没有合法 adaptive/sequential correction 时，reused result 只能 exploratory/conditional，不能叫 clean confirmatory test。

四分类是 ScholarOps governance；临床试验来源只支持更窄的 nuisance-vs-effect 区分及部分 internal-pilot reuse 的 inference consequence，不证明这四个 label 是 universal statistical categories。

## EMP-REUSE02 — Inference after data reuse
最终解释受 effect open 前冻结的 reuse policy 约束：

| Policy | Formal interpretation |
|---|---|
| `EXTERNAL_HOLDOUT` | 对 untouched holdout 做 ordinary confirmatory interpretation，仍受 frozen design 约束 |
| `BLINDED_INTERNAL_NUISANCE_ONLY` | 只有 documented internal-pilot/nuisance procedure 及其 assumptions 支持时才 confirmatory |
| `VALID_ADAPTIVE_SEQUENTIAL_REUSE` | 使用 frozen valid adaptive/sequential procedure 的 inference/critical values，而不是普通 final p-values |
| `EXPLORATORY_REUSE_ONLY` | exploratory/conditional，不得称 clean confirmatory evidence |

Wittes et al. (1999) 研究特定 two-group normal internal-pilot design。Interim variance-based sample-size recalculation 下，final pooled variance 会向下偏，使 naive final t-test 可能提高 type-I error；失真依设计而异。其 restricted design 中，在研究过的参数范围内，当 internal-pilot sample 大约超过每组 30 时，type-I error 未超过约 0.052；unrestricted design 在很小 pilot、很早 recalculation 时可出现更大 inflation。论文还给出 design-specific 建议：internal pilot 从一开始规划、实际 pilot fraction 约 1/4–3/4；在其 restricted normal setting 中，约 1.99 而非 1.96 的 critical value 可在较宽参数范围保护 5% type-I error。

这些数字**不是 ScholarOps 通用常数**，只有当前 design 与该 normal internal-pilot setting 足够接近时才可迁移。Effect-based branch selection 是另一个问题，不能移植这些数值修正。

实际 reuse 与 frozen policy 不一致时，设置 `CLAIM_DRIFT=YES`，走 governance return path，不得静默改 policy。

## I. Formal estimation 与 result QA

## EMP-FORMAL01 — Formal Main Estimation 执行 Freeze B，不重新设计
只有 `EMPIRICAL_EXECUTION_CLASS=FORMAL_STUDY` 且 Freeze B 完成后才进入 formal main estimation。执行已经冻结的 primary sample、treatment/exposure、primary outcome、cleaning/transformation、estimator、FE/control structure、inference/cluster procedure、触发时 multiplicity architecture 与 economic-scale interpretation。

Formal-result execution 不是新的 design-selection phase。

## EMP-FORMAL02 — Formal Result QA
Formal result 出来后，在解释经济含义前，至少记录或核验以下字段：

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

同时检查执行是否与 Freeze B 一致、sample 与 exclusions 是否符合规则、model/inference 是否实际运行、必要 diagnostics 是否完成、result table/figure 与 source output 是否一致、缺失/失败/警告是否被隐藏，以及任何 post-freeze change 是否触发 revalidation / Claim Drift。

QA 不能通过“结果看起来合理”替代可追踪证据。只有 main result 完整、且没有 unresolved implementation、data、measurement 或 inference blocker 时，才能进入 mechanism/robustness。对影响 verdict 的明确 implementation/data bug 可修复后按 frozen main 重跑；需要改变 construct 或 identification 时进入 Claim Drift；结果不显著或不方便本身不是重新设计 main specification 的许可。

## EMP-FORMAL03 — Mechanism / robustness 按 trigger 激活，不自动堆积
Formal main result 后，不自动开启所有 mechanism、heterogeneity、placebo 与 robustness。只有它们能够检验 prespecified rival、identification assumption、measurement concern、inference fragility 或边界条件时才激活。

结果后新提出、且并非预先规定的机制或 subgroup 必须 `EXPLORATORY`，不能用多轮追加检验把研究救到显著。

## J. Multiplicity 与 specification governance

## EMP-MULT00 — 三层 multiplicity 不同
不要把三类不同的问题合并成同一种 adjustment：

```text
A. WITHIN_STUDY_MULTIPLICITY
   同一研究中的多个 outcomes、treatments、subgroups、windows、horizons 等

B. SPECIFICATION_SEARCH_DATA_SNOOPING
   在同一数据上反复选择 window、model、rule 或 sample

C. LITERATURE_SELECTION_FACTOR_ZOO
   从被高度搜索的文献空间中选择研究假设
```

其中 `WITHIN_STUDY_MULTIPLICITY` 由 `EMP-MULT01–06` 处理，`SPECIFICATION_SEARCH_DATA_SNOOPING` 由 `EMP-SPECSEARCH01` 处理，`LITERATURE_SELECTION_FACTOR_ZOO` 由 `CORE-L4-09` 处理。within-study 的 FWER/FDR 不能修复 literature-level factor-zoo selection；specification-search correction 也不是 outcome multiplicity 的同义词。三类状态必须分别跟踪。

## EMP-MULT01 — 先定义 scientific claim unit，再定义 testing family
Multiplicity 可以来自多个 outcomes、treatments、subgroups、event windows、horizons、model/specification variants 或 mechanism tests。外部来源直接识别 outcomes、subgroups 与 treatments 等 multiplicity 来源；ScholarOps 将同一决策逻辑扩展到 windows、horizons 与 mechanism tests，而 specification search 另行治理，不能谎称这些扩展都由同一来源逐项提出。

在 Freeze A 之前，每个 confirmatory hypothesis 至少记录：

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

testing family 应由“哪些 rejections 共同支持同一个 confirmatory scientific claim”定义，而不是由 tests 是否出现在同一张表定义。不能在看到结果后，把不利 test 拆成新的 family 来逃避 multiplicity。若当前设计的 treatment assignment、subgroup structure、family size 或 dependence structure 与方法来源明显不同，先按 `CORE-M01` 核方法适用性。

## EMP-MULT02 — Claim logic
结果打开前，对每个 testing family 冻结一种 claim logic：

```text
ANY_OF_MANY
ALL_CO_PRIMARY_REQUIRED
ORDERED_HIERARCHY
OMNIBUS_OR_INDEX_FIRST
DISCOVERY_FAMILY
SEPARATE_SCIENTIFIC_CLAIMS
```

不同 claim logic 对应不同 error-control 与 power/precision 含义。单独 p-values 的显著性不能替代 family-level claim 的实际逻辑；也不能先看结果，再选择最容易保留结论的 claim logic。若成功要求所有 co-primary endpoints 都通过，其 type-I-error 与 power 结构不同于 any-of-many family，不能机械移植其他领域的数值例子。

## EMP-MULT03 — Error criterion / method selection
对于以“任一 rejection”支撑结论的 confirmatory family，默认记录：

```text
MULTIPLICITY_ERROR_CRITERION=FWER
```

除非事先明确选择并有方法依据支持其他 confirmatory error criterion。`Holm` 可作为透明的 strong-FWER baseline；更有力的 resampling step-down 方法只有在 dependence/resampling structure 与 independent variation units 足够支持时才能使用。若只有已发表的 unadjusted p-values 而没有 individual-level data，Bonferroni/Holm 等简单方法可能是少数直接可执行选择。

对于 large exploratory/discovery family，FDR control 可能更合适；但 FDR 与 FWER 回答不同的 error question，FDR-controlled discovery family 仍属于 `EXPLORATORY/DISCOVERY`，不能自动变成原来的 confirmatory claim。根据 scientific claim、dependence、sampling/cluster structure 选择方法，不能为了得到更多 significance 事后挑 correction。若 assumptions 不合适，按 `CORE-M01/M02` 查方法 precedent 并记录 fit/mismatch。

## EMP-MULT04 — Primary / secondary / exploratory hierarchy
在 Freeze A 之前，把 hypotheses 明确分类为：

```text
PRIMARY
CO_PRIMARY
SECONDARY_CONFIRMATORY
EXPLORATORY
```

Primary/CO_PRIMARY family 承担主 claim 的正式 inference；`SECONDARY_CONFIRMATORY` 按预设 hierarchy 与 familywise logic 处理；结果后新增 analysis 只能 `EXPLORATORY`。ScholarOps 借用 formal multiple-endpoint guidance 的可迁移原则——先确定哪些 endpoints/claims 承担结论，再讨论 multiplicity——但不把 clinical regulatory rules 整套搬入 finance/business research。

不能把 secondary/exploratory 中最有利的 result 事后提升为“真正 primary finding”而不建立新的 branch/freeze。

## EMP-MULT05 — Reporting
报告 raw 与 adjusted evidence 时，清楚说明 family definition、adjustment criterion、method、number of tests、dependence assumptions、primary claim 与哪些结果未通过 adjustment。

不要只报告“调整后仍显著”的幸存结果而隐藏完整 testing family。

## EMP-MULT06 — Gate status / automatic short-circuit
先计数：

```text
N_CONFIRMATORY_TESTS_PER_SCIENTIFIC_CLAIM
```

若某个 confirmatory scientific claim 只有一个 substantive test，且没有多个 primary outcomes/treatments/subgroups/windows/specification choices 共同支撑该 claim，则设置：

```text
WITHIN_STUDY_MULTIPLICITY_STATUS=NOT_APPLICABLE
MULTIPLICITY_LEDGER_REQUIRED=NO
```

不要为了形式而创建 family ledger 或机械应用 Holm/FDR。若真实 multiplicity 存在，必须建立 ledger，并在 effect open 前冻结 family、claim logic 与 adjustment plan；若 family 未冻结、claim logic 未定义，或 adjustment 与 sampling/cluster structure 不兼容，则设置 `WITHIN_STUDY_MULTIPLICITY_STATUS=BLOCKED`，相关 freeze 不得完成。结果后再定义 family 属于 post-hoc selection。

## EMP-SPECSEARCH01 — Specification search on one dataset
同一 dataset 被反复用于 model/specification search 时，必须在结果前定义：

```text
SPECIFICATION_SEARCH_STATUS
BENCHMARK
PERFORMANCE_MEASURE
PREDICTION_SAMPLE
SEARCHED_SPECIFICATION_SET
```

White (2000) 研究的是一个可枚举 search universe 中“最优模型是否真的优于命名 benchmark”的 data-snooping 问题。Reality Check 评估表面 best relative performance 是否可能由搜索产生，并不证明 winning model 结构上为真。论文示例说明忽略 search 会显著低估不确定性：directional accuracy 的 naive p≈0.0036，而 Bootstrap Reality Check p≈0.2040；prediction MSE 对应约 0.1068 与 0.3674。

允许的 ScholarOps response 包括：formal estimation 前冻结完整 confirmatory specification 并把后续 variants 标 exploratory；采用 assumptions 与 sampling/dependence structure 匹配的经过验证 data-snooping/multiplicity procedure；科学与统计上合理时，用 untouched holdout 分离 search 与 formal inference。

如果 extensive search 已发生且没有 defensible correction、holdout 或 refreeze path，clean confirmatory inference 的 `SPECIFICATION_SEARCH_STATUS=BLOCKED`。

来源边界：White 的 procedure 只校正能够 enumerable/replay 的 model set；不可观察的既往 search 不会自动被纳入；核心 asymptotics 针对有 stated mixing/dependence 条件的 time-series setting，其他结构需另证；estimated-parameter directional-accuracy 不属于最简单 smooth corollary；Reality Check 可能 conservative，不是通用 robustness certificate；论文直接讨论 holdout/test data，但 full cross-validation extension 仅被视作潜在未来研究，而非已证明一般结果。

White 示例的 500 bootstrap resamples 与特定 stationary-bootstrap smoothing parameter 是示例，不是 ScholarOps universal default。

## K. Economic thresholds 与 effect interpretation

## EMP-THRESH00 — Execution-class activation
`TECHNICAL_PROBE` 与 `PREOUTCOME_MEASUREMENT_VALIDATION` 使用 `ECONOMIC_THRESHOLD_STATUS=NOT_APPLICABLE`；measurement precision target 不是 economic SESOI。

`OUTCOME_DECISION_SCREEN` 不因打开 effect 就自动激活 formal economic-threshold gate，因为 screen 不做 formal economic-null claim；其 go/no-go 依据 prespecified progression criterion。

`FORMAL_STUDY` 在 formal estimand/claim 真正需要时解释 economic magnitude。若 scientific claim 不依赖 minimum-meaningful-effect 判断，可在记录方法理由后保持 threshold gate not applicable。

## EMP-THRESH01 — 三类 threshold 分开
不得混淆：
1. `ECONOMIC_MINIMUM` 或 SESOI——最小经济/理论上有意义 effect；
2. `STATISTICAL_EVIDENCE_RULE`——CI、alpha、equivalence、minimum-effect 等 inference rule；
3. `MDE_OR_PRECISION_TARGET`——在给定 operating characteristics 下 design 能 detect/exclude 的最小 effect。

三者不能互相替代。

## EMP-THRESH02 — Economic minimum 的证据顺序
尽量用原始 economic units 定义 minimum，而不是从任意 standardized effect（如 0.1 SD）开始。

优先证据：
1. 与 actor、decision、institution、payoff 或 cost 直接相连的 substantive threshold；
2. theory/mechanism-based minimum；
3. high-quality close precedent 中的 economic magnitude；
4. defensible domain-expert/regulator/professional convention；
5. treatment-blind clean-sample distributional scales 仅用于把 raw-unit effect 翻译为 SD/IQR/percentile，不用于创造 substantive importance。

Raw-unit effect 难解释时可报告 1-SD change、IQR/percentile contrast、robust dispersion contrast，或 asset-pricing 场景中有意义的 high-minus-low portfolio characteristic contrast。

Bali, Engle, and Murray (2016, §6.2) 支持用 cross-sectional SD、IQR/95–5、high-minus-low characteristic spread 翻译 Fama-MacBeth coefficients 的经济量级；它支持多种可解释**尺度**，不定义 universal smallest economically important effect。

因此：`scale translation != economic-minimum definition`。
上述 evidence hierarchy 是 ScholarOps governance；Bali et al. 只支持 translation step，不支持 1–4 的 substantive ordering。

## EMP-THRESH03 — Formal economic-null 不能来自 nonsignificance
本规则属于 `FORMAL_STUDY` economic-magnitude adjudication，不属于 `OUTCOME_DECISION_SCREEN`。Nonsignificant 不证明 meaningful effect 不存在。正式 absence/irrelevance claim 要有 prespecified equivalence/minimum-effect framework、defensible bounds 与足够 precision。

联合考虑 significance 与 equivalence/minimum-effect 时，结果可以是 substantively nonzero、substantively small、statistically inconclusive、或 compatible with a null-like range。“Undetermined”是合法科学结论，不能改写成“no effect”。

Equivalence bounds 必须随 claim 报告，可来自 theory、practice、decision costs，或明确论证后来自 design 在 feasible sample 下能有意义排除的最小 effect。Resource-derived bound 是 project-specific，不证明 universal irrelevance。

结论只适用于实际 study 的 operationalization/design。Measurement change、confounding 或不同 intervention 可能改变结果；证明缺乏 meaningful effect 的证据负担与单纯“未检测到”不同，独立 replication 仍重要。

## EMP-THRESH04 — No arbitrary convention
不能仅因某数字常被叫作 “small”、0.1 SD 常见，或 estimate 看起来小，就冻结 economic minimum。

如果相关 formal freeze 前无法建立 defensible `ECONOMIC_MINIMUM`，对 economic-magnitude adjudication 设置 `ECONOMIC_THRESHOLD_STATUS=BLOCKED`。研究仍可报告 estimate/uncertainty，但 claim ceiling 更低。

## EMP-THRESH05 — Threshold Source Registry
每个 candidate economic minimum 记录：

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

至少区分：

```text
DIRECT_DECISION_OR_COST_ANCHOR
THEORY_BASED
HIGH_QUALITY_CLOSE_LITERATURE
DOMAIN_OR_REGULATORY_CONSENSUS
EMPIRICAL_EXPECTED_EFFECT
STANDARDIZED_CONVENTION
```

Treatment-blind SD/IQR/MAD 可以翻译单位，不能单独定义什么“经济上有意义”。

## EMP-THRESH06 — Threshold commensurability
比较不同来源 threshold 前，检查是否对应相同：
`construct / actor / population / horizon / raw unit / decision consequence`。

否则标 `NOT_COMMENSURABLE`，不得平均或投票。如果能合理转换到共同经济单位，保留 original values 与 translation rule。

## EMP-THRESH07 — Formal economic-threshold conflict resolution
本规则只在 `FORMAL_STUDY` 使用 economic thresholds 时适用，不把 `OUTCOME_DECISION_SCREEN` 变成 economic-null test。

多个 high-quality、construct-aligned threshold sources 冲突时记录：

```text
THRESHOLD_CONFLICT_STATUS =
NONE
RESOLVED_PRE_B3
THRESHOLD_SET_FROZEN
UNRESOLVED
NOT_APPLICABLE
```

若某 threshold 直接映射当前 actor/decision/cost-benefit，而其他只是 generic convention，可在 B3 前把前者 freeze 为 primary，其余保留 sensitivity；选择依据 substantive relevance，不是哪个 threshold 给出更喜欢的 verdict。

若无原则可排序，freeze admissible threshold set，而不是强迫单值。报告 decision 是否对集合 robust；不同 admissible thresholds 给出不同 decision 时，标记 threshold-sensitive，走 prespecified revision path，不能选有利 threshold。

无法构造 defensible admissible set 时，可以报告 effect/precision evidence，但不能基于该 threshold gate 给 formal economic-null/stop decision。

## EMP-THRESH08 — Required artifact
Economic-threshold gate 激活时，在 effect inspection 前创建 `ECONOMIC_THRESHOLD_LEDGER_<ID>.csv`，包含 candidate thresholds、commensurability assessment、primary-or-set decision、rejected thresholds 与理由、effect-open status。
