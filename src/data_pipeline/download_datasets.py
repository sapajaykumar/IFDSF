"""
--------------------------------------------------------
IFDSF Research Prototype
Module : download_datasets.py

Purpose:
Downloads and stores datasets required for the IFDSF
research project.

Current Implementation:
- Yahoo Finance (Implemented)

Future Implementation:
- SEC EDGAR
- Kaggle Corporate Dataset
- M5 Forecasting Dataset
- FRED Economic Data

Author : Ajay Kumar
M.Tech (Data Science & AI)
IIIT Dharwad
--------------------------------------------------------
"""

import os
import yfinance as yf

from src.data_pipeline.data_catalog import DATASETS

# --------------------------------------------------------
# Stocks to Download
# --------------------------------------------------------

TICKERS = [
    "AAPL",
    "MSFT",
    "TSLA"
]

# --------------------------------------------------------
# Create Dataset Folders
# --------------------------------------------------------

def create_dataset_folders():

    print("\nCreating Dataset Folders...\n")

    for dataset in DATASETS.values():

        folder = dataset["folder"]

        os.makedirs(folder, exist_ok=True)

        print(f"✓ {folder}")

    print("\nAll folders are ready.\n")


# --------------------------------------------------------
# Download Yahoo Finance Dataset
# --------------------------------------------------------

def download_yahoo_finance(
    ticker,
    start_date="2020-01-01",
    end_date="2025-01-01"
):

    print(f"\nDownloading {ticker} data...\n")

    folder = DATASETS["D5"]["folder"]

    file_path = folder / f"{ticker}.csv"

    data = yf.download(
        ticker,
        start=start_date,
        end=end_date,
        progress=False,
        auto_adjust=False
    )

    # Flatten MultiIndex columns if required
    if hasattr(data.columns, "nlevels") and data.columns.nlevels > 1:
        data.columns = data.columns.get_level_values(0)

    data.to_csv(file_path, index_label="Date")

    print(f"Dataset Saved : {file_path}")
    print(f"Records : {len(data)}")


# --------------------------------------------------------
# Main Function
# --------------------------------------------------------

def main():

    print("=" * 60)
    print("IFDSF Dataset Downloader")
    print("=" * 60)

    create_dataset_folders()

    for ticker in TICKERS:
        download_yahoo_finance(ticker)

    print("\nDownload Completed Successfully.")


# --------------------------------------------------------

if __name__ == "__main__":

    main()
