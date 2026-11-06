# AWTRIX Hub media

The refreshed HOME, ALERTS and NODES screenshots and GIFs are actual **52×16 TC002 framebuffer captures of a synthetic demo of the NetworkMonitor 0.31 renderer**. They use fictional hosts (`nas`, `api`, `vpn`, `db`), the documentation-only IP `192.0.2.1`, and synthetic results/history. They are promotional examples, not measured network results. The temporary demo used the revised production rendering methods, with network polling disabled.

Each source pixel occupies a 20×20 cell with a 16×16 LED face and dark gaps. Output is **1040×320**, without smoothing. Unlit cells have a dim neutral face so the pixel grid stays visible. Captured lit-pixel colors and positions are preserved.

## AWTRIX Hub cover

[networkmonitor-cover.gif](networkmonitor-cover.gif) is a looping **4-second, 40-frame, 1040×320** cover. It shows HOME, ALERTS with a position indicator, and a populated relative response-history graph with an indicator, green-to-orange peaks and red failure columns. The scenes are joined with editorial cuts.

![NetworkMonitor Hub cover](networkmonitor-cover.gif)

Stills: [HOME](networkmonitor-cover-home.png), [ALERTS](networkmonitor-cover-alerts.png), [NODES history](networkmonitor-cover-history.png).

## Page screenshots

| Page | Full-width layout | With instance icon |
| --- | --- | --- |
| HOME | [home.png](home.png) | [home-with-icon.png](home-with-icon.png) |
| ALERTS | [alerts.png](alerts.png) | [alerts-with-icon.png](alerts-with-icon.png) |
| NODES / TCP | [nodes-tcp.png](nodes-tcp.png) | [nodes-tcp-with-icon.png](nodes-tcp-with-icon.png) |
| NODES / HTTP | [nodes-http.png](nodes-http.png) | [nodes-http-with-icon.png](nodes-http-with-icon.png) |

ALERTS has three position marks, one per current failure. NODES has four marks, one per configured target. The current item is white; the others are gray. The enabled-by-default indicator occupies the last content row, to the right of the optional instance icon.

## Animated demonstration

[networkmonitor-demo.gif](networkmonitor-demo.gif) is a **23.6-second, 10 fps, 1040×320** animation showing HOME, all three alerts and all four targets, first without the instance icon and then with it. Page timing is controlled by the synthetic demo; text scrolling, icon animation and the position marks are rendered on the device.

## Verification and privacy

Both capture runs compiled and completed without reported runtime errors. The installed monitoring source and every original stored configuration value were restored and compared exactly after recording. No original hostnames, credentials, configuration backups or raw capture logs are included in this directory. The complete revised app has not been deployed as part of this media capture.

`tools/render_release_media.py <capture.json>` converts the local privacy-safe capture into the eight PNG screenshots, cover stills and raw RGB sequences for GIF encoding. The source JSON remains local; the rendering step does not access the device.

## Relative-latency examples

These earlier actual TC002 synthetic-demo captures use the relative mapping accepted for 0.30, before the position row was added:

- [Stable 5 ms](graph-relative-flat-device.png): entirely green despite full-height autoscaling.
- [Small 5–6 ms fluctuations](graph-relative-jitter-device.png): slight tint without an orange peak.
- [Large 5–50 ms changes](graph-relative-spikes-device.png): orange peaks, greener falling values and red failures.

## Indicator boundary checks

Actual TC002 synthetic demos: [four hosts](node-indicator-device.gif), [52 hosts](node-indicator-max-device.gif), [maximum-width still](node-indicator-max-device.png), and [53-target validation error](node-limit-device.png).

At maximum width, the final row contains exactly one white and 51 gray pixels. Production initialization accepted 52 synthetic TCP targets and rejected 53 with `Host limit` / `53 / 52 max`. Network polling was disabled in those test harnesses. Source and configuration were restored and compared exactly afterward.

## Single-item layouts

Actual TC002 synthetic-demo captures with indicators enabled: [one NODES host](single-nodes-device.png), [one ALERTS failure](single-alerts-device.png), and the corresponding [NODES](single-nodes-with-icon-device.png) / [ALERTS](single-alerts-with-icon-device.png) layouts with an instance icon. No position mark is drawn. Framebuffer checks confirmed that NODES uses all eight graph rows through row 15, and ALERTS retains its original second-line baseline with the last row blank. Both runs reported no compile or runtime errors. Installed source and every original configuration value were restored and compared exactly afterward.

## Indicator width with an instance icon

Actual TC002 synthetic-demo captures with default icon geometry (36 content columns):

| Item count | NODES | ALERTS |
| --- | --- | --- |
| 12 | [NODES](indicator-12-nodes-device.png) | [ALERTS](indicator-12-alerts-device.png) |
| 36 | [NODES](indicator-36-nodes-device.png) | [ALERTS](indicator-36-alerts-device.png) |
| 42 | [NODES](indicator-42-nodes-device.png) | [ALERTS](indicator-42-alerts-device.png) |
| 52 | [NODES](indicator-52-nodes-device.png) | [ALERTS](indicator-52-alerts-device.png) |

[Animated comparison](indicator-ranges-device.gif) shows each pair in ascending count order. All demonstration targets fail so ALERTS and NODES have the same item count. At 12 items, marks remain to the right of the icon. At 42 they span the full bottom row beneath it. At 52, exactly one white and 51 gray pixels were confirmed on both pages. No compile/runtime errors were reported. The original source and every stored configuration value were restored and compared exactly afterward. These demos use synthetic state and disable network polling.

The exact 36-item boundary was also captured on TC002: both pages had 16 blank bottom-row columns beneath the icon and exactly one white/35 gray pixels to its right. No compile/runtime errors were reported; original source and configuration were restored and compared exactly.
