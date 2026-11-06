# NetworkMonitor 0.27 architecture

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
