# ScholarOps — Your AI Research Collaborator

**For finance, accounting, economics, insurance, and empirical business research.**

[简体中文](README_CN.md) · **v1.0.0** · **Codex verified** · **Apache-2.0**

**Still struggling to find the right collaborator? Still waiting days for feedback on a citation, regression, or draft?**

ScholarOps gives you an AI research collaborator that stays with the details. It can read the paper with you line by line, trace citations back to their sources, revisit the data pipeline, question empirical choices, and check whether the final claim really matches the evidence. Think of it as a patient second pair of eyes that stays with the project from **source → data → design → result → claim**.

ScholarOps was developed through repeated use on a real empirical finance research workflow, then validated end-to-end on Codex with synthetic research fixtures before the first public release.

## What it helps with

- **Literature & citations** — closest prior work, dangerous neighbors, source identity, source locators, and whether a citation actually supports the sentence that uses it.
- **Data & measurement** — access, raw-data QA, identifiers, linkage, missingness, tails, variable construction, aggregation, and whether the data still measure the intended construct.
- **Research design** — unit, estimand, treatment, timing, identification, inference, sample support, method precedent, and project-specific assumptions.
- **Pre-result discipline** — freezes, blindness, Seen Data, pilot/screen boundaries, and the point at which a research decision becomes irreversible.
- **Results & claims** — implementation QA, table/figure consistency, multiplicity, specification search, economic thresholds, and the highest claim the evidence can support.
- **Long projects** — artifact identity, reproducibility, structured state, recovery with `RE`, and backward workflow tracing with `AU`.

The full Skill also includes an optional **AI × Finance** profile for questions involving AI capability, adoption, decisions, trading/holdings, and market outcomes.

## Quick start

### Option 1 — no installation

Use the copy-paste prompt:

- [Quick Start — English](quickstart/QUICK_START.md)
- [快速开始 — 简体中文](quickstart/QUICK_START_CN.md)

### Option 2 — install the full Skill in Codex

```bash
git clone https://github.com/white-ink-cell/scholarops-research.git
mkdir -p ~/.agents/skills
cp -R scholarops-research/skills/scholarops ~/.agents/skills/
```

Codex discovers user skills from `$HOME/.agents/skills`. The installable directory is:

```text
skills/scholarops/
```

Then work in natural language. For example:

```text
Read this literature review closely. Find the closest prior work and verify whether every citation supports the claim attached to it.
```

```text
Trace this regression table back through the data construction and tell me where the empirical pipeline could be wrong.
```

```text
Before I open the main results, freeze the hypothesis, sample, variables, thresholds, and main specification.
```

```text
AU
```

`AU` traces the workflow backward to the earliest material gap. `RE` recovers the latest defensible project state from structured state and registered artifacts.

## Research workflow

```text
Research question
→ literature landscape / focused census
→ collision & contribution check
→ construct / measurement / identification
→ data access & QA
→ pre-result freeze
→ optional outcome screen
→ formal empirical study
→ robustness / specification governance
→ evidence-to-claim review
→ reproducibility & project state
```

ScholarOps activates checks according to the risks present in the current project, so the workflow stays proportional to the research problem.

## Why it works well as a collaborator

### Built through a real paper workflow

ScholarOps grew through repeated use on a real empirical finance research project and was refined across the full workflow from literature and data work to formal results and claims. The public v1.0.0 release was then tested with 10 native Codex behavioral fixtures covering routing, `RE`, `AU`, blindness-safe recovery, literature collision, screen/formal-study separation, data fallback, profile isolation, and persistence boundaries.

### It stays with the details

A paper can fail through a small mismatch: the wrong article version, a citation that supports only half a sentence, an identifier merge that changes the sample, a proxy that drifts from the construct, a post-result specification change, or a table that no longer matches executed output. ScholarOps treats each of these as a first-class research problem.

### It keeps evidence behind the prose

Executed code, logs, frozen artifacts, source records, and verified outputs are treated as stronger evidence than convenient summaries or stale notes. This makes ScholarOps useful for finding silent errors, checking assumptions, and keeping long research workflows anchored to what was actually done.

## Good fits

- MSc dissertations and empirical thesis projects
- RA / predoc research workflows
- PhD papers and working papers
- literature and citation checking
- data-pipeline and measurement checking
- empirical-design and identification review
- result-to-claim consistency checks
- reproducibility and handoff of long-running research projects

## Method provenance

Externally grounded methodological rules are indexed in:

```text
skills/scholarops/references/METHOD_SOURCE_REGISTRY.csv
```

The registry records the source, locator, verification status, and the boundary of what that source supports. ScholarOps-specific workflow rules remain distinguishable from the external methods they build on.

## Validation

**v1.0.0** passed:

- native Codex end-to-end behavioral validation;
- source/runtime consistency checks;
- generated-runtime drift checks;
- bilingual human-facing checks;
- public privacy and source-body scans.

Native validation was performed with **Codex CLI 0.155.1** using synthetic research fixtures.

## Issues

Use [GitHub Issues](https://github.com/white-ink-cell/scholarops-research/issues) for bugs, documentation problems, and feature requests.

## Citation

GitHub uses [`CITATION.cff`](CITATION.cff) to generate standard citation metadata for ScholarOps.

## License

[Apache License 2.0](LICENSE)
