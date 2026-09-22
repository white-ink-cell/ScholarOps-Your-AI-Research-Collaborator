# 07 — Artifact、State 与 Reproducibility Governance（简体中文正式译本）

> 英文 `07_ARTIFACT_STATE_REPRODUCIBILITY_GOVERNANCE_EN.md` 是唯一 canonical semantic source。

## A. Artifact identity、fixity 与 verification

## GOV-ART00 — Selective Hash / Fixity Policy
Hash 不是每个 intermediate file 都必须完成的仪式。

默认对两类资产进行 hash/fingerprint：

1. **Milestone artifacts**：当前 delivery 的 milestone class 不为 `NOT_APPLICABLE` 时，该 milestone 所需 canonical artifacts 需要 fixity evidence。
2. **Non-regenerable inputs**，包括：

```text
RAW_OR_EXTERNALLY_ACQUIRED_INPUT
NON_REGENERABLE_MANUAL_LABEL_OR_GOLD_DATA
```

这些输入即使不是 milestone deliverable，也因无法通过 `raw + frozen code` 重新生成而需要特殊保护。

由 `raw + frozen code` 机械可再生的 scratch files、caches、temporary merges、ordinary diagnostic tables 与 disposable intermediates，默认不需要逐个 hash。

当 intermediate 被 downstream formal result 直接复用、重建代价高/不可能，或存在显著版本混淆风险时，把它升级为 hashed asset。

原则：`fixity effort ∝ irreproducibility or version-confusion risk`。

## GOV-ART01 — Artifact identity
用以下信息去重 artifact：
`canonical location / hash / content identity`。

允许状态：
`ORIGINAL / RESTORED / GENERATED_LATER / MISSING / SUPERSEDED`。

文件名相似不能证明内容相同。

## GOV-ART02 — Verification reuse / re-check triggers
`GOV-ART00` 控制 verification intensity；本规则控制 verification frequency。

核心原则：

> 已记录 verification 在其声明 scope 内持续有效，直到出现 re-verification trigger。重新验证由变化触发，而不是因为开始了一个新任务。

对没有变化的数据反复做 file identity、parsing 或 field checks，不是额外严谨，而是重复固定成本。

先分类 asset mutability：

```text
ASSET_MUTABILITY = FROZEN_SNAPSHOT / LIVE_SOURCE / UNKNOWN
```

- `FROZEN_SNAPSHOT`：内容与位置固定且已记录 hash；scope 内可复用 prior verification。
- `LIVE_SOURCE`：API、live database query、可能被他人覆盖的 shared location 或 rolling directory；不能假设 prior verification 继续有效。
- `UNKNOWN`：当前任务内完成分类前，按 live 处理。

若同一 live asset 反复被使用，优先把它冻结成 snapshot 并记录 hash，而不是永远重复完整验证。

以下情况重新验证：

```text
1  current file hash differs from verified_hash
2  version, vintage, or period changes, including vendor restatements or redownloads
3  canonical location changes and content identity is not established by hash
4  the current use exceeds verification_scope
5  schema, parser, code, or toolchain used to read the asset changes
6  an evidence error or claim drift is discovered
7  no verification record or verified_hash exists where one is required
8  ASSET_MUTABILITY=LIVE_SOURCE
```

Verification scope 必须写到后续使用者能够与新用途比较。“Verified”但没有 scope，不可复用。

记录：

```text
FIRST_VERIFICATION
REUSED_UNCHANGED
REVERIFIED_TRIGGERED
BLOCKED_UNVERIFIABLE
```

`REUSED_UNCHANGED` 可跳过重复 parsing/profiling，但不能跳过 identity comparison。
`BLOCKED_UNVERIFIABLE` 仍可允许 exploration，但除非 freeze layer 明确解决或接受限制，不能支撑 formal results。

接口：
- `GOV-ART00` 决定是否应有 hash；
- `GOV-ART01` 提供 location/hash/content identity；
- prior-asset resolution 应把 candidate artifacts 交给本规则，而不是自动重做 full QA；
- 已完成 verification 属于完成的工作，不能因新任务开始而回退。

## GOV-PATH01 — Location identity
使用受控 `PATH_TYPE` vocabulary。
未知位置记录：`UNKNOWN — DO NOT GUESS`。

## B. State 与 registries

## GOV-STATE02 — Stage non-regression
已完成 gate 不会因新会话或 summary 而回退。
只有以下情况可返回更早 stage：
`evidence error / claim drift / superseding artifact`，并记录：
`reason / evidence / supersedes`。

## GOV-REG01 — Registry Identity / Drift
Project IDs 必须在 master registry、lineage 与 current state 中一致。
没有 documented provenance 的 ID 是 `UNREGISTERED_CANDIDATE` 或 `DISCOVERY_ID`；不得悄悄提升为 formal primary project。

## GOV-REG02 — Registry minimum schemas
当对应治理风险激活时，至少维护以下逻辑 schemas。

