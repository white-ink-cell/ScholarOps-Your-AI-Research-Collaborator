# 01 — 核心研究工作流（简体中文正式译本）

> 英文 `01_CORE_RESEARCH_WORKFLOW_EN.md` 是唯一 canonical semantic source。本文件用于中文阅读；Rule ID、状态值、字段、controlled vocabulary 与代码保持英文规范形式。

## A. 研究问题治理

## CORE-Q01 — 先有重要问题，再谈方法
首先明确：
`actor / action-or-decision / friction / counterfactual / consequence / why-it-matters`。
不要因为出现了新算法、新字段或容易获取的数据，就反向拼凑出一个本身不重要的研究问题。

## CORE-Q02 — 构念同一性
数据中观测到的 A/B 必须真正对应理论所声称的 A/B。
任何 proxy、数据源替换或粒度变化，都要比较：
`actor / unit / timing / information set / construct / claim ceiling`。
如果 construct identity 不成立，在估计任何结果之前先降低或重新冻结 claim。

## CORE-Q03 — So-What
候选问题必须说明，结果至少可能改变下列一项：
`understanding / identification credibility / measurement / theoretical interpretation / boundary conditions / decisions / institutions`。
“有数据 + 有 gap”本身不够。

## CORE-Q04 — Important Problem × Credible Attack
如果问题重要，但当前在数据、识别或测量上没有可信的攻击路径，把它放入 future-data 或 long-horizon queue，而不是把问题本身判成坏问题。
如果问题很容易执行但没有重要性，则因 So-What 不足而停止。

当问题、actor、construct 与 consequence 已足够明确，可以进行 literature landscape scan 时，设置 `QUESTION_FORMATION_STATUS=PASS`；否则使用 `REVISE` 或 `BLOCKED`。

## B. 发现与文献

## CORE-LIT01 — 多元发现路径
候选可以来自：
`canonical problem / real-world phenomenon / institutional or regime change / assumption challenge / literature conflict / replication concern / researcher curiosity`。
这些路径只记录 idea provenance，不自动证明 novelty。

## CORE-LIT02 — Blind-first 是偏差诊断工具，不是否决权
可使用 blind-first search 降低历史 seed paper 的锚定。blind pool 冻结后，研究者自己的想法可以作为 challenger 进入相同 gate。
研究兴趣可以产生问题，但不能证明 novelty 或 priority。

## CORE-LIT03 — Landscape ≠ Focused Census
Landscape scan 只用于广度发现和初步撞题检查。进入 Pre-L4 前必须完成 Focused Census。

完成的 Focused Census 至少包括：
- search log；
- coverage map；
- bibliography；
- source map；
- unresolved-blocker ledger。

不能仅因 Landscape “看起来不拥挤”就进入 L4。

## CORE-LIT04 — Focused Census 停止规则
Census 开始前记录：
`required source families / query families / year window / citation-chase targets / source-quality order / decision-stability criterion / unresolved-blocker policy`。

是否完成由 decision stability 决定，而不是固定搜索轮数：
1. 预先规定的 Core、Adjacent 与高权威 Frontier source families 已覆盖；
2. 预先规定的 query families 和 dangerous-neighbor citation chains 已完成；
3. closest-neighbor set 与 contribution delta 已达到 decision-stable，即继续加入非决定性来源不再改变当前 continuation、narrowing 或 pre-L4 decision；
4. 最后再运行一次 sentinel search，至少使用一个新的 synonym、citation route 或 freshness/date route；
5. 如果 sentinel 找到可能改变决策的来源，继续 targeted verification；
6. 如果只返回重复、低相关或无法改变决策的材料，Census 可以停止；
7. 如果工具无法观察完整 forward citations，记录 `NOT_OBSERVABLE`；不得声称搜索 exhaustive。

一个决定性的新论文可以提前终止搜索。不要为了满足形式上的轮数而继续无意义搜索。

## CORE-LIT05 — Evidence、Search Process 与 Provenance 分开
`EVIDENCE` 是真实论文/appendix、官方数据或机构文件、正式标准。

`SEARCH_PROCESS` 是 query、搜索日期、不可获取数量和排除记录。

`PROVENANCE` 是内部 registry、SQL、以前报告、summary 或 scoring table。

