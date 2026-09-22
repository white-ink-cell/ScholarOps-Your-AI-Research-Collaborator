# 08 — Host Memory, Recovery, Evidence and Language


## GOV-EVID01 — Evidence hierarchy
When sources conflict, use the strongest direct evidence available. A project-state note or conversation summary cannot override a frozen artifact, verified hash/content identity, executed code/log, or other stronger direct evidence merely because the note says the task is complete.

A practical ordering is:
1. frozen canonical artifacts and direct audit results;
2. executed code/logs and verified data/output artifacts;
3. contemporaneous reports or conversation records;
4. retrospective summaries;
5. proposals/plans;
6. model memory.

The hierarchy is about evidentiary strength, not about file names.

## GOV-STATE01 — Derive the next state mechanically
Derive the current research stage and allowed next step from the required artifacts and gates, not from a README or chat statement that declares `COMPLETE`.

For long-running projects, maintain only the state fields needed by the active workflow. Git is optional. Persistent state may be stored under a project-local `.scholarops/` directory or an equivalent host-specific location, but the directory is created only when persistence is useful and the user permits it.

## GOV-RES01 — Resolve prior assets before requesting them again
When a task depends on a previously created/uploaded/acquired asset that is not attached to the current message, search the current workspace and registered project assets first. Confirm identity/version before reuse. Reuse prior verification when the asset is unchanged and no re-verification trigger applies. Ask the user only for the asset that is genuinely unavailable.

Do not confuse "the model does not remember it" with "the asset does not exist."

## GOV-CONV01 — Evidence reconstruction and handoff
`RE` means: recover the latest canonical project state, validate it against registered artifacts, and consult archived conversation evidence only when the canonical state is incomplete, inconsistent, or the user asks for historical reconstruction.

Recovery order:

```text
host/project instructions
→ current structured state
→ decisions and artifact registry
→ open issues and relevant structured memory
→ current project artifacts
→ archived sessions/transcripts only when needed
```

Do not read result-sensitive archive content merely because recovery was requested. Respect the current Seen Data/blinding boundary.

A handoff summary is not the same thing as a verbatim transcript. Call a file a transcript only when the underlying conversation record was actually available/exported. Never reconstruct missing historical turns from model memory and label them complete.

When `RE` is the user's only request, recover and report state, missing required assets, and blockers, then stop rather than silently advancing the next research gate.

## GOV-TRANSCRIPT01 — Transcript completeness audit
For a real conversation/session archive, record enough provenance to distinguish an intact source from a partial handoff, for example:

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

A hash proves fixity, not completeness. Truncation markers, abrupt endings, unexplained message/time gaps, or references to missing later decisions require a `PARTIAL` or `UNKNOWN` review.

## GOV-SEEN02 — Upstream factual correction is legal; outcome-driven redesign is not
After unblinding, a design may still correct an independently demonstrated upstream factual error. Classify the trigger:

```text
REVISION_TRIGGER =
UPSTREAM_SOURCE / DESIGN_PRESPECIFIED / OUTCOME_DRIVEN / UNDETERMINED / NOT_APPLICABLE
```

An `UPSTREAM_SOURCE` correction is allowed only when the trigger is the upstream source itself rather than the observed result, the correction rule applies consistently to all relevant units, and the correction plus evidence is recorded in the repair ledger. It does not restore blindness or reset Seen Data.

`OUTCOME_DRIVEN` redesign is not allowed as confirmatory repair. If the trigger cannot be determined, treat it conservatively as outcome-driven until resolved.

The methodological source for the blindness principle is registered under `EMP-BLIND01`; the rule `EMP-BLIND01A` is the ScholarOps implementation layer. The source locator points to `EMP-BLIND01`; this is a provenance correction only and does not change the substantive rule.

## GOV-ACT01 — Irreversible actions remain irreversible
Distinguish warnings, recoverable runtime failures, and irreversible external actions. Seeing the main effect, submitting an external task, incurring a charge, sending a message, or publishing a file does not become undone because a later error occurs.

If a result was seen, a later implementation repair may be legal under the repair rules, but the project remains unblinded for the scope that was seen.

## GOV-AUDIT01 — Current-workflow audit (`AU`)
`AU` audits the current research workflow from the available evidence, identifies the earliest material gap or inconsistency, distinguishes presentation issues from research-state defects, and stops after the audit when no separate task is requested.

Conversation order can show that a request or promise was made; artifact/log/hash evidence is needed to show that the work actually occurred.

## GOV-LANG01 — User-facing language
Use the user's current language for explanations and judgments unless the user explicitly requests another language. Preserve canonical names, paper titles, author names, venues, DOIs, search queries when needed, code, field names, rule IDs, controlled vocabulary, and machine schemas in their normative/original form.

The canonical machine/runtime layer remains English-only.
