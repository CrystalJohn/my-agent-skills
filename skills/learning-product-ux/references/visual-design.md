# Visual design and responsive systems

Read for UI creation, redesign, visual polish or developer handoff. U1–U5 in [ui-sources.md](ui-sources.md) support typography, reuse and adaptable layout; additional decision rules below are authored heuristics.

## Direction before styling

Extract the desired character from brand, audience, content and product role. Describe it operationally: "editorial, restrained, text-led" means a clear type hierarchy, selective imagery and few emphasis colors; "playful journal" might use marginal decoration and tactile surfaces while keeping controls conventional.

If direction is genuinely open, compare two materially different directions on the same representative content. Choose by fit, readability, implementation cost and user preference. Do not force multiple moodboards for a small change. References are not a license to reproduce distinctive artwork, branding or full layouts.

Define:
- Intended emphasis and reading order.
- Typography roles, density, spacing rhythm and layout structure.
- Palette roles and component shape language.
- Imagery/icon strategy and motion purpose.
- One distinguishing design idea that serves the task, if useful.

Do not label styles inherently good or bad. Gradients, cards, rounded corners and asymmetry can work when coherent and purposeful.

## Compose with real content

Arrange related content together; give unrelated groups visible separation. Use size, weight, placement and contrast deliberately rather than making every block equally prominent. Maintain alignment anchors and consistent component anatomy. Test the initial viewport and the whole scroll experience; the hero alone is not the product.

Use containers and spacing tokens appropriate to density and content. A spacing scale is a consistency tool, not a rule to round every optical adjustment. Fixed heights need a content/overflow reason. Do not crop critical instructions or user input to preserve symmetry.

For data-heavy work, optimize comparison and scan paths before adding generous empty space. For reading, contain line length without squeezing the text. Exact line lengths and spacing are starting hypotheses to inspect in the actual font/language.

## Typography

Define roles such as display, page heading, section heading, body, label, helper and numeric data. Record family, weight, size, line height and tracking; distinguish semantic heading structure from visual size. Reuse existing roles first.

Check font availability, license, language coverage (including Vietnamese diacritics if needed), loading/fallback behavior and performance. A single family may supply enough hierarchy. Decorative fonts belong where they remain legible.

Body line height around 1.5 is a starting point from U1, not a universal accessibility requirement. Headlines and dense labels need their own treatment. Stress-test wrapping, long names, multi-line buttons and text enlargement. Avoid shrinking text to force content into a card. Use numeric alignment when users compare numbers.

## Color and surfaces

Use role-based tokens: canvas, surface, text-primary, text-secondary, border, action, focus, positive, warning and critical. Assign roles before selecting exact colors. Brand and status colors may overlap only when meaning remains clear. Check text/background pairs in actual states; a palette alone cannot establish contrast.

For web AA checks, U8 specifies 4.5:1 for ordinary text and 3:1 for large text, with exceptions; large text means the criterion's defined size/weight, not "a heading." U13 covers required non-text visual information at 3:1 against adjacent colors, with its exceptions. Consult those sources for borderline cases. Disabled elements can be exempt from a criterion without becoming good usability examples.

Use labels, icons or shape as well as color for meaning. Gradients, image backgrounds and transparency need checks at the actual text location and worst relevant background. Dark mode needs semantic remapping and state inspection, not simple inversion.

## Tokens and reusable components

Map existing tokens/components before adding new ones. Separate primitives (palette/space values), semantic roles, and component overrides only where that complexity helps. Keep Figma variables and code names aligned when both exist (U2/U3).

For each affected component declare anatomy, variants, content limits, behavior and applicable states. Do not generate every combination mechanically. A button may need default, hover, focus-visible, active, disabled and pending; a choice may additionally need selected and graded states. Selected is not submitted; disabled is not loading.

Represent repetition as real components rather than detached copies. Define layout relationships with auto layout/Stacks in design tools and suitable flow/grid/flex rules in code. Map to the project's existing architecture, not a mandatory library. In Figma, annotations can capture nonvisual behavior; screenshots cannot supply those contracts by themselves.

## Responsive behavior

Model one adaptable system (U4/U5). For each region decide what grows, wraps, stacks, scrolls, stays fixed, changes order or collapses. Choose breakpoints when content or interaction breaks; device presets are test samples, not complete coverage.

- Preserve information priority and required actions across widths.
- Keep meaningful DOM/reading/focus order; visual rearrangement must not create a different keyboard journey.
- Replace hover-only affordances with touch/keyboard-accessible equivalents.
- For dense tables, compare controlled horizontal scroll, field prioritization and alternative views; do not remove comparison data silently.
- Sticky actions must not obscure content, errors, the focused control or the onscreen keyboard.
- Test intermediate widths, long content and zoom, not just desktop/phone screenshots.
- Honor genuine two-dimensional tasks such as maps/editors; provide usable navigation and surrounding controls instead of pretending all canvases should stack.

U9 explains web reflow at 320 CSS px for vertical content and the two-dimensional-content exception; native products require their platform guidance too.

## Imagery, icons and motion

Choose imagery that informs recognition, explanation or brand intent. Use originals or appropriately licensed assets; record source and reuse status. Keep icon family, stroke/weight and alignment coherent. Ambiguous or important actions need understandable labels and accessible names.

Give motion a job: reveal hierarchy, preserve orientation or confirm an action. Define trigger, transition, interruptibility and reduced-motion alternative. Avoid blocking task completion behind decorative animation. A static screenshot does not prove timing or reduced-motion support.

## Minimum visual handoff

For the changed scope, deliver concrete token values or existing token references; component/state mapping; responsive rules; representative real content; asset provenance; and implementation notes for nonvisual behavior. Any unverified measurement from a screenshot is an estimate, not an extracted design token.

Review at real size: hierarchy → layout/spacing → typography → color/contrast → component consistency → imagery/motion. Fix issues in this order when earlier decisions explain later symptoms; do not polish shadows around a broken task.