关于 novelty、collision、construct identity 或 data existence 的结论，不能只由 search-process metadata 或 provenance record 支撑。

## CORE-LIT06 — Source Quality / Frontier Authority
默认优先级：
1. peer-reviewed Core literature；
2. peer-reviewed Adjacent literature；
3. canonical high-quality sources；
4. high-authority frontier research；
5. low-authority frontier material 仅用于 exact-similarity checks 或 Core-gap sentinel。

arXiv、SSRN、ResearchGate 是传播渠道，不是质量认证。
在给出 stop 或 narrowing 判断时，低权威 unpublished work 不能被赋予与高质量 peer-reviewed evidence 相同的裁决权重。

## CORE-LIT07 — 必须读真实 predecessor method
不要根据标题或摘要迁移方法。
至少提取：
`sample construction / variable formula / cleaning / timing / estimator / inference / assumptions / failure modes / appendix implementation / version changes`。
之后才能判断哪些内容可迁移。

## CORE-LIT08 — 用户已提供的核心材料优先
如果用户已经提供 core papers、appendices、replication packages、methods books 或 official documents，先搜索并读取这些材料，再补充外部文献。
不要因为换了会话就凭记忆重新设计。

## CORE-LIT09 — Open-world Field Router
文献搜索不能写死成某一组期刊。
先识别候选真正的 academic home，再动态构建：
`Core / Adjacent / Frontier / methods / institutional sources`。
“没有搜到”不能当成“没人研究过”的证据。

## CORE-LIT10 — Standard / Regulator 的 claim ceiling
监管规则、会计准则和官方制度可以确立 institutional definitions 与 requirements。
但它们本身不能证明 literature absence、novelty 或 economic effect。

## CORE-LIT11 — Freshness Reopen
已完成的 Focused Census 不因开启新会话或新一轮工作就自动重跑。
只有在相关触发发生时才 reopen，例如：
`freshness window exceeded in a fast-moving field / new highly related paper / estimand or measurement changed`。
否则复用已冻结 evidence package。

## C. Discovery 纪律与范围

## CORE-DISC01 — Research horizon / boundedness
使用受控 horizon 对候选分类，例如：
`CURRENT_EXECUTABLE / BRIDGE_PROJECT / LONG_HORIZON_RESEARCH_AGENDA / HOLD_FUTURE_DATA`。
项目如需扩展 vocabulary，只能通过 schema；不得创造近义状态绕过 state model。

当前项目必须有可观测对象和有边界的 claim ceiling。如果研究价值完全依赖当前不可观测的未来均衡问题，应放入 long-horizon agenda。

## CORE-DISC02 — Discovery freeze / selection
当计划中的 Landscape coverage 完成后，默认冻结新 idea generation，并把选中的候选推进到 Focused Census。
只有在所有候选都被终止、新制度/数据冲击改变机会集，或发现明确系统性遗漏时，才 reopen Discovery。

Focused Census 通常应研究少量 construct-distinct、decision value 高的候选，而不是把不可比的分数强行做成 ranked Top-N。

## CORE-DISC03 — Discovery Iteration vs Confirmatory Lock
Pre-L4 Freeze 前，允许在以下环节受控迭代：
`problem ↔ question ↔ construct ↔ literature ↔ argument ↔ feasibility`，
但必须记录 version/change/reason。

Pre-L4 Freeze 后启用严格 gates。研究问题发生实质变化必须触发 Claim Drift 并重新 freeze；不能一边改问题，一边假装仍处于原来的 L4 review。

## D. Contribution / collision

## CORE-C01 — Collision 是诊断，不是自动死亡
基于 collision 的 stop 必须同时满足：
`DIRECT_REDUNDANCY + NO_SUBSTANTIVE_CONTRIBUTION_DELTA`。

相同大问题仍可能通过可信 identification advance、contradictory adjudication、mechanism deepening、boundary condition、institutional change 或 high-value replication 形成贡献，但候选必须说明新设计如何改变可被信任的 inference。

## CORE-C02 — Single Contribution-Delta Rule
每个存活候选最多保留一个 primary、两个 secondary contribution modes：

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

始终明确：
`old paper does X / candidate adds Y / why Y changes inference / evidence that X lacks Y / required data`。

