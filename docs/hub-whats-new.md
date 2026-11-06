# What’s new in 0.31

- Added bottom-row position indicators to **NODES and ALERTS**, enabled by default. The current item is white; other items are gray. NODES shows all hosts, while ALERTS shows only active failures. With just one item on a page, its indicator is hidden and the original graph height or text position is retained.
- Marks are distributed evenly across the available width, becoming one pixel per item at maximum capacity. Colors are configurable; disable **Show page indicators** to restore the previous layout.
- Added validation of the combined TCP + HTTP host count against the available interface width: 52 without an instance icon, or 36 with default icon geometry on TC002. An oversized list displays **Host limit** and pauses checks instead of silently omitting hosts.
- Added relative green-to-orange response-history gradients: stable values remain green, small fluctuations receive a slight tint, and large increases turn orange. Failed checks remain red. Adjust **Full orange increase** and **Slow graph color**, or disable **Graph gradient** for solid bars.
- Refreshed the screenshots, animated demonstration and Hub cover with synthetic, privacy-safe device captures.
