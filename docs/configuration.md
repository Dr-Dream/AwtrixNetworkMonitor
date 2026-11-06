# NetworkMonitor 0.23 configuration

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
- History capacity is the panel width returned by `width()`: one result per one-pixel column. A 52-pixel panel retains 52 results per node. Incomplete history grows from left to right; once full, the oldest result is removed for each new result. The former `historysize` setting is removed because capacity now follows the display geometry. On panels taller than 8 rows, the graph uses every column below the header. An 8-row panel uses a compact view; this does not add TCP support to ESP32.
- `color_*`: configurable status and display colors. NODES uses `color_text` for hostnames, `color_info` for the TCP icon, and `color_http` for the HTTP icon. Latency/result text uses `color_ok`, `color_fail`, or `color_wait` according to the last completed status.

New parameters and their defaults are configurable implementation choices; hardware validation has not been performed. Do not put secrets in URLs or settings: source and logs are accessible through the device interface.
