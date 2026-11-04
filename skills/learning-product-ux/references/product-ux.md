# Product UX: from needs to screen behavior

Read for discovery, information architecture, general product flows, dashboards, forms, or UX audits. Guidance is authored synthesis; U11/U12 in [ui-sources.md](ui-sources.md) provide process/form premises. Learning-specific decisions additionally use [learning-workflows.md](learning-workflows.md).

## Establish evidence without manufacturing research

Capture: actor; situation; task; current workaround; pain point with source; constraint; desired observable outcome. Existing support reports, analytics definitions, interviews, and product behavior may supply evidence. Without these, label a provisional task model and test it. Do not turn guesses into research-backed personas.

Choose a method by uncertainty:
- Interviews/observation: understand goals and workarounds. Ask about recent actual episodes, not only whether users like an idea.
- Content inventory and task mapping: find duplication, missing destinations, and competing terms.
- Card sorting/tree testing: investigate grouping or findability when IA is uncertain; a small product may not need either.
- Task-based usability sessions: observe whether people can complete a proposed flow.
- Quantitative comparison: use defined populations, denominators, instrumentation and study design; do not infer causal improvement from a visual makeover.

Recruiting or contacting participants needs authorization. Synthetic participants and agent walkthroughs are design reviews, not human research.

## Architecture before decoration

Use user vocabulary for navigation. Distinguish destination navigation from local tabs, filters, and actions. Explain current location, scope, and return path. Keep permissions and actor roles explicit.

For a proposed screen ask: what new task, permission, lifecycle, or navigation requirement makes a separate destination necessary? Feedback, empty results, or selected items may be states within the same screen. Choose progressive disclosure for secondary complexity; do not hide essential cost, requirements, status, or recovery.

For a flow record:
`entry intent → relevant content → action → authoritative result → next action`
Include direct link, refresh, back, cancellation, expired data and interrupted work where relevant. A stepper should represent actual progress, not imply unsaved steps are complete.

## Choose by task

| Situation | Useful direction | Strong alternative / boundary |
|---|---|---|
| Returning user has one pending task | Resume action with useful context | Open directly at task; avoid a dashboard used only as a doorway |
| Compare records and act in batches | Structured table with sort/filter and selection scope | List/cards when comparison is not needed; mobile must preserve required fields |
| Explore a visual catalog | Scannable cards with meaningful metadata | List for dense scanning; images should add recognition value |
| Complete several independent tasks | Task overview with truthful status | Linear flow only when order is necessary |
| Short focused decision | Inline control or compact dialog | Full page for a long/resumable task; nonmodal panel when context must remain interactive |
| Explain an offer on a landing page | Audience/problem, concrete value, credible evidence, clear next step | No mandatory section count, fake testimonials, fabricated metrics or forced signup |
| Configure settings | Clear groups, persistence semantics, recovery | Immediate save versus explicit Save depends on consequence and existing behavior |
| Search/filter results | Query, active filters, result count/scope and clear reset | Empty data, no matches, denied access and failure need distinct messages |

These are contextual proposals, not evidence that a pattern always wins.

## Forms, feedback, and content design

Use persistent labels, clear requirements, sensible input modes, and examples where format is ambiguous. Placeholder text is not the only label. Explain disabled actions where the reason is not evident. Validate at a useful time without interrupting unfinished input.

Tie errors to the affected field and tell the user how to repair them. For long forms, consider a linked summary with logical focus movement (U12 describes the GOV.UK implementation; its exact wording and mandatory summary rule are not universal). Preserve valid input when possible. Distinguish client validation, server rejection, permission loss, and uncertain save.

Name actions by outcome: e.g. "Save changes" when that is what happens. Success text should identify what was saved or submitted and what follows. Do not promise automatic saving, undo, offline support or cross-device continuity without implementation evidence. A toast is insufficient as the only persistent record of an important failure.

Localize content, not just labels: dates, names, currencies, plural forms and reading direction as relevant. Test realistic long Vietnamese/English labels when those locales are supported. Avoid forcing terminology that confuses interface language with language-learning assistance.

## Compact general contract

Use only relevant fields:
- Actor/task and source of need.
- Screen/route or component/state, entry/exit/back/resume.
- Real content hierarchy and primary/supporting actions.
- Pattern, alternative, rationale and known tradeoff.
- State transitions: trigger, visible feedback, allowed actions, persistence/authority.
- Applicable states: loading, ready, empty, no results, invalid, submitting, success, partial failure, unavailable, permission denied, stale or uncertain outcome.
- Visual rules: tokens, responsive changes, component variants and content extremes.
- Semantics, focus, keyboard/touch and announcement expectations.
- Acceptance cases and measurement with denominator; open decisions with owner.

Example: a submitted profile update loses its response. Show uncertainty and preserve edits; reconcile using the real API before another mutation. If reconciliation is unavailable, disclose that limitation instead of inventing a successful save. This is a proposed behavior contract, not a claim about an existing backend.

## Audit prioritization

For each finding: observed evidence/location; affected task/user; impact; reproduction; fix; verification. Separate observed failures from possible risks and taste preferences. Prioritize blocked tasks/data loss, then repeated confusion/access barriers, then consistency and polish. A low-severity cosmetic fix should not become a product rewrite.

