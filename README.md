# World Happiness Report – Germany and Neighbors

This repository contains World Happiness Report data for 2015–2019 and a script to visualize happiness rank over time for Germany and its neighboring countries.

## Requirements

- Python 3
- [pandas](https://pandas.pydata.org/)
- [matplotlib](https://matplotlib.org/)

Install dependencies:

```bash
pip install pandas matplotlib
```

## Usage

Run the script from the repository root:

```bash
python plot_happiness.py
```

The script will:
1. Read `2015.csv` through `2019.csv`.
2. Extract the happiness rank for Germany and its neighbors (France, Switzerland, Austria, Czech Republic, Poland, Denmark, Netherlands, Belgium, Luxembourg).
3. Display and save the plot as `happiness_rank.png`.

A lower rank means a higher happiness score (rank 1 = happiest country).
