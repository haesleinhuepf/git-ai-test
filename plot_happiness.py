"""Plot happiness rank over time for Germany and its neighboring countries."""

import os
import pandas as pd
import matplotlib.pyplot as plt

# Germany's neighboring countries
COUNTRIES = [
    "Germany",
    "France",
    "Switzerland",
    "Austria",
    "Czech Republic",
    "Poland",
    "Denmark",
    "Netherlands",
    "Belgium",
    "Luxembourg",
]

YEARS = [2015, 2016, 2017, 2018, 2019]


def load_year(year):
    """Load happiness data for a given year and return a dict {country: rank}."""
    path = os.path.join(os.path.dirname(__file__), f"{year}.csv")
    df = pd.read_csv(path)

    # Normalize column names: strip whitespace, lowercase for lookup
    col_lower = {c.lower().strip(): c for c in df.columns}

    # Identify country column
    for candidate in ("country", "country or region"):
        if candidate in col_lower:
            country_col = col_lower[candidate]
            break
    else:
        raise ValueError(f"Cannot find country column in {year}.csv. Columns: {list(df.columns)}")

    # Identify rank column
    for candidate in ("happiness rank", "happiness.rank", "overall rank"):
        if candidate in col_lower:
            rank_col = col_lower[candidate]
            break
    else:
        raise ValueError(f"Cannot find rank column in {year}.csv. Columns: {list(df.columns)}")

    return dict(zip(df[country_col].str.strip(), df[rank_col]))


def main():
    data = {country: [] for country in COUNTRIES}
    valid_years = []

    for year in YEARS:
        try:
            ranks = load_year(year)
        except FileNotFoundError:
            print(f"Warning: {year}.csv not found, skipping.")
            continue
        valid_years.append(year)
        for country in COUNTRIES:
            data[country].append(ranks.get(country, None))

    fig, ax = plt.subplots(figsize=(10, 6))
    for country in COUNTRIES:
        ranks = data[country]
        ax.plot(valid_years, ranks, marker="o", label=country)

    ax.set_xlabel("Year")
    ax.set_ylabel("Happiness Rank (lower is happier)")
    ax.set_title("Happiness Rank Over Time: Germany and Neighboring Countries")
    ax.invert_yaxis()  # Rank 1 at the top
    ax.legend(loc="best")
    ax.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()

    output = "happiness_rank.png"
    plt.savefig(output)
    print(f"Plot saved to {output}")
    plt.show()


if __name__ == "__main__":
    main()