## CORE-C03 — No Conjunction Novelty
没有任何一篇论文同时满足 A+B+C+D，并不能证明 novelty。
如果组合只是把 workflow 拼在一起、加更多 checks 或换更新模型，默认视为弱贡献。
只有当 synthesis 产生新的 interaction、complementarity、substitution、nonlinearity、equilibrium implication、decision rule 或 boundary condition 时，才可能具有实质贡献。

## CORE-C04 — Same question, different method
方法不同本身不是贡献。
在看结果前，明确：
`old limitation / new advantage / bias or identification problem resolved / change in estimand credibility / adjudicating pattern`。

## CORE-C05 — Contradiction / deepening
只有新设计能够可信地裁决此前分歧时，contradictory result 才强。
多篇论文可以研究同一个 mother question，但新候选必须增加有意义的 mechanism、boundary、actor、institution、equilibrium、welfare/decision consequence 或 measurement identity。

## CORE-C06 — Inference-Value Test
即使方向结果与既有研究一致，只要研究改变以下内容，仍可能有贡献：
`causal credibility / construct validity / rival exclusion / boundary / mechanism / magnitude, welfare, or decision implication`。
如果增量只是更大样本、更新方法、更细粒度或更精确地再确认既有结论，默认视为弱贡献，并可能停止。

## E. Claim discipline 与研究表达

## CORE-CL01 — Claim ceiling
Predictive 不等于 causal。
Signal 不等于 adoption。
Proxy 不自动等于 construct。
Platform existence 不等于 user entitlement。
Claim 不得高于实际建立的最高证据层级。

## CORE-CL02 — Heterogeneity 本身不是 mechanism
优先使用短、直接、可观察的 mechanism chain。
只有 mechanism 事前明确，而且 heterogeneity pattern 能帮助排除强 rival explanation 时，heterogeneity 才能支持 mechanism。

## CORE-CL03 — 结果后形成的探索性内容
正式结果打开后才首次形成的 hypothesis、cutoff、subgroup 或 mechanism，必须标记为 `EXPLORATORY`。
不得事后改写成 confirmatory。

## CORE-CRAFT01 — Problematization
除了 gap search，还应检查候选是否挑战或澄清：
`unit / rationality assumption / information set / counterfactual / equilibrium / measurement / institutional invariance / external-validity boundary`。

## CORE-CRAFT02 — Argument architecture
Argument architecture 是 post-L4、pre-writing 的 craft tool，不是 Pre-L4 entry gate。
一种实用结构是：
`question or claim → mechanism or reason → expected evidence → warrant → strongest rival → discriminating evidence → qualification or claim ceiling`。

One-paragraph paper test 可以迫使研究者写清：
`question / unit-estimand / design / closest literature / contribution / why the reader should care`，从而暴露逻辑缺口。
如果在 Discovery 早期使用，它只能是 diagnostic；不能仅因写不出漂亮段落就阻止进入 L4。

## CORE-CRAFT03 — Theory/contribution map
维护一个轻量 map：
`WHAT / HOW / WHY / WHO-WHERE-WHEN`
以及
`ORIGINALITY / UTILITY`。
不要强迫每个项目都声称宏大新理论。

## CORE-CRAFT04 — Write-to-think / outline-first
Discovery 阶段可以用 exploratory memo 暴露逻辑缺口。
正式写作前冻结 `PAPER_ARGUMENT_OUTLINE` 与 `EXHIBIT_MAP`，使论文围绕 argument 组织，而不是按研究工作的时间顺序堆叠。

## F. Data/method-triggered candidate discipline

## CORE-D01 — 数据不能制造重要性
`DATA_FIRST` 或 `METHOD_FIRST` 候选必须先证明：
1. 问题与 bottleneck 在新数据/方法出现前已经存在；
2. 旧方法无法区分重要的竞争解释；
3. 新数据/方法改变 construct validity、identification 或 observability，而不仅是把研究做得更大、更细或更方便。

## CORE-D02 — Historical substitute
声称“首次可以研究”之前，搜索 historical substitutes，例如：
`administrative data / hand-collected samples / surveys / FOIA / commercial or proprietary data / author-constructed data / legacy filings / replication packages`。

