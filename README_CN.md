# ScholarOps — 你的 AI 研究合作者

**面向金融、会计、经济、保险与实证商科研究。**

[English](README.md) · **v1.0.0** · **Codex verified** · **Apache-2.0**

**还在因为找不到合作者而焦虑？还在等一条迟迟不来的回复？还希望有人愿意陪你把每一条引用、每一个数据处理、每一个实证细节重新过一遍？**

ScholarOps 把 AI 变成一个可以一直陪你盯细节的研究合作者。它可以和你一起逐字读论文、逐条追引用、重新走数据流程、反复琢磨研究设计，并检查最终的 claim 是否真的和证据对得上。它更像多了一位始终盯着细节的合作者，从 **来源 → 数据 → 设计 → 结果 → 结论** 一直陪到文章成形。

ScholarOps 来自对真实金融实证研究流程的反复使用，并在首个公开版本发布前，用合成研究案例完成了 Codex 端到端行为验证。

## 它能和你一起做什么

- **文献与引用** — 找最近的前序研究和危险邻居，确认文献身份与定位，并逐条检查引用是否真的支持对应句子。
- **数据与测量** — 检查数据权限、原始数据 QA、标识符、匹配、缺失、尾部、变量构造、aggregation，以及数据是否仍然测量原本的 construct。
- **研究设计** — 核查 unit、estimand、treatment、timing、identification、inference、sample support、方法 precedent 与项目特定假设。
- **结果前纪律** — 管理 freeze、blindness、Seen Data、pilot/screen 边界，以及哪些研究决定在结果被打开后已经不可逆。
- **结果与结论** — 检查 implementation QA、表图与执行结果一致性、multiplicity、specification search、economic threshold，以及证据最高能支持到什么 claim。
- **长期项目** — 管理 artifact identity、reproducibility、structured state，用 `RE` 恢复项目，用 `AU` 向前追溯工作流缺口。

Full Skill 还包含一个可选的 **AI × Finance** profile，用于 AI capability、adoption、decision、holdings/trades 与 market outcome 等研究问题。

## 快速开始

### 方式 1 — 不安装 Skill

直接使用可复制提示词：

- [快速开始 — 简体中文](quickstart/QUICK_START_CN.md)
- [Quick Start — English](quickstart/QUICK_START.md)

### 方式 2 — 在 Codex 中安装 Full Skill

```bash
git clone https://github.com/white-ink-cell/scholarops-research.git
mkdir -p ~/.agents/skills
cp -R scholarops-research/skills/scholarops ~/.agents/skills/
```

Codex 会从 `$HOME/.agents/skills` 发现用户级 Skill。可安装目录是：

```text
skills/scholarops/
```

安装后直接用自然语言工作。例如：

```text
仔细读这段文献综述。找最近的前序研究，并逐条核查引用是否真的支持对应的 claim。
```

```text
从这张回归表向前追溯数据构造，告诉我整个实证流程里哪些地方可能出错。
```

```text
在打开主结果前，冻结 hypothesis、sample、variables、thresholds 和 main specification。
```

```text
AU
```

`AU` 会向前追溯整个工作流，找到最早的实质缺口；`RE` 会从 structured state 与已登记 artifacts 中恢复当前最可信的项目状态。

## 研究流程

```text
研究问题
→ 文献 landscape / focused census
→ 撞题与 contribution check
→ construct / measurement / identification
→ 数据获取与 QA
→ 结果前 freeze
→ 可选 outcome screen
→ formal empirical study
→ robustness / specification governance
→ evidence-to-claim review
→ reproducibility 与 project state
```

ScholarOps 会按当前项目真正存在的风险激活检查，让工作流与研究问题本身保持匹配。

## 为什么它更像一个研究合作者

### 在真实论文流程里反复打磨

ScholarOps 在真实金融实证研究项目中反复使用和修改，覆盖从文献与数据处理到正式结果与 claim 的完整流程。v1.0.0 随后完成了 10 个原生 Codex 行为案例验证，覆盖 routing、`RE`、`AU`、blindness-safe recovery、文献 collision、screen/formal-study 分离、data fallback、profile isolation 与 persistence boundary。

### 它会一直盯住细节

一篇论文可能因为一个很小的错出问题：引用了错误版本、文献只支持半句话、identifier merge 改变了样本、proxy 偏离 construct、看过结果后又改 specification，或者表格已经和实际执行输出不一致。ScholarOps 会把这些细节重新拉回研究判断本身。

### 它会把文字背后的证据重新翻出来

Executed code、logs、frozen artifacts、source records 与 verified outputs 会被放在比方便的 summary 或过期 notes 更高的位置。这样更容易发现隐藏错误、重新核查假设，并让长期研究流程始终和实际做过的事情对得上。

## 适合的场景

- MSc dissertation 与实证硕士论文
- RA / predoc 研究
- PhD paper 与 working paper
- 文献与 citation checking
- data pipeline 与 measurement checking
- empirical design / identification review
- result-to-claim 一致性核查
- 长周期研究项目的 reproducibility 与 handoff

## 方法来源

外部方法依据统一登记在：

```text
skills/scholarops/references/METHOD_SOURCE_REGISTRY.csv
```

Registry 记录 source、locator、verification status，以及该来源实际支持到哪里。ScholarOps 自己的 workflow rule 与外部方法依据保持区分。

## 仓库结构

```text
scholarops-research/
├── README.md
├── README_CN.md
├── quickstart/                 # 可复制提示词
├── examples/                   # 合成研究案例
├── skills/scholarops/          # Full Skill
│   ├── SKILL.md
│   ├── modules/
│   ├── governance/
│   ├── profiles/
│   ├── references/
│   └── runtime/
├── spec/                       # maintenance source spec
├── tooling/                    # runtime builder / validator
└── tests/                      # release checks
```

## 验证

**v1.0.0** 已完成：

- 原生 Codex 端到端行为验证；
- source/runtime consistency checks；
- generated-runtime drift checks；
- bilingual human-facing checks；
- public privacy 与 source-body scans。

原生验证使用 **Codex CLI 0.155.1** 与合成研究 fixtures 完成。

## Issues

Bug、文档问题和 feature request 请使用 [GitHub Issues](https://github.com/white-ink-cell/scholarops-research/issues)。

## 引用

见 [`CITATION.cff`](CITATION.cff)。

## License

[Apache License 2.0](LICENSE)
