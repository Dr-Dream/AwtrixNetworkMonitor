# NetworkMonitor 0.32 configuration reference

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

## Graph gradient

`graph_gradient=true` enables a vertical palette from `color_ok` to `color_graph_top` (default `#FF9830`). Each node uses its own retained successful history; failed samples are excluded from the minimum and maximum. TCP/HTTP success still depends on connection/status, not on color.

The baseline is the successful minimum. The color span is the larger of the observed maximum minus that baseline and `baseline * graph_full_pct / 100`. `graph_full_pct` defaults to 100 and accepts 10–1000%. Increasing it softens the color change. A one-millisecond floor protects zero-resolution measurements and division; it is not a network-health threshold.

At default settings, stable 5 ms samples remain green, 5–6 ms variation receives only a slight tint, and a 5–50 ms range reaches orange at the peak. Falling values become greener. The reference adapts when old samples leave the retained history; colors compare values within that window rather than indicating an absolute latency limit.

Bar heights remain autoscaled to the retained maximum. Failed checks remain solid `color_fail` columns. Disabling the gradient restores solid `color_ok` bars. The palette is cached during initialization; drawing allocates no collections.

The relative mapping was compiled and executed in a temporary TC002 demo with synthetic histories. Framebuffer checks confirmed green-only stable samples, a slight tint for small fluctuations, and orange peaks with red failures for large changes. The original source and all stored configuration values were restored and compared exactly. This verifies the demo rendering, not deployment of the complete revised monitoring app.

## NODES and ALERTS position indicators

`node_indicator` (labelled **Show page indicators**) defaults to true. On displays taller than eight rows, NODES reserves the last row of the available content area for host-position marks and uses the remaining rows for history. The instance icon retains its own area. The active mark uses `color_node_active` (white by default); others use `color_node_idle` (gray by default). With no targets, no marks are drawn. With a single target, no marks are drawn and the graph keeps its full height.

Each host receives an evenly partitioned slot. Slots at least three pixels wide leave a one-pixel gap when there is more than one host; narrower slots are contiguous. When the page item count exceeds the width beside the icon, marks extend across the full bottom row beneath it, without resizing or moving the icon. This decision uses the total host count for NODES and the failure count for ALERTS. At the display-width item count, each slot is exactly one pixel. The combined valid TCP + HTTP target count is validated during initialization against the display width, even if the indicator is disabled. A larger list is rejected in full: the panel shows `Host limit` and `<count> / <limit> max`, the reason is logged, and network checks remain paused. No configured targets are silently dropped. The limit is 52 on TC002, regardless of the icon settings. History capacity still follows the narrower content width; host capacity does not. Disabling the indicator restores the previous graph height. Eight-row displays retain their existing one-line NODES view.

ALERTS uses the same enabled-by-default toggle and indicator colors. Its mark count is the current failure count and its active position follows the alert index, not the complete host list. The second text baseline moves from row 14 to row 13 while the indicator is visible (at least two failures) so the last pixel row stays clear for the marks. With no failures, ALERTS falls back to HOME and shows no marks. With a single failure, no mark is drawn and the original text baseline is retained. Disabling **Show page indicators** restores the original ALERTS text baseline and full NODES graph height.