## CORE-D03 — Decomposition 不是自动 novelty
把 Y 分成 Y1/Y2/Y3 不自动构成贡献。
只有当 decomposition 能区分理论、防止 sign cancellation、改变 counterfactual 或改变相关决策时才继续。

## CORE-D04 — Data/method-first 候选的低成本停止检查
在为 data-first / method-first idea 投入完整 Focused Census 前，先用少量关键论文、historical substitutes、old-vs-new inference table 与 contribution delta 做低成本 decision check。
如果候选无法说明问题早于新能力而存在，或新能力确实改变 inference，则应尽早停止，而不是花完整 L4 只为记录失败。

## G. Method precedent / ambiguity

## CORE-M01 — Professional Method Precedent / Concrete-Problem Grounding
任何具有实质方法后果的动作前，问两个问题。

### A. Skill procedure 是否真正被规定清楚？
至少应覆盖：
`input / unit / timing / construct / sequence / data conditions / decision criteria / estimator-or-operation / evidence basis / failure state / freeze point / next state`。
若缺失项可能实质改变结论，设置 `METHOD_GAP=YES`。

### B. 当前问题是否存在 Skill 未覆盖的特殊情形？
例如：
- unusual data-generating mechanisms；
- special missingness or selection；
- nested、clustered 或 network dependence；
- human-AI collaboration 或 agent workflows；
- vendor-specific field semantics；
- unusual market institutions 或 event timing；
- special labels 或 measurement error；
- nonstandard sampling、rollout 或 interference；
- 与标准教材假设不一致的数据分布或执行约束。

若存在，设置 `CONCRETE_PROBLEM_SPECIAL_CASE=YES`。
不要机械套教材默认做法，也不要根据“通常如此”来猜测数据语义、threshold、formula 或 missingness mechanism。

使用以下顺序：

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

如果只有用户能够解决一个 material unknown，而且不同答案意味着不同方法，按 `CORE-M03` 最小化提问，而不是猜测。
如果当前数据可以直接回答，按 Assistant-first execution 检查数据，而不是要求用户提供一个可以被验证的主观印象。

原则：按 concrete problem 的真实形态进行分析。方法来源提供候选方法和假设，不替代对当前数据、制度或 construct 的判断。不能先凭直觉设计，再找文献为决定背书。

## CORE-M02 — Method Decision Table
每个真正重要的方法选择至少记录：
`decision / exact current problem / special-case features / predecessor options / assumptions / evidence / current-data diagnostic / fit-or-mismatch / selected rule / rejected alternative / reason / claim consequence`。

如果 predecessor method 依赖当前 setting 不满足的 assumptions，记录 `NOT_TRANSFERABLE_AS_IS`。来源权威不代表可以机械照搬。

只有跨独立项目反复出现的 gap 才升级为 ScholarOps core rule。候选/项目专属处理放在项目 Method Freeze。

## CORE-M03 — User correction / new-idea ambiguity
当用户纠正、质疑或提出新想法时，如果不同解释会改变：
`question / actor / construct / estimand / treatment / data / method / claim / requested action`，不得猜测。
先重述已清楚部分，只问解决实质歧义所需的最少问题。不要因不重要的措辞差异反复盘问用户。

## CORE-M04 — Treatment ladder、mapping chain 与 inference unit
一句“X affects Y”经常把三个独立问题混在一起，而每一项都可能使结论失效。

### 1. Treatment ladder：capability ≠ eligibility ≠ adoption ≠ use
Treatment 可能经历：
`exists → available → eligible → adopted → actually used → use changes action`。
每一级都是不同 treatment，对应不同 estimand 与解释。Eligibility 可能识别 intent-to-treat effect，但不能证明 actual use 的效应。
Claim 必须停在已经被验证的最高一层。

### 2. Mapping chain：assignment 与 measurement 间每一环都需验证
当 treatment 分配给 A、outcome 却在 B 上测量时，每个 link 都是可证伪 mapping：

```text
assignment unit → intermediate ownership/relationship → measurement unit
```

任何一环未解决，claim ceiling 就停在最后已验证 link。“A 通常就是 B”或“没发现反例”不等于 validation。

