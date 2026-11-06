# NetworkMonitor 0.27 configuration

All settings are declared in the `NetworkMonitor.ax` header using `# @config` and read without repeating defaults in application logic. Saving settings in AWTRIX restarts the app. The code does not overwrite existing device configuration values.

## Targets and checks

- `tcphosts`: an independent comma-separated list of `host:port` entries. The port is mandatory, in the range 1–65535. The last colon separates the port; IPv6 addresses use no square brackets. Support for specific addresses in the device network stack has not been tested.
- `httphosts`: an independent comma-separated list of complete `http://` or `https://` URLs. Success means a final HTTP status of 200–299; GET follows redirects according to firmware rules. Response content is unused and collection is capped at 64 bytes. Latency includes queueing and request processing; it is not ICMP ping.
- Empty and whitespace-only entries are ignored. Invalid entries are skipped with a log message. Empty lists remain empty. Commas within URLs must be encoded as `%2C`.
- `interval`: the delay after a complete scan finishes; default 60 s. Showing the app does not reset this interval. The middle button requests a scan and public IP refresh after the current operation finishes.
- `tcp_timeout`: default 4 s; converted to milliseconds for `tcp.connect`.
- `http_timeout`: default 5 s; passed to the HTTP API in seconds. Network queues and DNS remain subject to separate firmware limits.
- `ipurl`: default `http://ifconfig.me`. Requests send `Accept: text/plain` and accept only a complete IPv4/IPv6 address with optional surrounding whitespace. HTML and invalid responses are rejected. The actual service response from the device has not been tested; previously saved URLs are not changed automatically.
- `wanperiod`: default 300 s after a public IP request completes. On failure, the last valid address remains visible with a `!` marker.

During a recheck, the last completed status remains available and the node label receives `...`. TCP failures update the result regardless of the previous status. There are no retries within a scan.

## Pages

- `mode=auto`: HOME → ALERTS (when failures exist) → NODES (when enabled) → the next app. The app temporarily holds rotation to finish scrolling and releases its hold when hidden. Network checks continue while hidden; pages do not advance.
- `mode=manual`: turn the knob to change pages; entries within a page advance automatically. `manualtime=30` s sets the normal display duration, and `manualhold=20` s sets the hold after the last knob input. This limit can interrupt a long list and can be increased.
- `show_nodes=true`: enables the node page.
- `pagetime=5` s: the minimum duration of one entry or HOME, rather than the whole list.
- Entries advance after both text lines complete scrolling and the minimum duration has elapsed. NODES scrolls the hostname and result together, without a separate result screen. The former `resulttime` setting is removed. Equal-width replacements wait for an additional scroll boundary to avoid counting an inherited partial pass; text that fits does not require a completed scroll run. `scrollwait=60` s bounds the wait per entry, including while the matrix is off. The effective limit is at least `pagetime`. Long text can be interrupted when this limit is reached.
- `scrollspeed=65`: a percentage of the API base speed (100% = 21 pixels/s). `scrollgap=10` pixels; `scrollhold=500` ms.
- History capacity is the available interface width (the panel width when the instance icon is disabled): one result per one-pixel column. A 52-pixel panel retains 52 results per node with the icon disabled, or 36 with the default 14-pixel icon, one-column left margin, and one-column gap. Incomplete history grows from left to right; once full, the oldest result is removed for each new result. The former `historysize` setting is removed because capacity now follows the display geometry. On panels taller than 8 rows, the graph uses every available interface column below the header. An 8-row panel uses a compact view; this does not add TCP support to ESP32.
- `color_*`: configurable status and display colors. NODES uses `color_text` for hostnames, `color_info` for the TCP icon, and `color_http` for the HTTP icon. Latency/result text uses `color_ok`, `color_fail`, or `color_wait` according to the last completed status.

## Instance identifier icon

The optional icon distinguishes multiple installed copies of NetworkMonitor. It is separate from all existing HOME, ALERTS, status, TCP, and HTTP pictograms, which keep their original appearance, colors, and pulse behavior.

Under **Apps → the installed script → gear → Icon**:

- `show_icon=false`: disabled by default for new configurations. With the icon disabled, the interface coordinates, text widths, pictograms, and graph capacity match version 0.23. Previously saved settings are respected; turn this switch off to return to the original layout.
- `icon_kind=home`: select `home` (house), `shield` (VPN), `server`, `wifi`, `database`, or `cloud`. This identifies the script instance; a VPN symbol does not add a VPN check.
- `icon_color=#40B8E0`: color of the instance icon, independent of check status and existing pictogram colors.
- `icon_animate=true`: animate details within the icon. Disable for a static frame.
- `icon_left=1` px: blank margin before the icon (1–4 px); the icon never touches column 0.
- `icon_inset=1` px: vertical inset on each edge (0–2 px). The icon is square: 14×14 on TC002 by default, 16×16 at 0, or 12×12 at 2.
- `icon_step=350` ms: frame duration, configurable from 100 to 2000 ms; each sequence has four frames.

When enabled, the instance icon occupies a vertically centered square on the left: 14×14 on TC002 by default, with one blank pixel row above and below. All original interface elements move right by the left margin, icon width, and one blank column (16 columns on TC002 with the default settings), including lower counters, status pictograms, and the graph. Original fonts and pictograms keep their size. Text scrolls in the remaining width, and history capacity follows that width so the latest samples remain visible. With the icon disabled, the offset is zero. The same instance icon stays visible on every page, including empty and pending views.

The glyph uses built-in vector segments scaled to the configured square size, with one-pixel strokes and no external assets. Scaling moves segment endpoints without thickening the lines. Geometry and four activity-dot positions are prepared once during initialization; drawing uses `now_ms()` and allocates no lists or timers. Local raster previews and coordinate bounds were checked. Version 0.26 compiled and ran as `NetworkCheck` on TC002 firmware 1.2.3. Two 52×16 framebuffer captures confirmed that the configured cloud icon stays in columns 1–14, column 0 is blank, and column 15 separates it from the original interface. Existing configuration values were preserved. Other icon choices and animation timing were not verified on hardware.

New parameters and their defaults are configurable implementation choices; hardware validation is limited to the cloud-icon layout described above. Do not put secrets in URLs or settings: source and logs are accessible through the device interface.


## Version 0.27 icon artwork

The house adds a chimney and separated windows; the shield contains a padlock; the server uses three rack bays; WiFi uses curved waves with a brightness pulse; the database uses a cylinder with curved dividers; the cloud has two distinct lobes and a broad base. Cloud animation moves its contour by one pixel rather than placing an activity dot inside it. Original page/protocol pictograms and the interface geometry are unchanged.

[Pixel preview](icons-preview.png): house, VPN shield, server, WiFi, database, cloud, from left to right. This is a local raster preview, not a device capture. After explicit user approval, version 0.27 was installed as `NetworkCheck` on TC002 firmware 1.2.3. All six icon choices were enabled and captured individually. [Device captures](icons-device-0.27.png) confirm visible contours inside the allocated area, a blank left column, and a blank separator. WiFi animation was revised after the first capture so all waves remain visible while their brightness changes. All original configuration values were restored, including `show_icon=false` and `icon_kind=database`; the final app reports no compile/runtime error. Network behavior was not exhaustively tested.
