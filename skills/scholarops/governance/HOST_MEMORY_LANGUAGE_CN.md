# 08 — Host Memory, Recovery, Evidence and Language（简体中文正式译本）

> 英文 `HOST_MEMORY_LANGUAGE_EN.md` 是唯一 canonical semantic source。本译本用于中文阅读；Rule ID、字段、状态与路径保持英文规范形式。

## GOV-EVID01 — Evidence hierarchy
当来源冲突时，使用最强的直接证据。Project-state note 或 conversation summary 不能仅因写着“已完成”，就覆盖 frozen artifact、verified hash/content identity、executed code/log 或其他更强 direct evidence。

实用优先级：
1. frozen canonical artifacts 与 direct audit results；
2. executed code/logs 与 verified data/output artifacts；
3. contemporaneous reports 或 conversation records；
4. retrospective summaries；
5. proposals/plans；
6. model memory。

该层级依据 evidentiary strength，而不是文件名。

## GOV-STATE01 — Mechanically derive next state
当前 research stage 与 allowed next step 必须从 required artifacts 与 gates 机械推导，而不是相信 README 或 chat 里声明的 `COMPLETE`。

长期项目只维护 active workflow 真正需要的 state fields。Git 是可选的。Persistent state 可以放在 project-local `.scholarops/` 或等价 host-specific location，但只有 persistence 有价值且用户允许时才创建。

## GOV-RES01 — 先解析已有资产，再要求用户重新提供
当前任务依赖此前生成/上传/获取但未附在本消息的 asset 时，先搜索当前 workspace 与 registered project assets。复用前确认 identity/version；asset 未改变且没有 re-verification trigger 时复用 prior verification。只有 asset 真正不可获得时才要求用户再次提供。

不能把“模型没记住”误当作“asset 不存在”。

## GOV-CONV01 — Evidence reconstruction and handoff
`RE` 的含义是：恢复最新 canonical project state，与 registered artifacts 交叉验证；只有 canonical state 缺失/矛盾，或用户要求历史重建时，才查 archived conversation evidence。

恢复顺序：

```text
host/project instructions
→ current structured state
→ decisions and artifact registry
→ open issues and relevant structured memory
→ current project artifacts
→ archived sessions/transcripts only when needed
```

不能仅因用户请求恢复就读取 result-sensitive archive content；必须遵守当前 Seen Data/blinding boundary。

Handoff summary 不等于 verbatim transcript。只有底层 conversation record 实际可获得/导出时，文件才可称 transcript。不得根据 model memory 补写丢失历史并标成完整记录。

当 `RE` 是用户唯一请求时，恢复并报告 state、缺失的 required assets 与 blockers，然后停止，不得悄悄推进下一 research gate。

## GOV-TRANSCRIPT01 — Transcript completeness audit
对真实 conversation/session archive，记录足够 provenance 来区分完整 source 与 partial handoff，例如：

```text
TRANSCRIPT_ID
FILE_HASH
SOURCE_OR_EXPORT_METHOD
FIRST_VISIBLE_TURN
LAST_VISIBLE_TURN
DATE_RANGE
STRUCTURAL_TRUNCATION_SIGNAL
EXPLICIT_TRUNCATION_MARKER
UNRESOLVED_LATER_REFERENCE
TRANSCRIPT_COMPLETENESS_STATUS
TRANSCRIPT_GAP_IMPACT
```

Hash 证明 fixity，不证明 completeness。出现 truncation marker、abrupt ending、无法解释的 message/time gap，或对缺失后续决定的引用时，必须进行 `PARTIAL` 或 `UNKNOWN` review。

## GOV-SEEN02 — Upstream factual correction 合法；outcome-driven redesign 不合法
Unblinding 后仍允许修正有独立证据证明的 upstream factual error。先分类 trigger：

```text
REVISION_TRIGGER =
UPSTREAM_SOURCE / DESIGN_PRESPECIFIED / OUTCOME_DRIVEN / UNDETERMINED / NOT_APPLICABLE
```

`UPSTREAM_SOURCE` correction 只有在 trigger 来自 upstream source 本身而非 observed result、correction rule 一致作用于所有相关 units、且 correction 与 evidence 进入 repair ledger 时才合法。它不会恢复 blindness，也不会重置 Seen Data。

`OUTCOME_DRIVEN` redesign 不能作为 confirmatory repair。Trigger 无法确定时，在解决前保守地按 outcome-driven 处理。

Blindness principle 的方法来源登记在 `EMP-BLIND01`；`EMP-BLIND01A` 是 ScholarOps implementation layer。该规则修复私人包的 broken method-source locator，而不改变实质规则。

## GOV-ACT01 — Irreversible actions 保持不可逆
区分 warning、recoverable runtime failure 与 irreversible external action。看到 main effect、提交 external task、产生费用、发送消息或发布文件，不会因后来报错而自动撤销。

结果已被看到后，implementation repair 可能依据 repair rules 合法，但在已观察 scope 内项目仍然是 unblinded。

## GOV-AUDIT01 — Current-workflow audit (`AU`)
`AU` 基于现有证据审计当前研究工作流，定位最早的 material gap 或 inconsistency，区分 presentation issue 与 research-state defect；若没有另一项独立任务，则审计完成后停止。

Conversation order 可以证明曾提出请求或承诺；要证明工作实际发生，需要 artifact/log/hash evidence。

## GOV-LANG01 — User-facing language
除非用户明确指定其他语言，解释与判断使用用户当前语言。Canonical names、paper titles、author names、venues、DOIs、必要时的 search queries、code、field names、rule IDs、controlled vocabulary 与 machine schemas 保持其规范/原始形式。

Canonical machine/runtime layer 始终只使用英文。