### 3. Inference unit：数据行数不等于独立信息量
存在 common shock 时，independent information unit 是 shock/source，而不是 exposed objects 的数量。同一个 shock 暴露很多对象，并不等同于很多独立 shocks。
因此 leave-one-out、placebo、randomization-style inference 在适用时应作用于 independent-information layer。更多 objects 可以提高 within-shock measurement precision，但不能替代更多 independent shocks。

### 4. Cross-level prohibition
Individual、institution、object、market 是不同层级。一层的证据不能自动授权另一层的 claim。Individual-level behavior 可以启发 mechanism hypothesis，但不能证明 aggregate welfare effect；aggregate improvement 也不表示每个 individual 都改善。
跨层级引用时，明确 citation 提供的是 mechanism hypothesis 还是 same-level evidence。
更具体的 dependence 与 clustering 选择仍由 `CORE-M01` 约束。

## H. Opportunity、readiness 与 ranking

## CORE-R01 — Candidate ranking 禁止伪精确
没有预先设定权重和解释时：
- 不平均不可比维度；
- 不输出 8.8 vs 8.4 之类 pseudo-precise score；
- Landscape search 阶段不宣布 global winner。

跨阶段比较的是 `NEXT_EVIDENCE_INVESTMENT_PRIORITY`，不是最终研究质量。
同阶段内只有在 evidence maturity 可比时才比较 research quality。

## CORE-OE01 — Research opportunity 与 execution readiness 分开
分别记录：

```text
RESEARCH_CENSUS_VERDICT
PRE_L4_EXECUTION_READINESS
EXECUTION_BLOCKER_CLASS
RECHECK_TRIGGER
```

受控 blocker values 包括：

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

`RECHECK_TRIGGER` 必须是可检验事件，而不是“以后再看”。
`READY` 对应 pass；`CONDITIONAL` 必须说明 `CONDITION_TYPE`；`TEMPORARILY_BLOCKED` 要有可信 unblock path；`STRUCTURALLY_BLOCKED` 表示当前没有可预见路径。

临时 access、ethics、recruitment 或 procurement 问题不能冒充学术 stop。反过来，construct identity、contribution 或 So-What 薄弱，也不能用“未来也许有更好数据”来逃避。

## I. L4 — Pre-screen collision adjudication 与 pre-formal freshness review

## CORE-L4-01 — Pre-L4 Freeze + Entry Integrity
进入 L4 前只有一个最小必需 freeze artifact：
`PRE_L4_CLAIM_FREEZE_<ID>.md`。

只冻结 collision 与 claim-drift control 所需的研究身份：
`research question / mother problem / actor / friction / core construct / estimand / primary observable object or outcome / base scope / excluded extensions / claim ceiling / primary contribution delta / strongest rival`。

以下不是强制 Pre-L4 freeze fields：
`one-paragraph paper / full argument architecture / exhibit map / prose-level framing / detailed execution-readiness narrative`。
这些 craft elements 可以在 L4 后、正式写作前完成；不能只因缺这些内容就阻止 L4。

Freeze 开始时设置 `PRE_L4_CLAIM_FREEZE_STATUS=IN_PROGRESS`；只有 identity 与 evidence checks 通过后才设 `COMPLETE`；真实 claim freeze 或 upstream evidence 缺失时设 `BLOCKED`。
`L4_ENTRY_AUDIT` 检查 freeze 是否存在、identity 是否一致、Census evidence 是否可追溯；不能无必要扩张 freeze template。

L4 不是继续随意发明新问题的阶段。如果 deep read 迫使研究问题发生实质变化，标记 claim drift，回到相应上游阶段并重新 freeze。

## CORE-L4-02 — Dangerous-neighbor-first
L4 优先处理最可能直接撞题或最大幅度压缩 contribution 的 dangerous neighbors，而不是先读最容易获取或最支持候选的论文。

结合 version chain、same-author related work、appendix/replication、forward/backward citation chasing。
显式分类关系：
`direct redundancy / identification advance / construct correction / adjudication / mechanism / boundary / external validity / adjacent only`。

