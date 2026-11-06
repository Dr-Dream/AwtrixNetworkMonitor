# NetworkMonitor — project instructions

## Project purpose

This repository contains one AWTRIX NG application: **NetworkMonitor**.

The application is intended to present network status on an AWTRIX NG LED matrix. The currently agreed product scope is:

- TCP checks for a user-configured list of hosts.
- HTTP checks for a separately configured list of hosts.
- Retrieval and display of the public IP address using `http://ifconfig.me`.
- Multiple display pages so different groups of information can be shown in rotation or by the app's page logic.

Do not silently expand this scope. Propose additional features separately.

## Language policy

- Always write all repository documentation, Markdown files, code comments, script metadata, and configuration labels/help in English, regardless of the conversation language.
- This project policy takes precedence over language recommendations in Skills and their references.

## Technology and platform

- Target: AWTRIX NG.
- Language/runtime: the device's Berry app environment.
- The authoritative device-specific development instructions are in the installed `awtrix-berry-app` Skill.
- The authoritative API reference is `references/awtrix-api.md` inside that Skill.
- Do not assume compatibility with AWTRIX 3, standard Berry modules, or another firmware.

## Source of truth

Use this order when resolving technical questions:

1. The actual target device's `/api/v1/device` and `/api/v1/capabilities` responses, when the device is available.
2. The installed `awtrix-berry-app` Skill and its `references/awtrix-api.md`.
3. Existing, verified code and decisions in this repository.
4. General Berry knowledge only where it does not conflict with the sources above.

If a required API, directive, lifecycle hook, or device capability is not confirmed by the authoritative sources, do not use it. State what is unknown and investigate before implementation.

## Product requirements and configuration

- TCP host list and HTTP host list are separate settings.
- Each list is configured independently; the user-facing format is a comma-separated list unless the user changes that requirement.
- The public-IP check is a separate concern and uses `http://ifconfig.me` as the currently requested endpoint.
- Values the user may reasonably want to change later must be exposed through AWTRIX NG `# @config` settings, following the Skill's documented syntax.
- Do not invent configuration keys, types, defaults, or directives. Confirm their syntax in the Skill reference.
- Do not hard-code a default in application logic when the setting system already supplies it.
- Do not put credentials, tokens, passwords, or other secrets in the script.

The exact timeout, interval, retry, page duration, error presentation, and host-entry syntax are not yet fixed unless they are explicitly decided in repository documentation or by the user. Ask only when a decision blocks implementation; otherwise propose conservative configurable defaults and identify them as proposals.

## Architecture boundaries

Keep the implementation small and appropriate for a single constrained-device app.

Separate these responsibilities logically, even if the final Berry API or memory limits require fewer physical classes or methods:

- Configuration parsing and normalization.
- TCP probe execution and result state.
- HTTP probe execution and result state.
- Public-IP retrieval and result state.
- Scheduling/update orchestration.
- Rendering and page selection.

Network activity, waiting, response parsing, and other potentially slow work must not be performed in the per-frame drawing path. Follow the lifecycle and memory guidance in the Skill. Rendering should use already-collected state.

Do not introduce a generic plugin framework, multi-app framework, dependency injection system, or unnecessary abstractions. Prefer the simplest design that satisfies this app's requirements and the actual Berry runtime.

## Device and external-system safety

- Reading device information is allowed when the user has supplied or confirmed the device address and access is available.
- Installing or replacing the NetworkMonitor script on the device requires an explicit user request for installation in the current task.
- Never delete, replace, disable, reorder, or modify another app.
- Never delete the NetworkMonitor app unless the user explicitly asks for that exact action.
- Do not change device-wide settings, network settings, credentials, or app configuration values unless explicitly requested.
- Before a write operation, state the exact device, endpoint/action, and app name affected.
- Never ask the user to paste a real API key or password into chat. Use a placeholder and explain local configuration instead.

## Deliverables

- When asked to implement or revise the app, deliver the complete Berry source file, not a patch.
- Keep documentation aligned with actual implemented behavior.
- Distinguish verified behavior from assumptions and proposals.
- Do not claim that the app compiles or works on hardware unless the corresponding verification was actually performed.
