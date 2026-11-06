# Task workflow

## Respect the requested stage

Follow the stage the user explicitly requested.

- If the user asks for analysis, investigate and report; do not edit files.
- If the user asks for a plan, provide a plan; do not implement.
- If the user says "code only after approval", wait for approval.
- If the user asks for implementation directly, implementation is authorized within the stated scope.
- Do not treat a request to inspect, audit, explain, or plan as permission to create or modify files or install anything on the device.

Do not advance to the next stage merely because it seems like the natural next step. Ask or wait when the user reserved that decision.

## Before implementation

1. Inspect the repository and the relevant existing files.
2. Identify the exact app behavior being changed.
3. Activate and follow the `awtrix-berry-app` Skill for AWTRIX NG/Berry work.
4. Read the relevant API reference sections; the Skill may require reading the full reference before writing.
5. Check device model, SoC, panel dimensions, and capabilities when device access is available. Otherwise, state the missing information and avoid assuming TC001/TC002 capabilities.
6. Summarize the intended changes and any material assumptions.
7. Ask no more than three blocking questions at once. Use documented configurable defaults for non-blocking preferences.

## While implementing

- Keep changes limited to NetworkMonitor.
- Prefer a small, direct implementation over speculative abstractions.
- Do not add dependencies, libraries, modules, or firmware assumptions without evidence that the target supports them.
- Do not silently change agreed behavior or configuration semantics.
- If the requested implementation conflicts with the API reference or device capability, stop and explain the conflict rather than improvising.

## After implementation

Report:
- Files created or changed.
- Behavior implemented.
- Configuration options and their defaults.
- Verification performed and its result.
- Remaining limitations or unverified assumptions.

Deliver the complete `.ax` source file when implementing or revising the app, as required by the AWTRIX Skill.
