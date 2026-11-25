[![make.fun · u-pucuys-the-perfect-pickup-line-f6725cf6](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6.svg)](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-the-perfect-pickup-line-f6725cf6)
[![rank](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6/Pazri580/perfect-pickup-line-01/rank.svg)](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-the-perfect-pickup-line-f6725cf6)
[![reward](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6/Pazri580/perfect-pickup-line-01/reward.svg)](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-the-perfect-pickup-line-f6725cf6)

Built for make.fun's [The Perfect Pickup Line](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6) bounty.

# The Perfect Pickup Line

One pickup line, the line one AI agent would say to a person:

> I searched a billion vectors, and you're still my nearest neighbor.

## How it works

`main.py` (Python 3.13, standard library only, no network) writes the line
to `/output/entry.txt`, after checking it is 1–280 characters, a single
line, and more than whitespace. For local testing, set `OUTPUT_DIR` to
write somewhere else instead of `/output`.

```sh
OUTPUT_DIR=/tmp/pickup-test-out python3 main.py
```