### PROJECT
`project_id / project_status / agenda_role / queue_role / last_gate / next_gate / canonical_artifact / updated_at`

### DATA ASSET
`asset_id / source / version / period / fields / unit / location_type / location / hash / acquisition / reuse / asset_mutability / verified_at / verified_hash / verification_scope / verification_result`

最后五个字段为 `GOV-ART02` 提供落点；没有它们就无法安全复用 verification。

### ACCESS
`provider / source / entitlement / history / API_UI_bulk / cost / usability / tested_at / verification`

### SEEN DATA
`candidate / dataset / outcome_or_effect_seen / what_seen / when / by_whom / consequence`

### LITERATURE
`source_id / bibliographic identity / version / source_role / authority / candidate / read status`

扩展 registry 时通过 schema extension；不要创造近义临时列绕过 canonical schema。

## C. Upstream packages 与 schema migration

## GOV-UP01 — Upstream transition audit
进入下一个 gate 前检查真实 upstream package：
`manifest / canonical files / required audit files / freeze / source map`。
不能依赖 README 里一句“已完成”。

## GOV-UP02 — Schema migration
如果 old package 只缺 column name、normalized row 或可由现有证据无损重构的 field，可以做 `SCHEMA_ONLY_REPAIR`，同时保留 migration/supersession map。

从未有证据的值使用 `NOT_RECORDED` 或 `NOT_OBSERVABLE`，不得猜测。
如果缺失的是 substantive completion evidence 而不是 schema form，保持 prior stage，只修精确 evidence gap。

## D. Claim drift

## GOV-DRIFT01 — Claim-changing return
如果 L4、Method 或 Pilot repair 后继续研究需要改变：
`actor / estimand / field wedge / evaluation anchor / base scope / claim ceiling / core treatment`，设置：

```text
CLAIM_DRIFT=YES
RETURNED_FOR_REFREEZE
```

并记录：`old claim → trigger evidence → proposed new claim`。

不能一边改变 study，一边假装仍通过原 gate 继续推进。

## E. Seen Data

## GOV-SEEN01 — Seen Data Register
记录任何会消耗 confirmatory flexibility 的结果，包括 treatment coefficients、event-time outcome plots、treatment-group summaries、high/low-exposure outcome differences、alternative cleaning 后的 candidate outcomes，以及 pilot progression results。

B0/B1 下合法 blind diagnostics 不自动构成 effect-seen event。
一旦 effect 被看到，重命名或移动文件不能恢复 blindness。
打开 effect 同时设置 governance layer 要求的 irreversible-action status；后来执行失败也不能抹除“结果曾被看过”这一事实。

### Seen status 有 scope
每条记录必须说明看到了哪个 outcome family、module 与 units。
打开一个 module 不自动破坏真正未见 sister module 的 blindness；反之，scope 含糊时保守处理。

### 记录不等于修复 error rate
Register 只记录已消耗的 flexibility，不能恢复 type-I-error control。“已经记日志了”不能让已经看过的数据重新成为 confirmatory evidence。合法 reuse 必须遵循 prespecified reuse design，而不是事后登记。

### 没有 unseen units 就没有新的 out-of-sample confirmation
如果 provider、stratum 或 subsample 中没有 unseen units，它仍可提供 development 或 descriptive evidence，但不得描述为新的 out-of-sample confirmation layer。Previously seen units 可以单独报告，但不能与新 confirmatory sample 合并后冒充 fresh evidence。

## F. Reproducibility 与 replicability

## GOV-REP01 — Reproducibility
Reproducibility 问的是：相同 data、code 与 conditions 能否重新生成相同结果。
Formal results 至少应可沿以下链条追溯：
`Result → Code → Processed Data → Raw or Source Data`。

## GOV-REP02 — Replicability
Replicability 问的是：new data、new sample 或 independent implementation 在同一 scientific question 下是否得到一致结果，或产生可解释差异。
对有影响力 claim 的 high-value replication 本身可能是科学贡献，不能仅因 broad question 相同就自动终止。

## G. Delivery 与 task closure

## GOV-CLOSURE01 — Task Closure Self-Validation
遵守：

```text
CLAIMED_COMPLETE ≤ VERIFIED_COMPLETE
```

对话里声称“已经完成”不能高于真实 verification status。

### Ordinary delivery
使用 `TASK_CLOSURE_DEPTH=LIGHT`。不需要专门 closure artifact；Agent 在 final response 前完成相关检查。

### Milestone delivery
Milestone class 激活时使用 `TASK_CLOSURE_DEPTH=MILESTONE`。Milestone 应保留或更新足够证据证明完成，包括 execution/result artifacts、必要 QA、current state/verdict，以及 milestone 要求的 manifest/hash/package。
如果已有 QA/log 已证明相同事项，不要再制造冗余长篇“自检报告”。

