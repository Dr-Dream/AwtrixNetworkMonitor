# NetworkMonitor

An AWTRIX NG Berry application for **TC002**. It uses `tcp`, which the installed Skill reference documents as TC002-only. Version 0.27 compiled and ran on TC002 firmware 1.2.3. All six instance icons were checked through the 52×16 device framebuffer; their left margin and separator remain blank.

Complete source: [NetworkMonitor.ax](NetworkMonitor.ax).

- Separate comma-separated TCP host and HTTP URL lists.
- Public IP retrieval through `http://ifconfig.me`, with IPv4/IPv6 validation.
- HOME, ALERTS, and NODES pages with bounded latency history.
- Sequential asynchronous checks outside the drawing path.
- Optional vertically centered instance icon, separate from the existing page and protocol pictograms.

Settings are under **Apps → NetworkMonitor → gear**. To install manually, open the existing NetworkMonitor script on the **Scripts** tab, replace its contents with the complete file, and save. Version 0.27 was installed and checked as `NetworkCheck` on the target TC002. Original configuration values were restored after testing. If `ERR:` appears, inspect the message and line number on the Scripts tab.

Behavior is documented in [configuration](docs/configuration.md) and [architecture](docs/architecture.md). The authoritative API reference is `.codex`. The Skill and its reference have not been modified.

Device captures, left to right: house, VPN shield, server, WiFi, database, cloud. These are enlarged framebuffer crops taken during the icon check.

![Version 0.27 device icon captures](docs/icons-device-0.27.png)
