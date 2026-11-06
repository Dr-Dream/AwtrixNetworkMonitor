# Safety and change boundaries

## Repository changes

- Modify only files required for the requested NetworkMonitor task.
- Do not reformat, rename, move, or delete unrelated files.
- Before replacing an existing file, inspect its current contents and preserve unrelated user work.
- Do not overwrite the installed official AWTRIX Skill or its references.
- Do not add secrets, credentials, private URLs, or personal data to source control.

## Device changes

Treat writes to the physical AWTRIX device as external side effects.

- Do not install, replace, enable, disable, delete, or reorder scripts unless the user explicitly authorized that exact operation.
- An instruction to write or review code is not authorization to install it.
- Do not modify other apps or device-wide settings.
- Do not write app configuration values unless explicitly requested.
- Before an authorized write, identify the target device and exact app/script name and action.
- Never use DELETE as a cleanup shortcut.

## Network and credentials

- Use read-only requests for discovery whenever possible.
- Do not expose credentials in command output, logs, documentation, or chat.
- Do not ask the user to paste a real password or API key into chat.
- If authentication is required, explain how the user can supply it locally and securely.
- Do not broaden network scans or probe unrelated hosts. Check only the hosts configured for this app or explicitly named by the user.

## Uncertainty

If a proposed action may affect data, device state, another application, or network availability, stop and ask before proceeding.
