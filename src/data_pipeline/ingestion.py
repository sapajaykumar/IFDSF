"""
--------------------------------------------------------
IFDSF Research Prototype
Module : ingestion.py

Purpose:
Loads raw datasets into memory for further processing.

Author : Ajay Kumar
M.Tech (Data Science & AI)
IIIT Dharwad
--------------------------------------------------------
"""

import pandas as pd
from pathlib import Path

from src.data_pipeline.data_catalog import DATASETS


def load_dataset(dataset_id="D5", file_name="AAPL.csv"):
    """
    Load a dataset from the dataset folder.
    """

    folder = DATASETS[dataset_id]["folder"]
    file_path = folder / file_name

    print(f"\nLoading Dataset...")
    print(f"File : {file_path}")

    df = pd.read_csv(file_path)

    print("\nDataset Loaded Successfully.")
    print(f"Rows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")

    return df


def dataset_summary(df):
    """
    Display basic dataset information.
    """

    print("\n" + "=" * 60)
    print("Dataset Information")
    print("=" * 60)

    print(df.info())

    print("\nFirst Five Records\n")
    print(df.head())

    print("\nStatistical Summary\n")
    print(df.describe())


def main():

    df = load_dataset()

    dataset_summary(df)


if __name__ == "__main__":

    main()
