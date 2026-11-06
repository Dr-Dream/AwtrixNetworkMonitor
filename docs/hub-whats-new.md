# What’s new in 0.33

- Fixed a repeated rotation handoff that could skip the application following NetworkMonitor, especially with NODES disabled and no active failures. Completion now requests a transition only once and ignores late timer callbacks after leaving the screen.

## What’s new in 0.32

- Added bottom-row position indicators to **NODES and ALERTS**, enabled by default. The current item is white; other items are gray. NODES shows all hosts, while ALERTS shows only active failures. With just one item on a page, its indicator is hidden and the original graph height or text position is retained.
- Marks are distributed evenly across the available width, becoming one pixel per item at maximum capacity. Colors are configurable; disable **Show page indicators** to restore the previous layout.
- Added validation of the combined TCP + HTTP host count against the display width: up to 52 hosts on TC002 with or without an instance icon. When marks no longer fit beside the icon, the indicator extends beneath it across the full bottom row without resizing it. An oversized list displays **Host limit** and pauses checks instead of silently omitting hosts.
- Added relative green-to-orange response-history gradients: stable values remain green, small fluctuations receive a slight tint, and large increases turn orange. Failed checks remain red. Adjust **Full orange increase** and **Slow graph color**, or disable **Graph gradient** for solid bars.
- Refreshed the screenshots, animated demonstration and Hub cover with synthetic, privacy-safe device captures.
