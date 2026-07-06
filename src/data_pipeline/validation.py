"""
--------------------------------------------------------
IFDSF Research Prototype
Module : validation.py

Purpose:
Validates datasets before preprocessing.

Author : Ajay Kumar
M.Tech (Data Science & AI)
IIIT Dharwad
--------------------------------------------------------
"""

import pandas as pd

from src.data_pipeline.data_catalog import DATASETS


def validate_dataset(ticker):

    folder = DATASETS["D5"]["folder"]
    file_path = folder / f"{ticker}.csv"

    print("\n" + "="*60)
    print(f"Validating {ticker}")
    print("="*60)

    df = pd.read_csv(file_path)

    print(f"Rows              : {len(df)}")
    print(f"Columns           : {len(df.columns)}")
    print(f"Duplicate Rows    : {df.duplicated().sum()}")
    print(f"Missing Values    : {df.isnull().sum().sum()}")

    print("\nData Types")
    print(df.dtypes)

    if df.isnull().sum().sum() == 0:
        print("\n✅ Dataset Validation Passed")
    else:
        print("\n❌ Missing Values Found")


def main():

    tickers = ["AAPL", "MSFT", "TSLA"]

    for ticker in tickers:
        validate_dataset(ticker)


if __name__ == "__main__":
    main()
