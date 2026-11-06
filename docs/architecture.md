# NetworkMonitor 0.23 architecture

One Berry class in `NetworkMonitor.ax`. The required `tcp` module is documented as TC002-only. The app adds no shared modules or background apps and does not change device settings.

- `init` reads configuration, parses independent TCP/HTTP CSV lists, and initializes state, including content for the first frame.
- `loop` starts one HTTP request or TCP connection at a time. A single `busy` flag prevents overlapping operations. Public IP refresh takes priority; node scans follow their schedule. The scan interval starts when a complete scan finishes.
- HTTP and TCP callbacks update node status, failure reason, latency, and bounded history. TCP uses a separate pending-check flag, so a previous success cannot suppress a later failure. Successful TCP connections are closed immediately.
- The public IP callback validates IPv4/IPv6 syntax and ranges. The last valid address remains in memory separately from the latest request status.
- `reset_counts` and `prepare_home` prepare labels and colored text fragments outside drawing. Unchanged node labels and counters are reused.
- `draw` and its helpers render prepared state. `scroll_line` records scroll completion counts without fetching data, parsing responses, or assembling labels. Text duration is not estimated from character count or speed.
- Pages and entries advance only while the app is visible. When the last failure disappears, ALERTS immediately advances to the next page. Each entry has a minimum reading time and a finite scroll wait limit. NODES keeps the hostname and result in one scrolling line, without a separate result screen. Equal-width text changes wait past the inherited partial pass and then for a complete pass.

History is bounded to `width()` results per node and trimmed in place. Each result occupies one pixel column, so a full history fills the graph width without stretching or overlapping bars. HTTP bodies are capped at 64 bytes and are not retained. Results are collected again after restart; AWTRIX persists configuration.

Local checks covered source block/delimiter balance, internal method references, configuration declarations/reads, and the absence of networking or string/list construction in the drawing call tree. These checks are not Berry compilation. Compilation, network scenarios, rotation holding, and the visual layout on an actual TC002 remain unverified.
