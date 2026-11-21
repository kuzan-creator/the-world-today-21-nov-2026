[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/kuzan-creator/the-world-today-21-nov-2026/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/kuzan-creator/the-world-today-21-nov-2026/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

# The World Today — 21 November 2026

Sum up 21 November's world news in one image.

A 1024×1024 newspaper front page, drawn with Python/Pillow from
verified reporting (Reuters, AP, CNN, BBC, One Turn, Horizon) on
21 November 2026: 33 stories across 7 regions.

**Top stories on the page**

- Russia fires 400+ drones and 110 missiles at Ukraine; two missiles and a suspected drone land in NATO Poland — PM Tusk calls it a deliberate provocation.
- The AI rout: S&P 500 −3.7% into correction, Nasdaq −5.28%, Nvidia −14%, Anthropic −8.5% a day after its $2tn IPO.
- COP31 in Antalya slips into overtime; the draft deal drops every mention of fossil fuels.
- ICJ rules 9–6 that Myanmar committed genocide against the Rohingya — a historic first for a state.
- M6.7–6.8 earthquake shakes central Peru, felt in Lima.
- Saudi-led coalition intercepts three Houthi ballistic missiles aimed at Riyadh.
- UK–EU sign their biggest post-Brexit agreements; FBI and USDA hacked; Bayer agrees a $7.25bn Roundup settlement.

## How it runs

`main.ts` (Node 22) copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`
(or `/output/entry.png`). No network. Two runs write identical bytes.

`draw.py` is the source that draws `entry.png` — deterministic, no
network, no random values, no timestamps in the image. Re-run it with
`python3 draw.py` to regenerate the same PNG.

## Bounty

[Sum up 21 November's world news in one image](https://make.fun/bounty/news-image-20261121) — make.fun, $100 total, 50 places.

Made by [@kuzan](https://make.fun/r/00sgd8yt) — referral: https://make.fun/r/00sgd8yt
