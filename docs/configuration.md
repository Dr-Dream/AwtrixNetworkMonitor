# NetworkMonitor 0.27 configuration reference

The complete user-facing configuration tables, defaults, ranges, input examples, and screen diagrams are maintained in the [README](../README.md#configuration). That document is the English description prepared for the AWTRIX Hub listing.

## Storage and updates

All settings are declared in the leading `# @config` header of `NetworkMonitor.ax` and read with `store.get(key)`. Application logic does not repeat defaults or overwrite saved settings. The firmware restores configuration before initialization. Saving settings restarts the script; status, response history, and the last public IP are collected again.

Separate installed copies have independent settings. Their instance icons are identifiers; icon selection does not change the checks performed.

## Input parsing

- TCP and HTTP lists are parsed independently as comma-separated entries. Surrounding whitespace and empty entries are ignored. Invalid entries are skipped and logged.
- TCP entries require a port from 1 to 65535. The last colon separates host and port. The parser accepts unbracketed IPv6 host syntax; compatibility with particular IPv6 addresses in the device network stack has not been tested.
- HTTP entries require complete `http://` or `https://` URLs. Encode literal commas as `%2C`. Final status 200–299 is success; response bodies are not validated and collection is capped at 64 bytes.
- Public IP retrieval requests plain text and validates IPv4/IPv6 syntax. HTML and malformed responses are rejected. The last valid address is retained in memory when a refresh fails.

## Timing and layout

The scan interval begins after a complete node scan. The public IP interval begins after its request completes. There are no automatic retries within a scan.

An entry advances after its minimum duration and scroll completion, or when the scroll wait limit expires. Text that fits is immediately considered complete. Equal-width replacements wait for an additional scroll boundary to avoid counting an inherited partial pass. Pages advance only while the app is visible. Network checks continue while hidden.

On the TC002's 52×16 panel, the optional identifier has side length `16 - 2 * icon_inset`. The interface offset is `icon_left + side + 1` when enabled, or zero when disabled. Original page/protocol pictograms retain their size and colors. History capacity equals the remaining interface width, with one result per column. The default icon layout leaves 36 columns; disabling it restores all 52 columns.

## Verification

Version 0.27 compiled and ran as `NetworkCheck` on TC002 firmware 1.2.3. All six icon choices were captured from the 52×16 framebuffer. Left margins and interface separators were blank; no compile/runtime error was reported. WiFi was adjusted to keep all arcs visible throughout its brightness pulse. Original configuration values were restored after the test. Network behavior and compatibility with other firmware versions were not exhaustively tested.

[Device icon captures](icons-device-0.27.png), left to right: house, VPN shield, server, WiFi, database, cloud.
