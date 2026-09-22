# Optional Profile — AI × Finance（简体中文正式译本）

> 英文 `PROFILE_EN.md` 是唯一 canonical semantic source。本 profile 只在任务明确涉及 AI × Finance 时加载，不代表整个金融研究的通用规则。

## AGENDA-01 — Profile scope，不是个人研究议程
本 profile 研究 AI、LLM、Agent、Skills 与自动化如何改变金融信息的 acquisition、processing、production、validation、use、intermediation 与 aggregation，以及在存在直接证据时，这些变化如何进入决策或市场。

不得把维护者个人学位、dissertation 或长期研究议程编码进 installed profile。

## AGENDA-02 — Signal → adoption → decision → market ladder
使用：

```text
AI_OUTPUT_OR_CAPABILITY
→ USER_ADOPTION
→ DECISION_RELIANCE
→ HOLDINGS_OR_TRADES
→ MARKET_OUTCOME
```

向更高层级推进需要该层级的直接证据或可信设计。相似 AI outputs 本身不能证明 crowded trading。Market-level rollout/outage 可以识别 market-level availability effect，即使没有 user logs；但此时 claim 不能进一步识别具体谁使用了 AI。

## AGENDA-03 — Market-impact claim 的进入要求
Market-impact 项目至少需要一个直接 bridge，例如：

```text
OBSERVED_AI_ADOPTION
EXOGENOUS_ROLLOUT_OR_OUTAGE
USER_LEVEL_AI_USE
HOLDINGS_OR_TRADES
PLATFORM_USAGE
ORGANIZATIONAL_ADOPTION_RECORD
```

没有这类 bridge 时，把项目停留在 capability、output 或 information-processing 层级。

## AGENDA-04 — AI-system identity 是动态的
以下构念不能自动视为等价：

```text
LIVE_CONSUMER_PRODUCT
LIVE_API
CONTROLLED_RAG
OPEN_WEIGHT_MODEL
LOCAL_AGENT
STATIC_REPLAY
```

相互替换时比较 actor exposure、system instructions、information set、retrieval universe、tools、personalization、必要时 account/region、latency、reproducibility 与 external-validity target。改变 construct 的 substitution 必须重新冻结研究设计。

## AGENDA-05 — 对 live AI system 做 snapshot
研究依赖 live AI system 时，记录决定 exposure 与 reproducibility 的重要元素，例如 provider、product、可见时的 model/version、access mode、system instructions、prompt、tools、retrieval mode、sampling parameters、必要时 account/region、run time、repetition plan、保留的 raw outputs/citations 与 vendor change information。

Provider 不公开内部 model/version 时记录 `NOT_EXPOSED_BY_PROVIDER`，不得猜测。

## AGENDA-06 — Historical leakage 与 memorization risk
当前模型用于历史任务时，记录 model release date、如公开则记录 training cutoff、可能的 pretraining exposure、web/retrieval exposure、point-in-time input controls、future leakage risk 与 model-version reproducibility。无法排除 memorization 时降低 claim ceiling。

## AGENDA-07 — Evaluation independence
如果主要质量判断由与被研究系统同一 provider 或 model family 的 LLM 产生，在可行时至少要求一个 independent anchor：

```text
OBJECTIVE_FINANCE_TARGET
HUMAN_EXPERT_LABEL
REPRODUCIBLE_RULE_BASED_METRIC
EXTERNAL_REALIZED_OUTCOME
```

## AGENDA-08 — AI capability 不等于 NLP
方法应对准真实 bottleneck：text、entity resolution、graph structure、multimodality、causal heterogeneity、simulation、scalable coding、high-frequency processing 或其他能力。AI 工具的新颖性本身不是 finance contribution。

## AGENDA-09 — Benchmark result 不自动等于 finance paper
Leaderboard、model ranking 或泛化的“某 agent/model architecture 更好”通常是 engineering result。只有它改变 economic inference、mechanism、boundary、institution 或 decision 时，才保留为 finance contribution。

## AGENDA-10 — 适用时使用 blind-first agenda discovery
使用 blind-first idea discovery 时：先从当前 problem domain 与 general access boundary 出发；在 blind problem/candidate pool 冻结前避免加载旧 candidate substance；之后再拿 historical projects 做 collision comparison；researcher-originated ideas 也按相同标准评估。

历史上下文无法避免时，记录 `BLIND_CONTEXT_CONTAMINATION=POSSIBLE`。不能仅因候选像旧 seed 就奖励或惩罚。

## AGENDA-11 — Agenda-stage outputs 与 transition
Agenda/landscape 阶段应产出 problem maps、literature ecology、bibliography/search log、candidate families、collision/source maps、lifecycle coverage，以及 shortlist 或 stage matrix。它本身不授权直接跳到 deep collision adjudication 或 empirical execution。

## AGENDA-12 — Candidate-family rule
共享 mother problem 的候选，应比较 actor、friction、AI change、observable object、outcome、closest literature、data 与 claim ceiling，再分类为 `MERGE_AS_ONE_FAMILY`、`PRIMARY_WITH_NESTED_VARIANT` 或 `DISTINCT_CANDIDATES`，之后再决定是否复制 downstream work。

