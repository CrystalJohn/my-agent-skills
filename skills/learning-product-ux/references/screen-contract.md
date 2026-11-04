# Screen contract

Use relevant fields; omit irrelevant ones with a reason when omission could hide a risk. This is a proposed handoff format, not a published standard.

## Compact product map

| Screen/state ID | Learner intent | Role in journey | Objective/content IDs | Main action | Entry/exit | Evidence produced |
|---|---|---|---|---|---|---|

Navigation is a graph, not necessarily a funnel. Include resume, review, and recovery edges. Distinguish optional challenges from required progression. If learner, teacher, and author interfaces coexist, identify actor boundaries rather than merging their dashboards.

## Contract fields

- **Identity:** screen/state ID, route if needed, actor, learning mode, objective, content revision, status (proposed/observed/reviewed).
- **Position:** why it exists, prerequisites, originating screens, deep link, back/exit/resume, completion definition.
- **Information hierarchy:** context and goal; instructional stimulus; response workspace; primary action; support; progress. State what can collapse on small screens without hiding essential evidence.
- **Pattern decision:** selected pattern, strongest alternative, why it fits, when to reconsider.
- **Interactions:** selection, confirmation, hints, keyboard, feedback timing, retry variant, next lesson/review link.
- **State table:** trigger, visible response, allowed actions, saved data, transition. Cover applicable loading, ready, selected, submitting, feedback, complete, empty, locked, invalid, unavailable, and uncertain states. These are not all mandatory routes.
- **Data contract:** existing/proposed API, who grades, saved versus transient state, content version, duplicate handling, permissions, refresh, cross-device behavior if supported. Keep protected answer keys off unauthorized clients when stakes require it.
- **Accessibility/localization:** semantics, focus transitions, non-color cues, motion, text expansion, touch targets, media alternatives. Separate interface language from learning-assistance language and any declared assessment effect.
- **Measurement:** learning outcome, usability measure, engagement measure separately; event meaning and denominator; minimal data needed. Do not collect raw answers, child identifiers, or free text by default for analytics.
- **Acceptance:** observable Given/When/Then cases; mark backend, browser, educator, and learner checks independently.
- **Open decisions:** owner, needed evidence, current assumption, effect if wrong.

## Worked example: introductory vocabulary practice

Illustrative only. Proposed IDs, text, and rules below are not content from a real repository and have not received educator review.

**Screen S-PRACTICE-01:** learner has just studied lesson L-STATION-01. Objective O-SIGN-01 is to recognize the written word `station` in a short sign. This does not establish listening, speaking, or real-world navigation ability. Proposed item Q-SIGN-01 asks which sign identifies a station; the content owner must supply reviewed distractors and explanations.

**Journey:** lesson → practice → feedback state → variant or summary; feedback → specific lesson section → return to preserved attempt. Direct entry without lesson history offers the lesson or clearly labeled diagnostic practice. Whether it gates a challenge is an explicit product decision.

**Layout:** lesson context and question progress; sign stimulus and prompt; labeled answer choices; Confirm button; optional hint/reference. Prefer an inline feedback region so stimulus, answer, and explanation remain available together. Alternative: separate review page when explanations span multiple items; avoid forcing one modal per answer.

| State | Trigger/action | UI and persistence contract |
|---|---|---|
| Ready | Item loaded | Confirm inactive until a valid selection; expose reason; no score event. |
| Selected | Choose/revise option | Visible selection; keyboard operable; no score mutation yet. |
| Submitting | Confirm | Prevent duplicate activation; show progress; retain item/answer/revision. |
| Correct/incorrect | Authoritative result | Explain distinction and next step; outcome tied to attempt ID; count once. |
| Uncertain | Response lost | Say result is not confirmed; reconcile attempt before re-submitting; no invented incorrect result. |
| Content changed | Revision mismatch | Explain refreshed content; no learning penalty; use actual backend recovery behavior. |
| Complete | Reviewed next action | Summarize observed performance; offer next lesson or relevant review; do not announce mastery. |

**Proposed persistence requirement:** attempt ID, item revision, selected option, submission status and accepted outcome. If no backend exists, declare a local prototype and its reload limits; do not silently promise recovery across devices.

**Acceptance examples:** selecting alone never grades; confirming twice does not create two accepted attempts; a connection failure never becomes a wrong answer; keyboard users can choose/confirm/read feedback/continue; refresh after an uncertain submission resolves against saved state if supported, otherwise visibly reports the limitation; the feedback reference opens the correct content section.

**Measurement proposal:** unassisted correctness on a later non-identical item aligned with O-SIGN-01; separate assisted and unassisted attempts. Track successful submission among submitted attempts separately from knowledge correctness among graded attempts. XP is an economy signal, not the denominator for learning.
