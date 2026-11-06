# What’s new in 0.30

- Added a relative green-to-orange gradient to successful response-history bars.
- Stable response times stay green, even when autoscaling makes the bars tall. Small fluctuations receive a slight tint; substantial increases move toward orange. Lower values become greener again.
- Colors adapt to each host’s retained successful minimum and maximum, without fixed millisecond thresholds. Failed checks remain solid red.
- Added **Graph gradient**, **Full orange increase** (default 100%), and **Slow graph color** settings. Disable the gradient to keep solid success-color bars.
- Updated the device screenshots and animated Hub cover to demonstrate the new history colors.
