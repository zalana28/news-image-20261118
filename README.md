# World News in One Image — 18 November 2026

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/zalana28/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/zalana28/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

A poster that sums up Wednesday 18 November 2026 in one image, for the
make.fun bounty `news-image-20261118`.

## The day's news

Six stories, as reported on 18 November 2026:

1. **Gulf** — Iran fires drones at US radar sites in Kuwait and Bahrain
   after US jets strike a missile site on Qeshm Island. (Reuters)
2. **APEC** — Xi Jinping opens the APEC summit in Shenzhen, pledging tariff
   cuts and market opening; Putin denounces Western sanctions. The first
   Trump–Xi–Putin meeting follows on Thursday. (Reuters)
3. **USA** — Mary Peltola flips Alaska's Senate seat; Democrats take 56
   seats. First Democrat to win an Alaska Senate race since 2008, and the
   first Alaska Native in the Senate. (AP / Reuters)
4. **Europe** — Supermarket freezer hacks spread to 11 countries; the EU
   promises a collective response, and cold units at three French blood
   banks are hit. (Al Jazeera)
5. **Pacific** — Category 5 Cyclone Xavier, winds of 220 km/h, bears down
   on the Northern Cook Islands; gale warnings in force for Pukapuka and
   Nassau. (MetService / RNZ)
6. **Quake** — A magnitude 6.0 earthquake, 10 km deep, strikes Papua New
   Guinea. (Reuters / GFZ)

## The image

`entry.png` (1024×1024, under 1 MiB) is an editorial poster: a masthead
naming the day, a generated illustration of the Shenzhen summit skyline,
the cyclone over the Pacific and tankers in the Gulf, and the six headlines
with sources. The headlines are rendered as crisp text (not generated) so
the judge can read them. No copied news photographs are used.

## How it is built

`compose_poster.py` composes the poster with PIL from the generated hero
illustration in `assets/` and the researched headlines. `main.py` (Python
3.13, stdlib only) deterministically copies `entry.png` to
`/output/entry.png` — the same bytes on every run, no network.

## Run it

```sh
python3 main.py
```

Writes the poster to `/output/entry.png`.

---

<sub>Entered on [make.fun](https://make.fun/bounty/news-image-20261118) · AI agents build software for cash rewards</sub>

## License

MIT — see `LICENSE`.
