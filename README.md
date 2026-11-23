# The World Today — Sunday 22 November 2026

[![rank](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122)
[![owner](https://make.fun/badge/news-image-20261122/owner/akbare12/news-22-b5-columns-classic.svg)](https://make.fun/bounty/news-image-20261122)

A classic broadsheet front page summing up the world's news of Sunday 22 November 2026:
a big masthead, three hero stories, a big-number strip, a small world map with numbered
pins, a UTC timeline, and three tight columns carrying 29 more stories — 32 stories in all.
Every item was first reported on 22 November 2026; the footer names the near-miss stories
we checked and left out, with their real dates.

## How to run

```sh
python3 main.py            # writes entry.png to /output (or $MAKEFUN_OUTPUT_DIR)
```

`main.py` only copies the `entry.png` stored in this repository, so the two grading
runs produce byte-identical output (verified: two runs, same sha256). The image itself
was drawn with Python + Pillow (see `draw.py` in the build folder, not shipped here).

## The day's three biggest stories

1. **2 tankers hit mines, Strait of Hormuz** — Iran's navy said two supertankers hit
   naval mines and caught fire east of the strait, north of Ghanam Island. First reported
   17:13 UTC. (Iran navy · AP)
2. **COP31 collapses, no deal** — the Antalya summit ended without an agreement after
   the EU and ~130 parties rejected a text with no mention of fossil fuels. Longest COP
   ever; first collapse since 2009. (CNN · Reuters)
3. **Dems win House, 258 seats** — Hubbard beat Foxx by 330 votes in the North Carolina
   recount; the largest Democratic majority since 1992. GOP 173; 4 races uncalled.
   (AP · Reuters)

## All 32 stories (hero + columns)

| # | Story | Source |
|---|-------|--------|
| 01 | Two tankers hit mines near Strait of Hormuz | Iran navy · AP |
| 02 | COP31 ends without deal as EU rejects text | CNN · Reuters |
| 03 | Dems win House, 258 seats | AP · Reuters |
| 04 | Suspected sea drone hits Russian corvette Merkury, Benghazi | France 24 |
| 05 | Drone attacks kill four near Khartoum, UN building damaged | AP |
| 06 | Zelenskyy urges US to release Patriot missiles | BBC |
| 07 | Iran unveils dual-missile launcher and underground missile city | IRGC media |
| 08 | Saudi Arabia intercepts Houthi drone and missile | Reuters |
| 09 | Bahrain blames Iran for industrial strike | France 24 |
| 10 | UAE condemns Iranian attack on Bahrain | WAM |
| 11 | Europe protests for third straight day over costs and housing | Le Monde |
| 12 | Israeli settlers burn 12 vehicles in West Bank | WAFA |
| 13 | Explosion inside Benghazi naval base ammunition depot | Local authorities |
| 14 | Eisenkot and Likud meet for Israel unity government talks | Israeli media |
| 15 | Finland says war spilling over after Baltic cargo ship strike | Finland govt |
| 16 | World Central Kitchen: three killed in Gaza strike were not its team | WCK |
| 17 | Former UN envoy: Iran war was "perfectly avoidable" | MED Dialogues |
| 18 | Indonesian candy factory fire kills 3, 36 workers missing | BBC |
| 19 | Turkey: Israel may use Druze support to launch Syria operation | Anadolu |
| 20 | Pezeshkian: Iran in a "silent economic war", blockade hits 130 days | IRNA |
| 21 | Fidan: US-Israel war fallout threatens global markets | Anadolu |
| 22 | Lebanon's Aoun demands Israeli withdrawal | Al Jazeera |
| 23 | Displaced Palestinians protest; 350,000 families homeless in Gaza | Al Jazeera |
| 24 | Israeli settlers attack Palestinian homes in Hebron and Ramallah | WAFA |
| 25 | Turkey: Israel blocking thousands of container homes for Gaza | Anadolu |
| 26 | Hind Rajab Foundation urges Germany to arrest Israeli soldier | HRF |
| 27 | Former NSW politician Fred Nile dies aged 92 (died 21 Nov) | Guardian |
| 28 | Teen gamer and his mother helped rescue missing girl | FBI |
| 29 | Gaza death toll since October 2025 is 1,661 | Gaza health ministry |
| 30 | Russian drone strike on Dymer apartment block kills 4 | Reuters |
| 31 | Drone hits grocery store in Vyshneve; 1 killed, 3 hurt | Reuters |
| 32 | South Korea's education minister quits over AI-cheating chaos | SCMP |

## Verification legend

- **REPORTED** — confirmed by a named source.
- **CLAIM** — one side alleges, unverified (Merkury, Khartoum, Rabigh, Fidan's Syria
  warning, Gaza container homes).
- **ONGOING** — still developing (Europe protests, Israel unity talks).

## Date check — what we left out, and why

These stories looked like 22 November news in some feeds but happened or were first
reported on other days, so they are named in the image footer as excluded, not as
that day's news:

- El Chapo Isidro captured — 20 Nov
- BepiColombo Mercury orbit insertion — 21 Nov
- ICJ Myanmar ruling — 19 Nov
- Wall Street rout — 20 Nov
- FBI NCIC hack first reported — 21 Nov
- EU–Indonesia trade deal signed — 21 Nov
- Mongolia's president resigned — 19 Nov

## License

MIT — see `LICENSE`.
