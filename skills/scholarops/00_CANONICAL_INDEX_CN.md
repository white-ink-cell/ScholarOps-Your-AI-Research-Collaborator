# ScholarOps — 规范索引 / 路由器

ScholarOps 是一套面向金融、会计、经济、保险及相关商科研究的证据约束型研究工作流与研究治理 Skill。它不是自主科研 Agent、通用金融助手，也不是论文语言润色系统。

> **语义权威说明：** 英文 canonical 文件是 ScholarOps 的唯一规范语义源。本文件是经核对的简体中文正式译本；Rule ID、状态值、字段名、路径、DOI、代码与 controlled vocabulary 均保留其英文规范形式。若翻译与英文 canonical 出现任何歧义，以英文 canonical 为准，并应修正译文，而不是让两套规则分别演化。

## 0. 规范架构

ScholarOps 区分两类事实来源：

- **机器治理架构（machine-governed architecture）**：在仓库 source spec 中维护，并以生成后的 runtime registries 随 Skill 分发；
- **研究语义规则（semantic research rules）**：只在英文 canonical modules 与 optional profiles 中维护一次。

生成的 runtime 文件不得手工编辑。如果仓库中的 bundled runtime 与 source spec 不一致，则该 release 无效，必须重新 build 并 validation 后才能发布。

可安装 Skill 本身必须自包含。仓库级 build / validation tooling 属于维护基础设施，不是运行时依赖。

## 1. 加载纪律

不要默认加载所有模块。

1. 先读取 `runtime/TASK_ROUTER.csv` 与 `runtime/GATE_ACTIVATION_POLICY.csv`。
2. 只加载当前实质研究任务真正需要的模块。
3. 仅当任务明确研究金融、会计、保险或相关商科中的 AI、LLM、Agent、自动化或相关系统时，才加载 `profiles/ai-finance/PROFILE_EN.md`。
4. 若只需查找某条特定规则，优先使用 `runtime/RULE_LOCATOR_INDEX.csv`，不要加载无关模块。
5. 当方法规则需要核对来源或 provenance 时，使用 `references/METHOD_SOURCE_REGISTRY.csv`。

Risk-adaptive gates 与 artifacts 只有在对应风险实际存在时才激活。一次性的小任务不得被迫建立完整的项目治理官僚体系。

## 2. 宿主选择边界

是否选择或加载 ScholarOps，由宿主环境决定。一旦 ScholarOps 已被加载，由 ScholarOps 内部对当前研究任务进行路由，不需要额外的 execute 命令。

ScholarOps 适用于实质性的研究工作流任务，例如：研究问题形成、文献/撞题筛查、贡献裁决、研究设计、数据/测量工作、结果前治理、实证验证、证据/主张纪律、可复现性、项目恢复或工作流审计。

不要把 ScholarOps 自动扩展到普通金融概念解释、翻译、邮件起草、一般代码帮助或与研究工作流无关的文字编辑。

## 3. 命令优先级

ScholarOps 只保留两个工作流快捷命令：

- `RE` — 从 canonical structured state 与已登记 artifacts 中恢复当前项目；仅在必要时查阅 archived conversation evidence。若 `RE` 单独出现，只报告恢复后的状态与 blocker，然后停止。
- `AU` — 审计当前研究工作流，定位最早的实质性缺口或不一致；若 `AU` 单独出现，不自动推进到下一研究阶段。

如果一条消息除 `RE` 或 `AU` 外还包含明确的实质研究任务，则先执行快捷命令；只有当恢复/审计后的状态允许时，才继续路由该实质任务。

优先级：

```text
CANONICAL_VERSION_RESOLUTION
→ RE (when invoked)
→ AU (when invoked)
→ CONCRETE_RESEARCH_TASK
```

## 4. 项目状态与记忆

持久化 ScholarOps 项目状态是可选的，只有在确有价值并获得用户许可时才初始化。项目本地 `.scholarops/` 是 Codex-first 的推荐布局，不是所有宿主必须遵循的通用路径要求。

Structured state 是活动工作流记忆。更强的 artifact、hash、实际执行代码/日志与 audit evidence，高于仅仅声称“已经完成”的 state note。原始对话/session archives 是 fallback evidence，不是默认 active memory。

不得仅为恢复上下文就打开对结果敏感的 archives。恢复过程必须遵守当前 Seen Data / blindness 边界。

Git integration 是可选的，由用户决定。

## 5. 结果前治理

Pre-result blindness、Seen Data tracking、freeze、irreversible-action tracking，以及防止 outcome-driven redesign 的控制，是 ScholarOps 的核心能力。一旦结果已经被看到，后续即使发现 bug 并修正，也不会恢复到盲态。

`OUTCOME_DECISION_SCREEN` 只用于资源分配决策。正式的 SESOI、equivalence、minimum-effect 或 economic-null 裁决属于 Freeze B / `FORMAL_STUDY`。

## 6. 证据与撞题纪律

基于文献撞题给出 stop 或 narrowing 判断，必须有足够强且足够直接的证据支持所声称的不利命题。弱相邻证据只构成 verification lead，不能构成正式 narrowing verdict。

对外专业术语使用 `STOP / CLOSED / REOPEN` 管理研究分支。Stop 必须记录为什么停止，以及需要什么新证据才能 reopen；它不自动意味着某个经济效应已被证明不存在。

## 7. 访问与执行

Access 必须按能力事实判断。平台存在不等于用户有权限；有权限不等于拥有足够历史深度；能够查看不等于能够进行可扩展的研究访问。

当宿主可以合法读取相关文件并执行所需处理时，ScholarOps 应自行完成工作，而不是把本可执行的步骤推给用户。只有在 credentials、付费/私有资源、本地独占资产、审批或宿主能力真正构成 blocker 时，才要求用户完成最小必要动作。

## 8. 语言

Canonical machine/runtime 层只使用英文。面向用户的解释默认采用用户当前语言，除非用户明确指定其他语言。规范名称、题名、作者名、期刊/会议名、DOI、代码、字段名、Rule ID 与 controlled vocabulary 保持其规范形式。

## 9. 证据优先级

当证据冲突时，遵循 `GOV-EVID01` 与项目 artifacts。不能因为 README、summary 或过去对话写着“已完成”，就推断该任务确实已经完成。
