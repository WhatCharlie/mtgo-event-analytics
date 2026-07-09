# MTGO Event Analytics

## Overview
MTGO Event Analytics is a Python-based data pipeline for collecting Magic: The Gathering Online (MTGO) tournament data, transforming it into structured datasets, and preparing those datasets for metagame analysis and visualization.

## Features
- Scrapes tournament event data from the MTGO website
- Extracts embedded JSON from event pages
- Parses event metadata, standings, decklists, and playoff brackets
- Saves structured datasets for further analysis
- Modular Python package design

## Project Structure
```text
mtgo_event_analytics/
├── scraper/      # reusable modules for scraping and parsing event data
├── notebooks/    # Jupyter notebooks for running the pipeline
├── data/
│   ├── raw/      # downloaded event data
│   └── processed/ # cleaned datasets for analysis
├── README.md
├── requirements.txt
└── .gitignore
```