# 05 — Project State and Isolation（简体中文正式译本）

> 英文 `05_PROJECT_STATE_EN.md` 是唯一 canonical semantic source。

## PROJ-01 — Project state schema
每个 active project 在相关时应记录：

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

如果项目退回更早阶段，还要记录：

```text
STAGE_REGRESSION_REASON / EVIDENCE / SUPERSEDES
```

Project state 不能被新生成的 landscape table、chat summary 或其他项目状态覆盖。

## PROJ-02 — 项目具体取值放在 ScholarOps Core 之外
Event universe、provider admission、measurement threshold、screen/pilot result、data version、code version、freeze、failure diagnosis 与当前 empirical result 都属于 project artifact set。ScholarOps 定义 schema 与治理，不定义用户项目的具体数值。

## PROJ-03 — Project isolation
不同研究项目不能继承彼此的 status、results、freezes、Seen Data state、claims 或 failure verdicts。

复用 data asset 时记录 `ASSET_REUSED=YES`，明确只复用了 asset。任何 project result 或 design state 都不会自动继承。

## PROJ-04 — Inactive / blocked / held / closed 项目保持隔离
一个 inactive、blocked、held 或 closed project 不阻止另一个项目进行低成本 discovery。若重新考虑该项目，应恢复它自己的 prior stage 与 blocker，而不是假装过去工作不存在，或继承其他项目的当前状态。

`CLOSED_PROJECT` 不能悄悄重新进入 active pipeline。Reopen 必须有记录的 reopen condition，以及满足该条件的新证据。

## PROJ-05 — 泛化的多项目角色
同时管理多个研究时，分离以下角色：

```text
PRIMARY_PROJECT
ACTIVE_CHALLENGER
ALTERNATIVE_PROJECT
LONG_HORIZON_RESEARCH_AGENDA
HOLD_FOR_FUTURE_DATA
CLOSED_PROJECT
```

Literature map 或 candidate scan 不自动取代 primary project。Project switch 需要单独比较 research problem、contribution、evidence maturity、executability、time cost 与 fallback value。

## PROJ-06 — Cross-project asset reuse
跨项目复用 asset 前检查：

```text
identity / date range / construct compatibility / point-in-time legality /
hash-or-reference / licensing
```

Asset reuse 不表示 measurement、sample construction、estimand 或 treatment rules 可以无条件迁移。
