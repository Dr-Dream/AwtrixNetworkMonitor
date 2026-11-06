# AWTRIX Hub media

The page-layout screenshots were captured from the real 52×16 TC002 framebuffer running NetworkMonitor 0.27. The relative-gradient images and updated GIFs use actual framebuffer captures of a synthetic demo of the rendering introduced in 0.30. Screenshots are rendered at **1040×320** with a visible LED matrix: each source pixel occupies a 20×20 cell with a 16×16 LED face and dark gaps. Unlit cells use a dim neutral face so the grid remains visible. Lit-pixel colors and positions are preserved, without smoothing, added labels, or fabricated results. The same presentation is applied to the GIF.

## AWTRIX Hub cover

[networkmonitor-cover.gif](networkmonitor-cover.gif) is the dedicated **4-second**, **40-frame**, **1040×320** cover (about 19 KB). It shows a readable HOME scene followed by a full-width relative response-history graph with green-to-orange peaks and red failure columns. The LED-grid rendering is the same as the screenshots.

![NetworkMonitor Hub cover](networkmonitor-cover.gif)

Still images: [HOME](networkmonitor-cover-home.png) and [history](networkmonitor-cover-history.png).

The HOME cover scene and relative-history scene were recorded on the actual TC002 in separate temporary demos. The cover combines those recordings with an editorial cut. The IP `192.0.2.1`, host `nas`, counters, response times, and populated history are **synthetic promotional data**, not measured network results. The production script and all its configuration values were restored and compared with the pre-capture backups afterward. The older screenshot series below remains a separate set of real observations with temporary demonstration hosts.

## Files

| Page | Full-width layout | With instance icon |
| --- | --- | --- |
| HOME | [home.png](home.png) | [home-with-icon.png](home-with-icon.png) |
| ALERTS | [alerts.png](alerts.png) | [alerts-with-icon.png](alerts-with-icon.png) |
| NODES / TCP | [nodes-tcp.png](nodes-tcp.png) | [nodes-tcp-with-icon.png](nodes-tcp-with-icon.png) |
| NODES / HTTP | [nodes-http.png](nodes-http.png) | [nodes-http-with-icon.png](nodes-http-with-icon.png) |

[networkmonitor-demo.gif](networkmonitor-demo.gif) is a looping **10.8-second**, **10 fps**, **1040×320** animation showing HOME followed by stable, slightly varying and strongly varying relative response histories. These are synthetic demonstrations captured from the device, joined with editorial cuts. It replaces the older page-tour GIF.
![NetworkMonitor demonstration](networkmonitor-demo.gif)

## Capture setup

The user's actual hosts were temporarily replaced with `example.com` and the documentation-only address `192.0.2.1`. Public IP requests were redirected away from the real-IP service. The second series attempted to retrieve the documentation address `203.0.113.42` from a static-response endpoint, but that request failed on the device; HOME therefore honestly shows the unavailable-IP marker (`!`). No actual public IP appears in these images.

TCP/HTTP results and short histories are real observations of the temporary capture setup. Some HTTP requests failed; failure labels and graph bars have not been retouched. A full history takes multiple scans to accumulate, so the graphs are intentionally sparse.

All original configuration values were restored and compared with the pre-capture backup after recording. No original hostnames, credentials, configuration backups, or raw capture logs are included in this directory.

## Relative-latency examples

These actual TC002 framebuffer captures show synthetic histories using the accepted relative mapping at `graph_full_pct=100`:

- [Stable 5 ms](graph-relative-flat-device.png): entirely green despite full-height autoscaling.
- [Small 5–6 ms fluctuations](graph-relative-jitter-device.png): slight tint without an orange peak.
- [Large 5–50 ms changes](graph-relative-spikes-device.png): orange peaks, greener falling values and red failures.

The original installed source and every stored configuration value were restored and compared exactly after capture.

## Rendering the updated media

`tools/render_hub_media.py --home <home-capture.json> --relative <relative-capture.json>` renders the privacy-safe framebuffer recordings into PNGs and raw RGB sequences for GIF encoding. The source JSON recordings remain local; they are not shipped with the repository. No device configuration is changed by this rendering step.