## CORE-L4-03 — Evidence blocker / queue
如果缺失全文或 appendix 可能改变决策，设置：
`L4_STATUS=BLOCKED` 与 `L4_VERDICT=L4_BLOCKED_EVIDENCE`，然后执行 targeted evidence unblocking。
若合理获取路径耗尽且短期无法解决，使用 `L4_STATUS=PARKED_BLOCKED`。Parked 既不是 pass，也不是 stop。
一个 blocked candidate 不必阻断其他候选的低成本 Focused Census，但在新的 candidate 占用 active L4 slot 前，必须先把它 unblock 或 parked。

## CORE-L4-04 — L4 status mapping
L4 status 与 verdict 必须来自 Controlled Vocabulary Registry。

关键 pre-screen / pre-formal routes：

```text
L4_PASS_TO_METHOD_DESIGN
→ Method / Design / Pre-Outcome Identification Minimum

L4_NARROW
→ return to PRE_L4_CLAIM_FREEZE
→ revise the frozen claim
→ re-enter L4
```

`L4_NARROW` 不是 pass。

在给出正式 `L4_NARROW` 或任何 `L4_BLOCKED_*` verdict 前，按 L4 evidence-sufficiency rule 记录 source tier。证据如果太弱或太间接，不能支持 narrowing/stop claim，就只能作为 verification lead，不能成为正式 narrowing verdict，也不能悄悄缩小 frozen contribution claim。证据充分的 direct collision 仍进入 adjudication。

不要输出 `COMPLETE + L4_BLOCKED_*` 等逻辑矛盾组合。

## CORE-L4-10 — 对不利文献判断实行证据对称性
用于 reject、block 或 narrow 某项研究 claim 的来源，必须足够强、足够直接，能够支撑所声称的不利命题。

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

规则不是“working paper 永远不算”。当 high-authority frontier paper 的相关 claim 与 evidence 真正可得且充分时，它可以建立 direct collision。真正的要求是：不能把弱或仅相邻材料升级成它无法支持的正式 claim-narrowing verdict。

必须遵守：
- 低于不利命题所需证据等级的材料，不能触发正式 `L4_NARROW`、`L4_BLOCKED_*` 或 claim shrinkage；
- 记录为 verification lead / unresolved evidence，并写明确 unblock condition；
- 对 direct 且充分支持的 collision evidence，仍要进行正式 contribution adjudication，不能因为结果不方便就忽略；
- `SEARCH_PROCESS_ONLY` 只能说明搜索做了什么/没发现什么，不能单独证明“world first”或“already done”；
- dangerous-neighbor-first 是优先级规则，不是有罪推定。

本规则明确 `CORE-L4-04` 与 `CORE-L4-10` 之间的 evidence-sufficiency 边界，同时保持 direct-collision adjudication 标准不变。

## CORE-L4-05 — L4 evidence package
完整 L4 review 通常保留：
`deep read / bibliography / collision matrix / version chain / citation chase / source map / entitlement audit / decision`。

`L4_SOURCE_MAP` 至少包括：
`candidate_id / claim_id / claim_text / source_id / source_role / source_version / evidence_locator / support_level / notes`。
使用显式 `NOT_APPLICABLE` 或 `NOT_AVAILABLE`；不要靠悄悄缺文件来表达状态。

## CORE-L4-06 — One-candidate L4 + last-mile
Census 后优先一次深审一个候选，以减少无效并行投入。
L4 开始时，用被冻结的 exact claim 做一次 last-mile direct-collision search。这不是重新进行 Landscape discovery。

## CORE-L4-07 — Incremental unblock
blocked full text 获得后，只更新受影响 evidence objects，例如 bibliography、version chain、collision matrix、deep read、decision 与 source map。
除非新证据改变 Core literature ecology，不要重跑完整 Census。

## CORE-L4-08 — Pre-Formal L4 Recheck：先做 Freshness Sentinel
该过渡检查设置 `L4_PHASE=PRE_FORMAL_RECHECK`。其目的是确认通过 screen 或其他允许的 pre-formal path 后，literature freshness 与实际实施的 measurement/estimand 没有产生新 collision；它不是默认重跑整个 L4。

进入条件包括存活的 screen verdict 或其他明确允许的 survivor state。输入包含 frozen pre-formal claim、prior search cutoff 与 dangerous neighbors、已实施 measurement/estimand identity，以及 Seen Data Register。

记录：

