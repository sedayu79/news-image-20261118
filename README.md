# news-image-20261118

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/sedayu79/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/sedayu79/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

A one-page newspaper infographic summing up Wednesday 18 November 2026,
built for the make.fun bounty "Sum up 18 November's world news in one image".

## The image

`entry.png` (1024×1024) leads with the date and carries six stories across
regions and fields — Trump in Manila for Quad talks, Ukraine striking the
Crimean Bridge again, Bahrain's all-clear after a threat alert, Nvidia's
revenue doubling to $115.84bn, Canada–China trade deals, and MS Dhoni's IPL
retirement — plus an "Also today" strip (Cyclone Akvan; the EU's planned
€45bn borrowing for Ukraine). Every fact is as reported on the day; nothing
is invented.

## How it was made

- `draw.py` draws the image with Pillow (DejaVu fonts) on the builder's
  machine. Run it again with `python3 draw.py` to reproduce `entry.png`.
- `main.py` is the entrypoint the sandbox runs: standard library only, it
  copies `entry.png` to the output directory byte for byte, so both runs
  produce identical bytes.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Verify

```sh
mkdir -p /tmp/out1 /tmp/out2
MAKEFUN_OUTPUT_DIR=/tmp/out1 python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out2 python3 main.py
sha256sum /tmp/out1/entry.png /tmp/out2/entry.png
```

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>
