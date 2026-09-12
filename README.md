# Nigerian Language Translator

Translate everyday English words into five Nigerian languages — Yoruba, Hausa, Igbo, Idoma, and Kanuri — and back again.

**Live app:** _https://nigerian-language-translator-d1erma8btsf.streamlit.app/_

---

## Origin

This project started as a group assignment for **COS-CLUB** at Bingham University, where each team member contributed an initial word list for one language. This repository is an independent continuation of that original project — restructuring the data, expanding it from verified sources, and adding features. The original group version remains intact and credited; nothing here replaces it.

## Why these 5 languages

Earlier drafts of this project experimented with expanding to over 20 Nigerian languages using an academic core-vocabulary database. That expansion was scaled back deliberately: five well-documented, verifiable languages are worth more than twenty thin, unverified ones. Every language below meets a minimum bar of either substantial word count, a traceable open-license source, or both.

## Word counts and sources

| Language | Entries | Primary source |
|---|---|---|
| Igbo | 2,731 | English-Igbo Dictionary dataset (Kaggle, scraped from igboenglish.com) |
| Hausa | 1,220 | World Loanword Database (WOLD) — Awagana & Wolff (2009), CC BY 3.0 |
| Yoruba | 357 | Original COS-CLUB contribution + filtered common-vocabulary list + Crowther's 1852 Yoruba vocabulary (public domain) |
| Idoma | 121 | Original COS-CLUB contribution + UCLA Phonetics Archive (1960–1962 field word lists) + Wikipedia (Idoma language, animal names) |
| Kanuri | 99 | ASJP Database core vocabulary, sourced from published Kanuri wordlists, CC BY 4.0 |

Full attribution for each academic source is in the **Sources & Licensing** section below.

## Features

- **Two-way translation** — English to your chosen language, or that language back to English
- **Fuzzy matching** — small spelling mistakes or typos still find the right word
- **Live suggestions** — as you type, matching words appear before you hit translate
- **Session translation counter** — tracks how many successful translations happen per visit

## How it works

Each language's word list lives in its own JSON file (`yoruba.json`, `hausa.json`, `igbo.json`, `idoma.json`, `kanuri.json`), loaded at startup. The app is built with [Streamlit](https://streamlit.io).

## Running it locally

```bash
pip install streamlit
streamlit run DICT2.py
```

Make sure all five `.json` files are in the same folder as `DICT2.py` before running.

## Project structure

```
COS-CLUB/
├── DICT2.py
├── yoruba.json
├── hausa.json
├── igbo.json
├── idoma.json
├── kanuri.json
└── README.md
```

## Data quality notes

- Igbo entries were filtered from a larger scraped dataset — phrases and misaligned rows were removed, keeping only clean single-word English-to-Igbo pairs.
- Hausa entries use double vowels (e.g. `ruwaa`, `raanaa`) to mark long vowels — this is intentional academic transcription, not a typo.
- Yoruba includes a small number of entries from a 170-year-old missionary vocabulary; spelling in those entries reflects 1852 orthography, not necessarily modern usage.
- None of these word lists have been fully verified by native speakers of every language. Community contributions and corrections are welcome — see below.

## Roadmap

- Native-speaker verification pass on all five languages, starting with Yoruba
- Grow Idoma and Kanuri past their current core-vocabulary stage
- Deploy publicly via Streamlit Community Cloud

## Contributing

If you speak any of these languages and want to help verify or expand the word lists, contributions are welcome — accuracy matters more than volume, so please only add or confirm words you're genuinely confident about.

## Sources & Licensing

- **Igbo:** Goody Duru, *English-Igbo Dictionary* dataset, Kaggle (scraped from igboenglish.com).
- **Hausa:** Awagana, Ari & Wolff, H. Ekkehard. 2009. "Hausa Vocabulary." In Haspelmath, Martin & Tadmor, Uri (eds.) *World Loanword Database*. Leipzig: Max Planck Institute for Evolutionary Anthropology. Licensed CC BY 3.0.
- **Yoruba (historical entries):** Crowther, Samuel. *A Vocabulary of the Yoruba Language* (1852). Public domain.
- **Idoma:** UCLA Phonetics Archive, Idoma word lists (1960–1962). Idoma language article, Wikipedia (animal names section).
- **Kanuri:** Wichmann, Søren & Brown, Cecil H. & Holman, Eric W. et al. *The ASJP Database*, Max Planck Institute for Evolutionary Anthropology. Licensed CC BY 4.0.

## Tech stack

Python · Streamlit · JSON