## AGENDA-13 — Finance-specific increment
如果把 finance 换成 law、medicine 或 generic software use 后，proposed AI mechanism 的贡献几乎不变，就必须识别真正改变 inference 的 finance-specific institution、contract、payoff、price-formation process、capital-allocation problem、disclosure/regulatory structure 或其他 boundary。否则视为 general AI application，而不是 finance contribution。

## AGENDA-14 — 项目特定 AI claims 存在 project artifacts 中
Provider name、outage event、model list、event rule 与 project-specific implementation details 属于项目 freeze/registry，不属于 reusable profile。

## AGENDA-15 — Finance-program 与 field-home gates
对 AI × Finance candidate 进行 deep literature adjudication 前，使用下面三个 field-home rules。

## AI-FIN-FIELD01 — Finance legibility
进入 finance-priority queue 的候选应能用一句话回答：`What finance question changes if this result is correct?`

答案应连接到 finance object，例如 prices/returns、financing/investment、governance、information intermediation、banking/credit、risk/insurance、household finance、market design 或 liquidity。

## AI-FIN-FIELD02 — Academic home
Deep collision adjudication 前识别 `PRIMARY_ACADEMIC_HOME`，并列出来自该 home 的少量 canonical/nearest papers。HCI/CS mechanism 可以是 adjacent evidence，但不能替代 finance-specific increment。

## AI-FIN-FIELD03 — Domain familiarity
缺乏先验领域熟悉度不自动 stop。如果项目需要大量 institutional knowledge，建立最小 `DOMAIN_PRIMER`。如果学习负担超出当前可行预算，降低 executability，而不是假装 research opportunity 更弱。

## AGENDA-16 — General vs agenda-challenge coverage
Cross-domain challenge search 只有在项目明确进入 agenda-challenge mode 或当前 agenda lock 被 reopen 时才激活。在 active AI × Finance agenda 内，如果搜索被单一数据 modality 捕获，可使用 modality-exclusion challenger；但这一点本身不能证明应放弃 agenda。

## AGENDA-17 — Mechanism analogue
对 productivity、homogenization、common error、cognitive outsourcing、coordination 等 general AI mechanisms，相关时搜索 adjacent fields。存在 cross-domain analogue 不自动淘汰 finance project；候选必须说明哪一个 finance institution、equilibrium 或 boundary 改变了 inference。

## AGENDA-18 — Individual、collective 与 rationality claims
只有当项目声称 shared infrastructure、standardization 或 diversity 的效应时，才要求联合研究 individual quality 与 collective diversity/error correlation。区分 `HUMAN_RATIONALITY`、`HUMAN_AI_SYSTEM_PERFORMANCE`、`MARKET_EFFICIENCY`；没有证据不能跨层级移动。

## AGENDA-19 — Authentic finance outcomes
Investment intention、confidence 与 hypothetical portfolio weights 不自动等于 realized financial outcomes。当 claim 需要真实经济行为时，优先 incentive-compatible decisions、objective forecast/valuation targets、realized outcomes，或具有 external keys 的 professional tasks。否则降低 claim ceiling。

## AGENDA-20 — Blind-map-driven frontier search
Blind-first discovery 中，在 blind problem map 冻结前，不要用旧项目的 mechanism terms 作为 frontier search seed。Frontier queries 应从已冻结 problem families 导出。

## AGENDA-21 — Agenda challenge trigger
只有存在记录的 trigger 时才 reopen broad finance/business search，例如：多轮完整 agenda census 均无可信 survivor；独立 candidate families 反复遭遇结构性不可行；或用户明确要求。

## AGENDA-22 — External discovery handoff
ScholarOps 外部发现的候选可进入 focused pre-admission screening，并把 upstream provenance 标为 preliminary。不要仅为了适配旧 schema 就重跑完整 landscape，也不能绕过缺失 gates 直接把 handoff 提升到 deep adjudication 或 empirical work。

## AGENDA-23 — Neutral lifecycle coverage
当 agenda 是 AI 与 financial-information lifecycle 时，中性覆盖 acquisition、processing、production、validation、use、intermediation 与 aggregation。某一层可以被判定 saturated、no actionable gap 或 hold for future data；不要为填满每个格子而发明 candidate。

## AGENDA-24 — Direction-neutral candidate judgment
不要因为候选符合“AI improves efficiency”或“AI increases homogenization”等有吸引力的故事就加分。依据 problem importance、evidence、construct validity、identification、executability、finance significance 与 decisive negative result 的价值评估。Positive、negative、null outcome 都应能在结果前被解释。

## AGENDA-25 — Architecture decomposition
Model、data、tool、Skill、planning、verification 与 multi-agent choice 是 production inputs，本身不是 contribution categories。若改变 architecture 只改变 engineering performance，则降低 finance contribution；只有改变 financial inference、mechanism 或 allocation decision 时才保留。
