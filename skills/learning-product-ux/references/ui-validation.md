# UI/UX validation and handoff

Read when reviewing or implementing an interface. Use [validation.md](validation.md) as well for learning outcomes. Source basis: U8–U13 in [ui-sources.md](ui-sources.md); the workflow here is an authored protocol.

## Match verification to the change

For a color-only fix, inspect changed color pairs and relevant states. For a new flow, exercise entry → action → outcome → recovery, with actual data boundaries. Do not run a full research program for a small edit or claim a full audit after a screenshot check.

Keep evidence categories separate:
1. Specification/structure review.
2. Rendered visual inspection.
3. Actual interaction checks, noting prototype/fixture versus live backend.
4. Accessibility checks, stating methods/platforms/assistive technologies.
5. Representative-user observations.
6. Learning/content evidence when applicable.

Use "not checked" when a check could not run. Automated tests cannot establish visual quality or full accessibility conformance. Agent scenario reviews are not participant studies.

## Visual inspection

Inspect representative wide and narrow views plus widths around actual layout changes. Include long text, empty/minimal/dense data, relevant themes and important error/pending states. Check reading order, clipped labels, alignment, density, confusing emphasis, broken imagery, scroll reachability and sticky overlap.

Compare with the agreed direction and real task, not with an arbitrary aesthetic score. If exact Figma matching was requested, verify against the actual frame and available tokens; screenshots alone cannot reveal all design structure.

## Interaction and accessibility

Exercise the changed controls using keyboard and pointer/touch where available. Check accessible names, semantic elements, logical focus/reading order, visible focus, modal focus entry/containment/return, escape behavior, errors and status announcements. Prefer native controls when they meet the need; custom widgets must implement the relevant APG interaction pattern (U10).

Check applicable contrast, target size, text enlargement, reflow and reduced motion. U7's 24×24 CSS px minimum has exceptions; 44×44 can be a design target but is not the universal AA minimum. Consult actual platform guidance for native targets.

Include form repair and preserved input, duplicate activation, interrupted requests and uncertain outcomes when affected. Verify real persistence before saying "saved." Do not interpret an unknown response as success, failure or incorrect learning evidence.

Use accessibility tooling for issues it detects; supplement with manual checks and relevant assistive technology. Report the evaluated scope, not blanket compliance.

## Usability study proposal

Identify the highest-risk task and representative participants/context. Give a neutral task without naming the UI control they should choose. Observe completion, detours, help, misunderstanding and recovery; collect participants' explanation after the task without leading it.

Agree success criteria before results. A small qualitative study finds problems; it does not establish statistical uplift. Separate satisfaction, task success, business conversion and learning. Do not impose a universal participant count or fabricate a baseline.

## Handoff and audit output

For implementation: changed behavior and visual result; files/artifacts; tests actually performed; remaining limits. Keep design and code tokens aligned and expose unresolved assumptions.

For an audit use:
`finding → observation/reproduction → task impact → severity rationale → fix → acceptance check`

For a prototype explain what is interactive, what is simulated, what persists, and what remains a proposed contract. For a design-only deliverable provide sufficient component/state/responsive specifications that a developer does not need to guess the missing behavior.

