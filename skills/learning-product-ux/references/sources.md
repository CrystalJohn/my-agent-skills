# Evidence ledger

Research inspected 2026-10-30. Mutable URLs are not pinned snapshots. This is a bounded design synthesis, not an exhaustive systematic review. Each entry records what was inspected; no empirical result was reproduced. DIRECT below means the documentation directly establishes its own guidance, not that following it guarantees learning outcomes. SOURCE_CLAIM means reported research/guidance, not verified product effectiveness.

Common provenance: access date 2026-10-30; independent empirical verification not performed. Publication date is unavailable on inspected excerpts unless stated below. Applicability to a particular learner population, curriculum, age, and implementation remains to be validated. The catalog's screen names, contracts, and mechanism choices are authored INFERENCE/proposals, not quotations from these sources.

## E1 — Start with learner needs

- Source: GOV.UK Service Manual, [Learning about users and their needs](https://www.gov.uk/service-manual/user-research/start-by-learning-user-needs), sections Researching users and their needs / Writing user needs.
- Type/quality: DIRECT, Tier 1 for official process guidance.
- Supports: investigate users, tasks and existing evidence; treat non-user opinions as assumptions.
- Does not support: a particular learning-screen architecture or measured improvement for this skill.
- Limitation: government-service context; transfer to learning products is inference.

## E2 — Learning activities

- Source: IES/What Works Clearinghouse, [Organizing Instruction and Study to Improve Student Learning](https://ies.ed.gov/ncee/wwc/PracticeGuide/1), recommendation list and expanded guidance; September 2007.
- Type/quality: SOURCE_CLAIM, Tier 3 research synthesis by an authoritative evidence body; source owns its evidence ratings.
- Supports: spacing and alternating worked examples with problem solving; quiz-based re-exposure; explanatory questions. The guide rates quiz re-exposure strong, spacing moderate, and diagnostic allocation recommendations minimal.
- Does not support: a universal scheduling algorithm, exact UI, calibrated mastery threshold, or identical benefits across ages/domains.
- Limitation: older synthesis; consulted for established instructional principles, not as an up-to-date exhaustive review.

## E3 — Action-oriented feedback

- Source: CAST, [UDL Guidelines, consideration 8.5](https://udlguidelines.cast.org/engagement/effort-persistence/feedback/), explanatory paragraph and action list; live guidance.
- Type/quality: SOURCE_CLAIM, Tier 2 primary framework-owner guidance, not an effect-size trial.
- Supports: specific, timely, constructive feedback about ways to progress and strategies; emphasis on improvement rather than relative performance.
- Does not support: mandatory immediate answer disclosure in every exam, or proof one feedback layout improves learning.
- Limitation: framework guidance must be adapted to assessment policies and learning objectives.

## E4 — Benefits and uncertainty of gamification

- Source: Michael Sailer and Lisa Homner, [The Gamification of Learning: a Meta-analysis](https://link.springer.com/article/10.1007/s10648-019-09498-w), Abstract; online 2019-08-15, journal volume 2020.
- Type/quality: SOURCE_CLAIM, Tier 3 peer-reviewed research synthesis; inspected abstract findings, not reanalysis of studies.
- Supports: reported positive aggregate effects on cognitive, motivational and behavioral outcomes; motivational/behavioral results less stable in higher-rigor subsplits; contextual moderators matter.
- Does not support: guaranteed benefit from any specific badge, leaderboard, map, or product; time-on-task as a proxy for mastery.
- Limitation: heterogeneous interventions; this research did not establish a winning mechanic for the user's product.

## E5 — Contrary evidence and possible harm

- Source: Almeida, Kalinowski, Uchoa and Feijo, [Negative Effects of Gamification in Education Software](https://arxiv.org/abs/2305.08346v1), abstract and bibliographic record; 2023-05-15 repository version, journal reference Information and Software Technology 156 (2023).
- Type/quality: SOURCE_CLAIM, Tier 3 authors' research report; abstract inspected, underlying coding/data not audited.
- Supports: authors map 87 papers reporting undesired effects; points, badges, leaderboards and competition appear among mechanisms implicated in adverse reports.
- Does not support: prevalence among all deployments, causal harm from every implementation, or universal prohibition on competition.
- Limitation: selection focuses on negative reports; useful failure-mode discovery, not a population risk estimate.

## E7 — Task navigation and simplification

- Source: GOV.UK, [Complete multiple tasks](https://design-system.service.gov.uk/patterns/complete-multiple-tasks/), When to use / How it works.
- Type/quality: DIRECT, Tier 1 official design-system guidance.
- Supports: multi-session tasks can use grouped tasks/statuses; simplify before adopting an overview.
- Does not support: learning prerequisite design or proof a world map outperforms a list.
- Limitation: transaction pattern; learning adaptation is inference.

## E8 — Empty states

- Source: IBM Carbon, [Empty states](https://www.carbondesignsystem.com/building-blocks/core/patterns/empty-states), Overview / Anatomy / Designing with empty states; displayed update 2026-08-11.
- Type/quality: DIRECT, Tier 1 official design-system guidance.
- Supports: explain context and useful next actions when data is absent; adapt presentation to available space.
- Does not support: treating network failure, lack of permission, and lack of learning as the same domain state.
- Limitation: source is UI guidance, not a learning or application recovery contract.

## E9 — Target sizes

- Source: W3C, [Understanding SC 2.5.8 Target Size (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html), Success Criterion and exceptions; WCAG 2.2.
- Type/quality: DIRECT, Tier 1 official informative explanation of the criterion.
- Supports: AA criterion specifies 24×24 CSS px with spacing/equivalent/inline/user-agent/essential exceptions; larger targets can be preferable.
- Does not support: “44×44 is always required for WCAG AA,” native-platform equivalence, or whole-product conformance.
- Limitation: this page is informative guidance; scope and full conformance need the applicable standard and product audit.

## E10 — Modal semantics

- Source: W3C APG, [Dialog (Modal) Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/), Keyboard Interaction / Notes / Roles.
- Type/quality: DIRECT, Tier 1 official implementation guidance.
- Supports: contained focus, inert background, Escape behavior, accessible dialog naming, and logical focus return.
- Does not support: choosing a modal for every feedback event or assuming a component library implements the contract correctly.
- Limitation: APG is implementation guidance; verify the actual component and assistive-technology behavior.

## E11 — Structured management data

- Source: IBM Carbon, [Data table](https://www.carbondesignsystem.com/building-blocks/core/components/data-table/guidelines), Overview / When to use / When not to use; displayed update 2026-09-30.
- Type/quality: DIRECT, Tier 1 official component guidance.
- Supports: structured display, search/filter/sort and row/batch actions; not a spreadsheet replacement.
- Does not support: making every learner screen a data table or exposing records without permission boundaries.
- Limitation: select only for the user's actual comparison/management task.

## E12 — Focused question pages

- Source: GOV.UK, [Question pages](https://design-system.service.gov.uk/patterns/question-pages/), page headings / Hint text / Asking complex questions.
- Type/quality: DIRECT, Tier 1 official design-system guidance.
- Supports: task-specific headings and contextual explanation; one-thing-per-page is a referenced transactional design approach.
- Does not support: a universal one-question-per-screen rule for simulations, source comparison, or learning efficacy.
- Limitation: no learner-product comparative experiment performed here.

## I1 — Skill architecture decision

Type: INFERENCE. Premises E1–E5 and E7–E12 support combining learner-task framing, evidence alignment, conditional interaction patterns, and explicit state contracts. Chosen architecture: screen positioning → pattern selection → developer contract → validation. Assumptions: developer needs product guidance, and existing visual tools can handle styling when needed. Unknown: whether this architecture improves real teams' decisions; pilot required.

## Coverage and refresh

Queries covered official task patterns, Carbon states/tables, W3C interaction guidance, IES learning practice, CAST feedback, gamification effects and adverse effects. Search results were used for discovery; the listed pages/sections were opened. No claim here depends on a search snippet. Firecrawl status reported account-info fetch failure; browsing used the available web tool. No paid research service, whole-site crawl or source code copying was needed.

Deferred: exhaustive literature update, native mobile platform HIGs, age-specific studies, child privacy law, monetization, adaptive-learning algorithms, calibrated assessment and the user's actual repository. Do not treat these as established. Re-check mutable standards and platform guidance for implementation-specific work; broaden learner research when age/stakes/domain changes. No assets, component code, or full manuals were copied; the package is authored synthesis with links.
