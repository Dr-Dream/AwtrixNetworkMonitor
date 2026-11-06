# NetworkMonitor

An AWTRIX NG Berry application for **TC002**. It uses `tcp`, which the installed Skill reference documents as TC002-only. Compatibility with the target firmware and hardware execution have not been verified.

Complete source: [NetworkMonitor.ax](NetworkMonitor.ax).

- Separate comma-separated TCP host and HTTP URL lists.
- Public IP retrieval through `http://ifconfig.me`, with IPv4/IPv6 validation.
- HOME, ALERTS, and NODES pages with bounded latency history.
- Sequential asynchronous checks outside the drawing path.

Settings are under **Apps → NetworkMonitor → gear**. To install manually, open the existing NetworkMonitor script on the **Scripts** tab, replace its contents with the complete file, and save. No device installation has been performed. If `ERR:` appears, inspect the message and line number on the Scripts tab.

Behavior is documented in [configuration](docs/configuration.md) and [architecture](docs/architecture.md). The authoritative API reference is `.codex`. The Skill and its reference have not been modified.
