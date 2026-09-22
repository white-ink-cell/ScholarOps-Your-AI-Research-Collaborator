# 04 — Access and Resource Interface


## ACCESS-01 — Access states are not interchangeable
For every candidate source, distinguish at least:

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

Platform existence is not evidence of user entitlement, usable history, scalable extraction, or primary-sample eligibility.

## ACCESS-02 — Resolve existing assets before reacquiring data
If a task depends on an asset that may already exist, first resolve the currently attached artifacts and registered project assets. Reuse a verified unchanged asset when its identity is confirmed and no re-verification trigger applies. Reacquire or ask the user only when the required asset is genuinely absent, inaccessible, or invalid for the present task.

## ACCESS-03 — WRDS and institutionally licensed databases
Treat a WRDS login, or any institutional platform login, only as evidence that the platform can be entered. Verify the specific database, table, fields, years, export mode, and current subscription needed by the design.

## ACCESS-04 — Usage-based market-data services
Existing credits, prior purchases, or historical access do not imply current access to every dataset, year, schema, or delivery mode. Verify entitlement and expected cost for the actual requested sample.

## ACCESS-05 — LSEG and similar research terminals/APIs
Do not infer API, Datastream, tick-history, or premium add-on access from the existence of a standard user interface. A UI path that has not been tested for historical depth and export scale cannot silently support a large-sample design.

## ACCESS-06 — Bloomberg and other shared-terminal resources
Do not infer scalable research access from the statement that an institution "has Bloomberg" or an equivalent terminal. Determine whether the task is manual lookup, limited export, API/bulk, or otherwise unsuitable for the proposed primary sample.

## ACCESS-07 — Verified entitlement outranks generic platform marketing
Current user/institution entitlement evidence and actual probes outrank generic vendor pages. Vendor documentation that says an API or dataset exists cannot grant an entitlement the user does not have.

## ACCESS-08 — Do not repeatedly spend search time on known-unavailable paths
If a path is already verified as not entitled, excluded, or outside the current access universe, do not repeatedly treat it as the next acquisition route unless the user reports a relevant change or a new lawful access path appears.

## ACCESS-09 — Maintain an access registry when access is research-relevant
Record, as needed:

```text
provider / source / entitlement / UI / API / bulk / historical depth /
cost state / usability / tested_at / verification / candidate identifiers
```

Do not reduce a consequential access decision to a single yes/no flag when history, scale, matching, or cost determines executability.

## ACCESS-10 — Assistant-first execution
When the host can lawfully access the files and execute the required processing, the agent should perform the task rather than offloading runnable work to the user. Ask the user only for the minimum step that is actually blocked by credentials, institutional login, paid access, local-only resources, or host limitations.

## ACCESS-11 — Discover lawful alternatives before declaring access failure
Before `BLOCKED_ACCESS`, perform a proportionate search for lawful public bulk/API sources, public repositories, author replication packages, actually subscribed institutional resources, existing credits, legal educational/free access, and construct-preserving alternatives.

The fact that the ideal published dataset is private does not by itself make the research question infeasible.

## ACCESS-12 — A fallback must preserve the construct or reduce the claim
Compare any substitute on:

```text
unit / target / timing / construct / coverage
```

If the substitute changes the research object, timing, construct, or target population, record the substitution and narrow the claim. Do not present a lower-quality source as construct-equivalent without validation.

## ACCESS-13 — Record the strength of access evidence
Use an evidence ladder such as:

```text
DOC_ONLY / SCHEMA_VERIFIED / SAMPLE_PROBED / BULK_TESTED / HISTORICAL_DEPTH_VERIFIED
```

Documentation alone normally leaves primary-sample executability conditional when scale or history is material.

## ACCESS-14 — Scalability is part of access feasibility
If the design requires sustained security-by-security or event-by-event manual extraction, record `MANUAL_EXTRACTION_BURDEN`. The ability to view a record is not the same as scalable, reproducible access.

## ACCESS-15 — Do not bias research selection toward familiar data pipelines
Existing pipelines for one data modality must not automatically make candidates using that modality look more executable. Apply the same lawful access search and construct-preservation test to alternative data sources.

## ACCESS-16 — Separate cost state from usability state
Where relevant, record cost using categories such as:

```text
ZERO_COST_CONFIRMED / INCLUDED_IN_SUBSCRIPTION / COVERED_BY_FREE_CREDIT /
FREE_WITH_LIMITS / UNKNOWN / NEW_PAID_ACCESS_REQUIRED
```

and usability using categories such as:

```text
SCALABLE / LIMITED_UI_EXPORT / MANUAL_LOOKUP_ONLY / REFERENCE_ONLY /
EXCLUDED_BY_DEFAULT / UNVERIFIED / NOT_ENTITLED
```
