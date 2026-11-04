# Learning Product UX

Help developers answer: why does this screen exist, what learner action belongs here, what changes after it, and how will we know it works? Respond in the user's language. Treat the patterns below as design hypotheses to adapt, not a universal learning theory.

## Establish context before layout

Read the available brief, content, routes, components, progression rules, and API contracts. Reuse existing design systems. Distinguish observed product facts, user requirements, assumptions, and proposals. A screenshot establishes visible UI, not hidden transitions or learning effectiveness.

Identify the learner, age range if relevant, learning objective, taught content, task frequency, input modality, device, session constraints, and stakes. Ask only for missing information that changes the decision; otherwise label assumptions and continue. Do not assume all learners are children or that every product needs XP, streaks, levels, or a world map.

Trace `objective → taught material → activity → evidence → next action`. Use real IDs when supplied. For a new concept, invented IDs must be marked proposed; never claim invented content was taught or reviewed. Diagnostics may deliberately precede teaching, but must be identified as diagnostic and must not silently become punitive progression gates.

## Position the screen

Read [screen-contract.md](screen-contract.md) when creating or reviewing a screen or feature flow. Determine:

- Product role: orient, teach, practice, assess, explain, review, reflect, or manage.
- Entry: learner intent, previous screen, prerequisites, and direct-link behavior.
- Core job: one dominant learner decision; supporting actions may coexist.
- Exit: observable completion, next destination, back, interruption, and resume.
- Learning evidence: what the activity actually demonstrates; distinguish recognition, recall, supported performance, and transfer.

Separate screen, component, and state. Feedback can be a state on a practice screen; it need not become another route. A badge is a component, not a reason to create a screen. Split a screen when task, permissions, lifecycle, or navigation needs justify it; do not split solely to obey a screen count.

## Choose patterns by the job

Read only the relevant entries in [patterns.md](patterns.md). For consequential choices, compare the strongest alternative, explain what condition favors it, and name a failure mode. Separate evidence-backed guidance from product-specific inference; use [sources.md](sources.md) for provenance.

Prefer the smallest useful flow. Do not mechanically instantiate the whole catalog. A map is optional; a plain course list can be right. A simulation may need an integrated workspace; do not force it into single-question cards.

For gamification, specify `learner need → mechanism → intended behavior → learning evidence → possible harm → validation`. Distinguish game-based learning (the activity exercises the skill) from rewards around an activity. Completion, time spent, streaks, and XP alone do not establish mastery. Preserve approved economy rules; propose changes explicitly instead of silently adding penalties or rewards.

## Specify the behavior developers must implement

Create the appropriate portion of the screen contract, not a full template for every small request. Include meaningful content hierarchy, actions, state transitions, data ownership, and acceptance examples.

For scored choice activities, propose selection then explicit confirmation by default; adapt when the interaction intentionally assesses speed or continuous performance. Declare that adaptation and its consequences. Never equate an unsubmitted selection with a committed answer.

Distinguish valid incorrect answers from timeout, duplicate submission, stale content, lost connection, and grading unavailability. Describe uncertain submission and reconciliation before retrying a mutation. Preserve input where feasible. Never invent server persistence, offline support, reward transactions, or idempotency that the implementation lacks; name them as requirements or blockers.

Feedback should explain the relevant distinction, offer a learning reference or strategy, and provide a meaningful next attempt. For summative assessment, feedback timing and answer disclosure depend on the assessment policy; do not reveal protected answers in advance. Do not claim alternative forms of input assess the same construct without checking the objective (for example, captions may alter a listening assessment).

Check keyboard access, visible focus, readable feedback beyond color, reduced motion, responsive layout, and assistive technology semantics. Follow current platform guidance and W3C sources where applicable. Do not equate a checklist or automated scan with accessibility conformance. Do not universalize 44px as the WCAG 2.2 AA minimum; see sources E9.

## Deliver a decision that can be built

For a feature, provide a compact journey/screen map, selected patterns with alternatives, the relevant screen contracts, and prioritized work. For an audit, prioritize observed task failures and missing evidence, with concrete fixes and checks. For implementation requests, carry the contract through authorized code and verification; do not stop at recommendations.

Use [validation.md](validation.md) to distinguish structural review, interaction verification, content review, and learner evidence. Report what was actually run. Mark unreviewed learning content DRAFT; do not claim educator signoff or learning efficacy from model review, local tests, or UI polish.

For visual execution, also read visual-design.md. No particular framework, analytics vendor, Figma account, or other skill is required.
