# NetworkMonitor 0.32 architecture

One Berry class in `NetworkMonitor.ax`. The required `tcp` module is documented as TC002-only. The app adds no shared modules or background apps and does not change device settings.

- `init` reads configuration, parses independent TCP/HTTP CSV lists, and initializes state, including content for the first frame.
- `loop` starts one HTTP request or TCP connection at a time. A single `busy` flag prevents overlapping operations. Public IP refresh takes priority; node scans follow their schedule. The scan interval starts when a complete scan finishes.
- HTTP and TCP callbacks update node status, failure reason, latency, and bounded history. TCP uses a separate pending-check flag, so a previous success cannot suppress a later failure. Successful TCP connections are closed immediately.
- The public IP callback validates IPv4/IPv6 syntax and ranges. The last valid address remains in memory separately from the latest request status.
- `reset_counts` and `prepare_home` prepare labels and colored text fragments outside drawing. Unchanged node labels and counters are reused.
- `init` also derives the optional instance-icon area: a left margin, a vertically centered square (display height minus twice `icon_inset`), and one blank column. All original UI drawing uses this horizontal offset and the remaining content width; a disabled icon gives offset zero and the version 0.23 layout. Page, status, and protocol pictograms remain intact. Only the chosen icon's line segments and four activity-dot positions are retained.
- `draw` paints the instance icon on every page, using an elapsed-time phase and single-pixel line segments; no icon asset downloads are needed.
- `draw` and its helpers render prepared state. `scroll_line` records scroll completion counts without fetching data, parsing responses, or assembling labels. Text duration is not estimated from character count or speed.
- Pages and entries advance only while the app is visible. When the last failure disappears, ALERTS immediately advances to the next page. Each entry has a minimum reading time and a finite scroll wait limit. NODES keeps the hostname and result in one scrolling line, without a separate result screen. Equal-width text changes wait past the inherited partial pass and then for a complete pass.

History is bounded to the available content width in results per node (`width()` when the instance icon is disabled) and trimmed in place. Each result occupies one pixel column, so a full history fills the graph width without stretching or overlapping bars. HTTP bodies are capped at 64 bytes and are not retained. Results are collected again after restart; AWTRIX persists configuration.

Local checks covered source block/delimiter balance, internal method references, configuration declarations/reads, and the absence of networking or string/list construction in the drawing call tree. These checks are not Berry compilation. Version 0.26 compiled and ran on TC002 firmware 1.2.3 with no reported script error. Device framebuffer captures verified the cloud icon's single-pixel contour, blank left margin, and separator from the original UI. Existing saved settings were preserved. Other icon choices, animation timing, network scenarios, and rotation holding have not been fully verified.


## Version 0.27 icon artwork

The house adds a chimney and separated windows; the shield contains a padlock; the server uses three rack bays; WiFi uses curved waves with a brightness pulse; the database uses a cylinder with curved dividers; the cloud has two distinct lobes and a broad base. Cloud animation moves its contour by one pixel rather than placing an activity dot inside it. Original page/protocol pictograms and the interface geometry are unchanged.

[Pixel preview](icons-preview.png): house, VPN shield, server, WiFi, database, cloud, from left to right. This is a local raster preview, not a device capture. After explicit user approval, version 0.27 was installed as `NetworkCheck` on TC002 firmware 1.2.3. All six icon choices were enabled and captured individually. [Device captures](icons-device-0.27.png) confirm visible contours inside the allocated area, a blank left column, and a blank separator. WiFi animation was revised after the first capture so all waves remain visible while their brightness changes. All original configuration values were restored, including `show_icon=false` and `icon_kind=database`; the final app reports no compile/runtime error. Network behavior was not exhaustively tested.

## Successful-history gradient

Initialization caches a small RGB palette from `color_ok` to `color_graph_top` and reads `graph_full_pct`. Drawing scans the retained history for the successful minimum and maximum, ignoring failures. Each occupied row maps to a latency level under the current height autoscale. Its palette index follows growth above the minimum, divided by the larger of the observed range and the configured percentage of the minimum. A one-millisecond floor handles zero values and division.

Stable values remain green; small relative changes stay near green, while large increases reach orange. Decreasing values return toward green. Colors adapt as samples leave the history window. Failed samples retain solid `color_fail` columns; disabling `graph_gradient` uses solid successful bars.

The palette is bounded by the graph height and drawing allocates no per-frame collections. The graph method was exercised in a temporary TC002 demo with constant 5 ms, 5–6 ms fluctuations and 5–50 ms spikes. Actual framebuffer captures confirmed the intended colors. Source and configuration were restored and compared exactly afterward; the full revised monitoring app has not been installed as part of this change.

## NODES position marks

The optional host indicator partitions the content width when items fit beside the icon, or the full display width when they do not. It renders after the instance icon to preserve visibility on the bottom row without changing icon geometry. The active slot follows `node_pos` in `node_indexes` order. Larger slots reserve a one-pixel gap. Initialization rejects a combined valid TCP/HTTP list larger than the display width, clears the runtime list, and exposes a visible configuration error. The loop performs no checks until configuration is corrected. Graph bounds exclude the bottom row only when the indicator is enabled and there are at least two hosts. The cached palette supports the full graph height, including the single-host case. Rendering uses integer arithmetic and allocates no collections. The four-host indicator was compiled and captured on TC002 using synthetic data, with exact source/configuration restoration afterward.

On-device boundary checks also accepted 52 synthetic TCP targets and rejected 53 with a visible `Host limit` error. A separate 52-host rendering demo confirmed exactly one white and 51 gray indicator pixels. Network polling was disabled in those test harnesses. These checks do not constitute deployment of the full revised app.

ALERTS and NODES share `draw_position_indicator(count, position)`. ALERTS supplies the failure count and `fail_pos`; NODES supplies the target count and `node_pos`. Both pages suppress marks for zero or one item. The ALERTS second text baseline moves up one pixel only when an indicator is visible (enabled and at least two failures). The existing `node_indicator`, `color_node_active` and `color_node_idle` keys are retained for configuration compatibility; their UI labels now refer to page positions. HOME and eight-row rendering are unchanged.

The combined 0.31 renderer was compiled and captured on TC002 in a temporary synthetic demo, with and without an instance icon. ALERTS displayed three marks for three failures; NODES displayed four for four configured targets. Captures exercised scrolling text and page changes without runtime errors. The original source and all stored configuration values were restored and compared exactly afterward.

Single-item behavior was also verified on TC002 in synthetic demos with indicators enabled, with and without an instance icon. Pixel checks confirmed the eight-row graph through row 15 for one NODES host and the original ALERTS text position with a blank final row for one failure. Both runs completed without compile/runtime errors, and original source/configuration were restored and compared exactly.

Full-width extension beneath the instance icon was verified on TC002 with default icon geometry and 12, 42 and 52 synthetic failing targets on both NODES and ALERTS. Pixel checks confirmed content-only marks for 12, full-width marks for 42, and exactly one white/51 gray pixels for 52. All runs completed without compile/runtime errors; installed source and original configuration values were restored and compared exactly.
