"""
--------------------------------------------------------
IFDSF Research Prototype
Module : ingestion.py

Purpose:
Loads datasets into memory for further processing.

Author : Ajay Kumar
M.Tech (Data Science & AI)
IIIT Dharwad
--------------------------------------------------------
"""

import pandas as pd

from data_catalog import DATASETS


def load_dataset(ticker):

    folder = DATASETS["D5"]["folder"]

    file_path = folder / f"{ticker}.csv"

    print(f"\nLoading {ticker} dataset...")

    df = pd.read_csv(file_path)

    print("Dataset Loaded Successfully.")

    print(f"Rows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")

    return df


def dataset_summary(df):

    print("\nColumns")

    print(df.columns.tolist())

    print("\nFirst Five Records")

    print(df.head())

    print("\nMissing Values")

    print(df.isnull().sum())


def main():

    tickers = ["AAPL", "MSFT", "TSLA"]

    for ticker in tickers:

        print("\n" + "="*60)

        df = load_dataset(ticker)

        dataset_summary(df)


if __name__ == "__main__":

    main()
