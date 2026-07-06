"""
--------------------------------------------------------
IFDSF Research Prototype
Module : feature_engineering.py

Purpose:
Creates features for forecasting.

Author : Ajay Kumar
M.Tech (Data Science & AI)
IIIT Dharwad
--------------------------------------------------------
"""

import os
import pandas as pd

PROCESSED_FOLDER = "/content/drive/MyDrive/IFDSF_Data/datasets/processed"
FEATURE_FOLDER = "/content/drive/MyDrive/IFDSF_Data/datasets/features"

os.makedirs(FEATURE_FOLDER, exist_ok=True)


def create_features(ticker):

    input_file = f"{PROCESSED_FOLDER}/{ticker}_clean.csv"

    output_file = f"{FEATURE_FOLDER}/{ticker}_features.csv"

    print("\n" + "=" * 60)
    print(f"Feature Engineering : {ticker}")
    print("=" * 60)

    df = pd.read_csv(input_file)

    # Convert Date
    df["Date"] = pd.to_datetime(df["Date"])

    # Daily Return
    df["Daily_Return"] = df["Close"].pct_change()

    # 10-Day Moving Average
    df["MA10"] = df["Close"].rolling(10).mean()

    # 30-Day Moving Average
    df["MA30"] = df["Close"].rolling(30).mean()

    # 10-Day Volatility
    df["Volatility"] = df["Close"].rolling(10).std()

    # Remove empty rows
    df = df.dropna()

    # Save
    df.to_csv(output_file, index=False)

    print(f"Saved : {output_file}")
    print(f"Rows : {len(df)}")
    print(f"Columns : {len(df.columns)}")


def main():

    tickers = ["AAPL", "MSFT", "TSLA"]

    for ticker in tickers:

        create_features(ticker)


if __name__ == "__main__":
    main()