### Repair closure
最后一次 validation 之后发生任何 result/state-changing modification，都会使此前 closure pass 失效。设置 `REVALIDATE_AFTER_LAST_CHANGE=YES`，交付前验证最终 post-change 版本。

## GOV-DELIV01 — Milestone-Triggered Deliverable
普通 intermediate task、QA check 或一次性 diagnostic，默认交付：
- 相关时，实际使用的 code；
- result tables、figures 或 logs；
- 简短说明 input、action、finding 与 next step。

不要要求每个 intermediate task 都生产完整 `README + MANIFEST + SHA256SUMS + ZIP`。

真正 milestone 则生成该 milestone 所需的完整 release-style package，包括 canonical Markdown、必要 CSV/JSON logs、README、manifest、按 `GOV-ART00` 选择的资产 hashes，以及适用时 ZIP 或等价 bundle。
不逐个 hash 机械可再生 intermediates。

Package 名在离开对话后仍应可识别，例如：
`project_stage_purpose_date_version.zip`。
Manifest 不得 self-reference 包含它自己的 ZIP。

## GOV-DELIV02 — Completion summary
正式研究任务结束时报告：
`VERDICT / ALLOWED_NEXT_STEP / FORBIDDEN_NEXT_STEPS / REGISTRY_UPDATES`。
`ALLOWED_NEXT_STEP` 只给一个优先 next action，而不是无优先级列表。
普通解释性 Q&A 不需要完整 state template。

## H. Failure assets 与 reopening

## GOV-FAILASSET01 — Failure Asset Extraction
终止的 research branch 不被删除，而进入 terminated-branch archive。
适用于 research-census termination、L4 termination、screen 的 stop-resource decision，以及在 branch 被关闭时的 structurally blocked access。

Archive 至少记录：

```text
TERMINATION_REASON
FAILURE_CLASS
TERMINATION_STAGE
EVIDENCE_SNAPSHOT
SEEN_DATA_STATUS
REUSABLE_ASSETS
COOLDOWN_KEY
REOPEN_CONDITIONS
TERMINATED_BRANCH_FINGERPRINT
TERMINATION_ARCHIVE_STATUS=COMPLETE
```

`COOLDOWN_KEY` 必须标识稳定 claim/estimand，而不是 display name。给失败 idea 改名不能绕过 cooldown。
终止后允许做一次 reusable-data/code/method/source extraction，但 reusable assets 不会自动 reopen terminated hypothesis。

## GOV-COOLDOWN01 — Reopen
当某 claim/estimand 已积累规定 termination history 时，重启相似 candidate 前按 `COOLDOWN_KEY` 检查 terminated-branch archive。
机械判断这是有新证据支持的合法 reopen，还是换名字后的同一 terminated idea。

Reopen 需要可审计 trigger，例如 new data、new shock、stronger identification、construct correction、adjudicating evidence、mechanism、boundary condition、regime change 或 high-value replication opportunity，并记录 prespecified `REOPEN_CONDITIONS` 是否满足。
项目关闭后，如果没有存活 research question 需要，不要继续 speculative data expansion。

## I. Research-relevant QA

## GOV-QA01 — Research-relevant QA
只有能够影响 research conclusion、data integrity、citation traceability 或 file readability 的 QA 才改变 research verdict。
Browser quirks、styling 与 presentation-only issue 单独跟踪，本身不改变 research gate。

## J. Skill release identity 与 validation

## GOV-VERSION01 — Skill release identity / fixity
ScholarOps release 本身也是可追踪 artifact。
每个 stable release 记录 release metadata 与 canonical fingerprint；算法与 scope 由 public maintenance specification 定义。Validator 必须机械重算 fingerprint，不能因为文件里写了一个值就信任。

Fingerprint 用于 version identity 与 fixity，不是通用 anti-tamper security guarantee。如果同一 nominal version 有多个副本，内容不同必须产生不同 identity，canonical-version decision 不能依赖 modification time 或肉眼判断。

Release metadata 只保存 identity facts，不作为自我签发的 validation certificate。被验证对象不能自己证明自己有效。

版本一旦公开发布，不得静默修改内容。任何内容变化都要求新 release version。该 immutability principle 与 Semantic Versioning 2.0.0 section 3 一致；但 ScholarOps 自己的 major/minor/patch policy、fingerprint algorithm 与 manifest rules 是本项目工程选择，不能归因给 SemVer。

## GOV-VERSION02 — Stable release requires validator PASS
Release 只有在当前 public architecture 所需 checks 全部通过后才能标记 stable，包括：
- structural validation；
- semantic-invariant validation；
- recompute canonical fingerprint；
- 最后一次 package 修改后重新生成 manifest/checksum material；
- final check-only validation pass；
- 对 final immutable package 做 detached attestation，包括最终 validator result 与 package checksum（若 release process 使用此类 bundle）。

不能发布一个已知失败的 stable package，并承诺“下个版本再修”。