```text
PRE_FORMAL_L4_MODE =
SENTINEL_ONLY
FULL_UPDATE
RETURN_FOR_REFREEZE
```

当继续研究需要实质改变 actor、core construct、estimand、treatment、primary outcome 或 core identification 时，使用 `RETURN_FOR_REFREEZE`。标记 `CLAIM_DRIFT=YES`，通过 state machine 返回或创建新 branch。不要把新研究伪装成旧研究的 L4 update。

以下情形默认 `SENTINEL_ONLY`：prior L4 review 对该领域仍足够新；construct 与 estimand 未变；实际 measurement 仍在 frozen construct 范围内；不存在已知新的高度相关文献或制度/技术变化。Sentinel 至少检查 post-cutoff freshness、dangerous neighbor 的 version/same-author/forward-citation route（可观察时），以及使用真实 measurement/estimator 名称的 direct collision。

以下情形使用 `FULL_UPDATE`：prior review 对领域已经过时；measurement/estimator 实质改变；sentinel 找到可能改变决策的证据；dangerous neighbor 出现新版本/关键 appendix；或新的 institutional/data/technical development 改变学术邻域。

Post-result firewall：freshness query 不能因 effect sign、p-value 或有利 subgroup 而被选择。新文献可以改变 claim ceiling、确立 collision 或改变 benchmark priority；不能因为结果不理想就拿来改写原 confirmatory hypothesis。结果后新发明的 mechanism/analysis 属于 `EXPLORATORY` 或新 branch。

精确 calendar trigger 是项目/领域特定的 freshness parameter，不是通用真理。六个月只能在适合的快速领域作为默认 sentinel threshold；若缩短或延长，需要记录 field-specific justification。

## CORE-L4-09 — 对高度搜索研究空间设置 literature-selection hurdle
当 proposed hypothesis 来自已经被大量搜索的 research universe、Focused Census 显示同一 mother problem 下有很多并行 candidate signals，或贡献主要只是“又一个变量预测 X”时触发。

记录：

```text
LITERATURE_SELECTION_HURDLE_STATUS =
PASS / CONDITIONAL / BLOCKED / NOT_APPLICABLE
```

目的在于区分 candidate evidence 与“候选被选出来”本身的选择过程。Harvey, Liu, and Zhu (2016) 表明，在高度挖掘的 cross-sectional return-factor 文献中，传统 single-test significance threshold 可能过于宽松。发表版在不同 searched-universe 假设下得到 materially different benchmark t-statistics，因此不存在一个可以机械套用于所有金融研究的 ScholarOps 通用数字。

对论文 2012 calibrations，如果当前问题与相应 search universe 足够可比，可以记录以下 source-specific reference points：

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

`3.54` 是 homogeneous subset 的发表版 Bonferroni 值。

只有先把当前 claim 映射到相关 search universe 后，才可使用这些值。摘要层面的“t > 3.0”是总体警告，不是所有金融设计的统一 cutoff。

必须遵守三个边界：

1. **这是 selection-layer adjustment，不替代有效 inference。**Harvey, Liu, and Zhu 把文献报告的 t-statistics 作为输入；ScholarOps 仍必须按相关 empirical rules 验证当前研究的 standard errors、dependence、clustering、measurement 与 outliers。
2. **论文主要检验是 unconditional。**condition-specific claim 可能需要不同 mapping 与 claim ceiling。
3. **Dependence matters。**tests 正相关可能让某些 multiplicity adjustment 过度保守；candidate factor 数量增加并不机械等于最严的 independent-test threshold。

论文还区分 theory-motivated candidates 与 purely empirical searches。若据此放宽 hurdle，必须按 `CORE-M01` 记录 construct/theory mapping，不能当作免费豁免。

触发后至少选择一种可辩护 response 并记录进 L4 source map：literature-selection-aware evidence hurdle、真正 independent validation，或明确承认 selection from a searched universe 的较低 claim ceiling。

## J. Skill governance

## CORE-GOV01 — Skill anti-bloat
把每个新发现问题分类为：
`candidate-specific / family / agenda or profile / general rule / state-schema bug`。
只有 general/state-structural 或在独立项目中重复出现的问题才提升进 Core。Candidate-specific 处理应留在项目 Method Freeze。
