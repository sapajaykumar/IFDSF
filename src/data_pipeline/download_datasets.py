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
from pathlib import Path
import yfinance as yf

from src.data_pipeline.data_catalog import DATASETS


# --------------------------------------------------------
# Create Dataset Folders
# --------------------------------------------------------

def create_dataset_folders():
    """
    Create dataset folders if they do not exist.
    """

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
    ticker="AAPL",
    start_date="2020-01-01",
    end_date="2025-01-01"
):
    """
    Downloads stock market data from Yahoo Finance.
    """

    print("\nDownloading Yahoo Finance Data...\n")

    folder = DATASETS["D5"]["folder"]

    file_name = f"{ticker}.csv"

    file_path = folder / file_name

    data = yf.download(
        ticker,
        start=start_date,
        end=end_date,
        progress=False
    )

    data.to_csv(file_path)

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

    download_yahoo_finance()

    print("\nDownload Completed Successfully.")


# --------------------------------------------------------

if __name__ == "__main__":

    main()
