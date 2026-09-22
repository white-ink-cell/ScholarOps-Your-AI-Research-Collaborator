# 04 — Access and Resource Interface（简体中文正式译本）

> 英文 `04_ACCESS_INTERFACE_EN.md` 是唯一 canonical semantic source。本译本用于中文阅读；状态值、字段、Rule ID 与路径保持英文规范形式。

## ACCESS-01 — Access states 不能互换
对每个候选数据源至少区分：

```text
PLATFORM_EXISTS
PUBLICLY_EXISTS
USER_ENTITLED
HISTORICAL_DEPTH_VERIFIED
BULK_EXPORT_VERIFIED
MATCHING_DEPENDENCIES_VERIFIED
ACCESS_USABILITY_STATE
PRIMARY_SAMPLE_ELIGIBILITY
```

平台存在不能证明用户有权限、历史深度可用、能够规模化抽取，也不能证明可以进入 primary sample。

## ACCESS-02 — 重新获取数据前先解析已有资产
如果任务依赖的 asset 可能已经存在，先解析当前附件与已登记项目资产。身份确认、内容未变且没有重新验证触发时，复用已验证 asset。只有所需 asset 确实缺失、不可访问或对当前任务无效时，才重新获取或询问用户。

## ACCESS-03 — WRDS 与机构许可数据库
能够登录 WRDS 或其他 institutionally licensed platform，只证明平台入口可用。必须验证设计真正需要的具体 database、table、fields、years、export mode 与当前 subscription。

## ACCESS-04 — Usage-based market-data services
现有 credits、过去购买或历史访问不代表当前拥有所有 dataset、year、schema 或 delivery mode。针对实际样本验证 entitlement 与预期成本。

## ACCESS-05 — LSEG 与类似终端/API
不能因存在标准 UI 就推断 API、Datastream、tick-history 或 premium add-on 权限。未经历史深度与导出规模测试的 UI 路径，不能暗中支撑 large-sample design。

## ACCESS-06 — Bloomberg 与共享终端资源
不能因为机构“有 Bloomberg”或类似终端，就推断存在 scalable research access。要区分 manual lookup、limited export、API/bulk，以及是否根本不适合 proposed primary sample。

## ACCESS-07 — 已验证 entitlement 高于泛化平台宣传
当前用户/机构 entitlement evidence 与实际 probe 高于通用 vendor page。Vendor documentation 只能证明 API/dataset 存在，不能赋予用户并未拥有的权限。

## ACCESS-08 — 已知不可用路径不要反复消耗搜索成本
某路径已经验证为 not entitled、excluded 或不在当前 access universe 时，不要反复把它当作下一条 acquisition route，除非用户报告相关变化或出现新的合法访问路径。

## ACCESS-09 — Access 对研究重要时维护 access registry
按需记录：

```text
provider / source / entitlement / UI / API / bulk / historical depth /
cost state / usability / tested_at / verification / candidate identifiers
```

当 history、scale、matching 或 cost 决定 executability 时，不能把重要 access decision 压缩成单一 yes/no。

## ACCESS-10 — Assistant-first execution
当宿主可以合法访问文件并执行所需处理时，应由 Agent 直接完成，而不是把可运行工作转给用户。只有 credentials、institutional login、paid access、local-only resource 或 host limitation 真正阻塞时，才要求用户完成最小必要步骤。

## ACCESS-11 — 宣布 access failure 前先找合法替代路径
在 `BLOCKED_ACCESS` 前，按比例搜索合法 public bulk/API source、public repository、author replication package、实际已订阅 institution resources、现有 credits、合法 educational/free access 与 construct-preserving alternatives。

理想 published dataset 是私有的，本身不等于研究问题不可行。

## ACCESS-12 — Fallback 要么保持 construct，要么降低 claim
对任何 substitute 比较：

```text
unit / target / timing / construct / coverage
```

如果 substitute 改变研究对象、timing、construct 或 target population，必须记录 substitution 并收窄 claim。未验证时不得把低质量 source 描述成 construct-equivalent。

## ACCESS-13 — 记录 access evidence 强度
可使用如下 evidence ladder：

```text
DOC_ONLY / SCHEMA_VERIFIED / SAMPLE_PROBED / BULK_TESTED / HISTORICAL_DEPTH_VERIFIED
```

当规模或历史深度是关键时，documentation alone 通常只能让 primary-sample executability 保持 conditional。

## ACCESS-14 — Scalability 属于 access feasibility
如果设计要求长期逐证券或逐事件手工提取，记录 `MANUAL_EXTRACTION_BURDEN`。能够看到一条记录，不等于拥有 scalable、reproducible access。

## ACCESS-15 — 不因熟悉某条数据管线而偏置研究选择
已有某类数据 pipeline，不能让使用该类数据的候选自动显得更 executable。对替代数据源应用相同的合法 access search 与 construct-preservation test。

## ACCESS-16 — Cost state 与 usability state 分开
需要时按以下类别记录 cost：

```text
ZERO_COST_CONFIRMED / INCLUDED_IN_SUBSCRIPTION / COVERED_BY_FREE_CREDIT /
FREE_WITH_LIMITS / UNKNOWN / NEW_PAID_ACCESS_REQUIRED
```

usability 使用：

```text
SCALABLE / LIMITED_UI_EXPORT / MANUAL_LOOKUP_ONLY / REFERENCE_ONLY /
EXCLUDED_BY_DEFAULT / UNVERIFIED / NOT_ENTITLED
```
