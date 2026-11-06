# Verification and evidence

## Evidence standard

Separate statements into:
- **Documented** — directly supported by the Skill/API reference.
- **Observed** — confirmed from the actual device or a tool response.
- **Implemented** — present in repository source.
- **Proposed** — a design choice not yet confirmed by the user or device.
- **Untested** — not verified.

A plausible explanation is not evidence. Do not report "no errors" merely because no error was noticed.

## API and code review

For every non-obvious AWTRIX API call or directive:
1. Locate it in `references/awtrix-api.md`.
2. Confirm exact spelling, signature, argument order, return behavior, lifecycle constraints, and device availability as applicable.
3. Check that the code uses it consistently with the documented semantics.
4. If the reference does not establish the behavior, mark it unverified and do not present it as fact.

For calculations and layout:
- Show the derivation, not just the formula.
- Check integer division and rounding behavior.
- Check boundary cases such as narrow panels, short panels, empty strings, and values at the limits.
- Distinguish text advance width from visible-ink width.
- Account for baseline and glyph bounds when positioning text.

## Functional checks

When reviewing NetworkMonitor, consider at least:
- Empty TCP host list.
- Empty HTTP host list.
- Mixed lists and whitespace around comma-separated entries.
- One host failing while another succeeds.
- DNS failure and connection timeout, if supported by the runtime.
- HTTP non-success response and malformed/unexpected response.
- Public-IP endpoint unavailable or returning an unexpected body.
- No stale result being presented as a fresh successful check.
- Page transitions while probes are running or have failed.
- Display clipping on the actual panel dimensions.

Do not invent a test harness or runtime API. Use only available tools and documented capabilities.

## Device verification

When a device is available and the user has authorized installation/testing:
- Read the device model, SoC, capabilities, and script heap budget first.
- On install, inspect the response body. HTTP 200 alone does not prove successful compilation; the Skill documents the `error` field and `null` as the success condition.
- Check the app status and runtime error information.
- For visual verification, pin the target app immediately before each framebuffer read, as described in the Skill.
- Use the framebuffer's returned width and height; do not assume a 32x8 display.
- Verify the actual pixels and expected page content.
- Do not claim visual verification if only compilation was checked.

If no device is available, provide the complete source and the Skill's web-UI installation/testing steps in the user's language. Clearly state that hardware execution was not tested.
