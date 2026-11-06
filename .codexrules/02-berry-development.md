# AWTRIX NG and Berry development rules

These rules supplement, and do not replace, the installed `awtrix-berry-app` Skill.

## Documentation-first API use

- Treat the Skill's `references/awtrix-api.md` as the authority for AWTRIX NG APIs, directives, lifecycle, and device-specific behavior.
- Do not use AWTRIX 3 APIs or assume that standard Berry modules are available.
- Do not invent function names, argument order, return values, directives, or feature flags.
- Before using an API, confirm its exact signature and relevant constraints in the reference.
- When explaining or auditing code, cite the reference section and exact line or excerpt when available. Never fabricate line numbers.
- If a capability is TC002-only or otherwise device-specific, verify that the target device supports it.

## Lifecycle and resource constraints

- Follow the lifecycle described by the Skill; do not assume method names or call frequency.
- Keep network requests, waiting, JSON parsing, and other potentially slow operations out of the per-frame drawing method.
- Render from state that has already been collected.
- Be conservative with strings, lists, dictionaries, temporary objects, and repeated allocations.
- Do not apply memory optimization folklore blindly. Tie each optimization to a documented Berry/AWTRIX constraint or measured result.
- Check the device-reported script heap budget when the device is available. Do not confuse it with free internal RAM or PSRAM.

## Configuration

- Expose user-adjustable settings using the exact `# @config` syntax documented by the Skill.
- Read settings through the documented store API.
- Do not duplicate configuration defaults in code.
- Keep TCP hosts and HTTP hosts as separate settings.
- Keep the public-IP endpoint or enable/disable option configurable only if that matches the product decision; do not add unnecessary settings without discussing them.
- Parse comma-separated host lists defensively: account for whitespace and empty entries, and document the accepted host syntax. Do not invent unsupported parsing APIs.

## Network behavior

- Keep TCP and HTTP checks logically distinct; success criteria for one must not be reused for the other without justification.
- Handle timeout, failure, and unavailable response states explicitly, using only documented APIs.
- Avoid blocking the UI or delaying the app lifecycle.
- Do not assume DNS, TLS certificate validation, redirect handling, or arbitrary URL support. Verify the actual firmware behavior in the Skill reference.
- The requested public-IP endpoint is `http://ifconfig.me`. Do not silently substitute a different service.
- Never embed secrets in source code or log sensitive values.

## Rendering and pages

- Use `width()` and `height()` rather than assuming a fixed panel size, unless a verified layout requirement explicitly targets a particular size.
- Remember that text positioning may use a baseline rather than a top-left coordinate; verify font metrics and drawing semantics in the reference.
- Keep page state and display state separate from probe execution.
- Avoid unnecessary redraw-time allocations and expensive work.
- Do not claim that a layout works on every panel size without checking clipping and text fit for the supported dimensions.
