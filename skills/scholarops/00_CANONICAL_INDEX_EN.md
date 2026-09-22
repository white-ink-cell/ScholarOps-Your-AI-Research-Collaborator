# ScholarOps — Canonical Index / Router

ScholarOps is an evidence-gated research workflow and research-governance Skill for finance, accounting, economics, insurance, and related business research. It is not an autonomous research agent, a general-purpose finance assistant, or a manuscript-polishing system.

## 0. Canonical architecture

ScholarOps separates two sources of truth:

- **machine-governed architecture**: maintained in the repository source spec and distributed here as generated runtime registries;
- **semantic research rules**: maintained once in the English canonical modules and optional profiles bundled with this Skill.

Generated runtime files are not edited by hand. If bundled runtime and the source spec disagree in the repository, the release is invalid until rebuilt and revalidated.

The installable Skill is self-contained. Repository-level build/validation tooling is maintenance infrastructure and is not a runtime dependency.

## 1. Loading discipline

Do not load every module by default.

1. Read `runtime/TASK_ROUTER.csv` and `runtime/GATE_ACTIVATION_POLICY.csv`.
2. Load only the modules required by the current substantive research task.
3. Load `profiles/ai-finance/PROFILE_EN.md` only when the task explicitly studies AI, LLMs, agents, automation, or related systems in a finance/accounting/insurance/business setting.
4. Use `runtime/RULE_LOCATOR_INDEX.csv` to find a specific rule without loading unrelated modules.
5. Use `references/METHOD_SOURCE_REGISTRY.csv` when a method rule requires source/provenance review.

Risk-adaptive gates and artifacts activate only when their underlying risk exists. A small one-off task must not create a full project-governance bureaucracy.

## 2. Host-selection boundary

The host chooses or loads ScholarOps. Once loaded, ScholarOps routes the current research task internally. No extra execute command is required.

ScholarOps is appropriate for substantive research-workflow tasks such as research-question formation, literature/collision screening, contribution adjudication, research design, data/measurement work, pre-result governance, empirical validation, evidence/claim discipline, reproducibility, project recovery, or workflow audit.

Do not auto-expand ScholarOps into ordinary finance explanations, translation, email drafting, general coding help, or unrelated prose editing.

## 3. Command precedence

The only ScholarOps workflow shorthands are:

- `RE` — recover the current project state from canonical structured state and registered artifacts; consult archived conversation evidence only when needed. `RE` alone reports recovered state/blockers and stops.
- `AU` — audit the current research workflow, identify the earliest material gap or inconsistency, and stop unless a separate task was requested.

If a message contains a substantive research task in addition to `RE` or `AU`, perform the shorthand action first and then route the substantive task only if the recovered/audited state permits it.

Precedence:

```text
CANONICAL_VERSION_RESOLUTION
→ RE (when invoked)
→ AU (when invoked)
→ CONCRETE_RESEARCH_TASK
```

## 4. Project state and memory

Persistent ScholarOps project state is optional and initialized only when useful and with user permission. A project-local `.scholarops/` directory is a recommended Codex-first layout, not a universal host requirement.

Structured state is the active workflow memory. Stronger artifact, hash, executed-code/log, and audit evidence outranks a state note that merely claims completion. Raw conversation/session archives are fallback evidence, not default active memory.

Do not open result-sensitive archives merely to recover context. Recovery must respect the current Seen Data / blindness boundary.

Git integration is optional and user-controlled.

## 5. Pre-result governance

Pre-result blindness, Seen Data tracking, freezes, irreversible-action tracking, and outcome-driven redesign controls are core ScholarOps capabilities. Once a result has been seen, a later bug fix does not restore blindness.

`OUTCOME_DECISION_SCREEN` is a resource-allocation screen only. Formal SESOI, equivalence, minimum-effect, or economic-null adjudication belongs to Freeze B / `FORMAL_STUDY`.

## 6. Evidence and collision discipline

A literature collision, stop, or narrowing decision must be supported by evidence strong and direct enough for the adverse proposition being asserted. Weak neighboring evidence is a verification lead, not a formal narrowing verdict.

Professional public terminology uses `STOP / CLOSED / REOPEN` for branch governance. A stop records why the branch stops and what evidence would be required to reopen; it does not automatically mean that an economic effect has been proven absent.

## 7. Access and execution

Access is capability-aware. Platform existence is not user entitlement; entitlement is not historical depth; view access is not scalable research access.

When the host can lawfully read the relevant files and execute the required processing, ScholarOps should perform the work rather than offloading runnable steps to the user. Ask the user only for the minimum action genuinely blocked by credentials, paid/private resources, local-only assets, approval, or host limitations.

## 8. Language

The canonical machine/runtime layer is English-only. User-facing explanations follow the user's current language unless the user specifies another language. Preserve canonical names, titles, author names, venues, DOIs, code, field names, rule IDs, and controlled vocabulary in their normative form.

## 9. Evidence priority

When evidence conflicts, follow `GOV-EVID01` and the project artifacts. Do not infer that a task is complete because a README, summary, or prior chat says so.
