"""
Plot happiness rank of Germany and its neighbors over time (2015-2019).

Schema normalization:
- 2015/2016: columns 'Country' and 'Happiness Rank'
- 2017:      columns 'Country' and 'Happiness.Rank'
- 2018/2019: columns 'Country or region' and 'Overall rank'

All yearly DataFrames are normalized to common column names
'Country' and 'Rank' before concatenation.
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

COUNTRIES = [
    "Germany",
    "Denmark",
    "Poland",
    "Czech Republic",
    "Austria",
    "Switzerland",
    "France",
    "Luxembourg",
    "Belgium",
    "Netherlands",
]

YEAR_FILES = {
    2015: "2015.csv",
    2016: "2016.csv",
    2017: "2017.csv",
    2018: "2018.csv",
    2019: "2019.csv",
}


def load_year(year, filename):
    df = pd.read_csv(os.path.join(SCRIPT_DIR, filename))

    # Normalize country column
    if "Country or region" in df.columns:
        df = df.rename(columns={"Country or region": "Country"})

    # Normalize rank column
    if "Happiness Rank" in df.columns:
        df = df.rename(columns={"Happiness Rank": "Rank"})
    elif "Happiness.Rank" in df.columns:
        df = df.rename(columns={"Happiness.Rank": "Rank"})
    elif "Overall rank" in df.columns:
        df = df.rename(columns={"Overall rank": "Rank"})

    df["Year"] = year
    return df[["Country", "Rank", "Year"]]


frames = [load_year(year, fname) for year, fname in YEAR_FILES.items()]
data = pd.concat(frames, ignore_index=True)

# Keep only countries of interest that appear in the data
available = [c for c in COUNTRIES if c in data["Country"].values]
data = data[data["Country"].isin(available)]

pivot = data.pivot(index="Year", columns="Country", values="Rank")

fig, ax = plt.subplots(figsize=(10, 6))
for country in available:
    if country in pivot.columns:
        ax.plot(pivot.index, pivot[country], marker="o", label=country)

ax.invert_yaxis()  # Lower rank number = happier, so rank 1 is at the top
ax.set_xlabel("Year")
ax.set_ylabel("Happiness Rank (lower is better)")
ax.set_title("Happiness Rank of Germany and Neighboring Countries (2015–2019)")
ax.legend(loc="best")
ax.set_xticks(list(YEAR_FILES.keys()))

output_path = os.path.join(SCRIPT_DIR, "happiness_rank.png")
plt.tight_layout()
plt.savefig(output_path, dpi=150)
print(f"Plot saved to {output_path}")
