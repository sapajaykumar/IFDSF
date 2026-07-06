"""
--------------------------------------------------------
IFDSF Research Prototype
Module : preprocessing.py

Purpose:
Cleans and prepares datasets for feature engineering
and forecasting.

Author : Ajay Kumar
M.Tech (Data Science & AI)
IIIT Dharwad
--------------------------------------------------------
"""

import os
import pandas as pd

from src.data_pipeline.data_catalog import DATASETS


def preprocess_dataset(ticker):

    raw_folder = DATASETS["D5"]["folder"]

    processed_folder = raw_folder.parent / "processed"

    os.makedirs(processed_folder, exist_ok=True)

    input_file = raw_folder / f"{ticker}.csv"

    output_file = processed_folder / f"{ticker}_clean.csv"

    print("\n" + "="*60)
    print(f"Preprocessing {ticker}")
    print("="*60)

    df = pd.read_csv(input_file)

    # -----------------------------
    # Convert Date
    # -----------------------------
    df["Date"] = pd.to_datetime(df["Date"])

    # -----------------------------
    # Remove unwanted column
    # -----------------------------
    if "Adj Close" in df.columns:
        df.drop(columns=["Adj Close"], inplace=True)

    # -----------------------------
    # Sort by Date
    # -----------------------------
    df = df.sort_values("Date")

    # -----------------------------
    # Remove duplicates
    # -----------------------------
    df = df.drop_duplicates()

    # -----------------------------
    # Handle missing values
    # -----------------------------
    df = df.dropna()

    # -----------------------------
    # Save cleaned dataset
    # -----------------------------
    df.to_csv(output_file, index=False)

    print(f"Saved : {output_file}")
    print(f"Rows  : {len(df)}")
    print(f"Columns : {len(df.columns)}")

    return df


def main():

    tickers = ["AAPL", "MSFT", "TSLA"]

    for ticker in tickers:

        preprocess_dataset(ticker)


if __name__ == "__main__":

    main()
