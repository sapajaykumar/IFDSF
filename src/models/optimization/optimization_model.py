"""
--------------------------------------------------------
IFDSF Research Prototype
Module : optimization_model.py

Purpose:
Financial Planning & Decision Support Engine

Semester 2:
Rule-based Optimization

Future:
Reinforcement Learning based Optimization

Author : Ajay Kumar
M.Tech (Data Science & AI)
IIIT Dharwad
--------------------------------------------------------
"""

import os
import pandas as pd

# ----------------------------------------------------
# Paths
# ----------------------------------------------------

OUTPUT_FOLDER = "/content/drive/MyDrive/IFDSF_Data/outputs"

FORECAST_RESULTS = os.path.join(
    OUTPUT_FOLDER,
    "forecast_results.csv"
)

FORECAST_METRICS = os.path.join(
    OUTPUT_FOLDER,
    "forecast_metrics.csv"
)

OPTIMIZATION_RESULTS = os.path.join(
    OUTPUT_FOLDER,
    "optimization_results.csv"
)

# ----------------------------------------------------
# Load Forecast Information
# ----------------------------------------------------

def load_forecast():

    forecast = pd.read_csv(FORECAST_RESULTS)

    metrics = pd.read_csv(FORECAST_METRICS)

    latest = forecast.iloc[-1]

    return latest, metrics

# ----------------------------------------------------
# Decision Logic
# ----------------------------------------------------

def generate_recommendation(mape):

    if mape < 5:

        return (
            "Increase Investment",
            "Low",
            95
        )

    elif mape < 10:

        return (
            "Maintain Current Budget",
            "Medium",
            85
        )

    else:

        return (
            "Reduce Financial Exposure",
            "High",
            70
        )

# ----------------------------------------------------
# Main
# ----------------------------------------------------

def main():

    print("=" * 60)
    print("IFDSF Decision Support Engine")
    print("=" * 60)

    latest, metrics = load_forecast()

    actual = latest["Actual"]

    predicted = latest["Predicted"]

    mape = float(
        metrics.loc[
            metrics["Metric"] == "MAPE",
            "Value"
        ].values[0]
    )

    recommendation, risk, confidence = generate_recommendation(mape)

    decision = pd.DataFrame({

        "Actual":[actual],

        "Forecast":[predicted],

        "MAPE":[round(mape,2)],

        "Risk Level":[risk],

        "Confidence (%)":[confidence],

        "Recommendation":[recommendation]

    })

    decision.to_csv(

        OPTIMIZATION_RESULTS,

        index=False

    )

    print("\nDecision Summary\n")

    print(decision)

    print("\nOptimization Result Saved")

    print(OPTIMIZATION_RESULTS)

# ----------------------------------------------------

if __name__ == "__main__":

    main()
