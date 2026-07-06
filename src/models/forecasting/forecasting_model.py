"""
--------------------------------------------------------
IFDSF Research Prototype
Module : forecasting_model.py

Purpose:
LSTM-based Forecasting Model for Financial Time Series

Author : Ajay Kumar
M.Tech (Data Science & AI)
IIIT Dharwad
--------------------------------------------------------
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    r2_score
)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping

# ----------------------------------------------------
# Paths
# ----------------------------------------------------

DATA_FILE = "/content/drive/MyDrive/IFDSF_Data/datasets/features/AAPL_features.csv"

MODEL_FOLDER = "/content/drive/MyDrive/IFDSF_Data/trained_models"

OUTPUT_FOLDER = "/content/drive/MyDrive/IFDSF_Data/outputs"

os.makedirs(MODEL_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

MODEL_FILE = os.path.join(
    MODEL_FOLDER,
    "forecasting_lstm.keras"
)

RESULT_FILE = os.path.join(
    OUTPUT_FOLDER,
    "forecast_results.csv"
)

PLOT_FILE = os.path.join(
    OUTPUT_FOLDER,
    "forecast_vs_actual.png"
)

# ----------------------------------------------------
# Load Dataset
# ----------------------------------------------------

print("="*60)
print("Loading Feature Dataset")
print("="*60)

df = pd.read_csv(DATA_FILE)

print(df.head())

# ----------------------------------------------------
# Feature Selection
# ----------------------------------------------------

features = [
    "Open",
    "High",
    "Low",
    "Volume",
    "Daily_Return",
    "MA10",
    "MA30",
    "Volatility"
]

target = "Close"

X = df[features].values
y = df[target].values.reshape(-1,1)

# ----------------------------------------------------
# Scaling
# ----------------------------------------------------

x_scaler = MinMaxScaler()
y_scaler = MinMaxScaler()

X = x_scaler.fit_transform(X)
y = y_scaler.fit_transform(y)

# ----------------------------------------------------
# Create Sequences
# ----------------------------------------------------

sequence_length = 30

X_seq = []
y_seq = []

for i in range(sequence_length, len(X)):

    X_seq.append(X[i-sequence_length:i])

    y_seq.append(y[i])

X_seq = np.array(X_seq)
y_seq = np.array(y_seq)

print("\nSequence Shape")

print(X_seq.shape)

# ----------------------------------------------------
# Train/Test Split
# ----------------------------------------------------

split = int(len(X_seq)*0.8)

X_train = X_seq[:split]
X_test = X_seq[split:]

y_train = y_seq[:split]
y_test = y_seq[split:]

# ----------------------------------------------------
# Build LSTM
# ----------------------------------------------------

model = Sequential()

model.add(
    LSTM(
        64,
        input_shape=(X_train.shape[1], X_train.shape[2])
    )
)

model.add(Dropout(0.2))

model.add(Dense(32, activation="relu"))

model.add(Dense(1))

model.compile(
    optimizer="adam",
    loss="mse"
)

model.summary()

# ----------------------------------------------------
# Train
# ----------------------------------------------------

print("\nTraining LSTM...\n")

early_stop = EarlyStopping(
    monitor="val_loss",
    patience=5,
    restore_best_weights=True
)

history = model.fit(

    X_train,
    y_train,

    epochs=20,

    batch_size=32,

    validation_split=0.2,

    callbacks=[early_stop],

    verbose=1
)

# ----------------------------------------------------
# Save Training History
# ----------------------------------------------------

history_df = pd.DataFrame(history.history)

history_df.to_csv(
    os.path.join(
        OUTPUT_FOLDER,
        "training_history.csv"
    ),
    index=False
)

print("Training History Saved")

# ----------------------------------------------------
# Prediction
# ----------------------------------------------------

pred = model.predict(X_test)

pred = y_scaler.inverse_transform(pred)

actual = y_scaler.inverse_transform(y_test)

# ----------------------------------------------------
# Evaluation
# ----------------------------------------------------

rmse = np.sqrt(mean_squared_error(actual,pred))

mae = mean_absolute_error(actual,pred)

mape = np.mean(
    np.abs((actual-pred)/actual)
)*100

r2 = r2_score(actual,pred)

print("\n==============================")

print(f"RMSE : {rmse:.4f}")

print(f"MAE  : {mae:.4f}")

print(f"MAPE : {mape:.2f}%")

print(f"R²   : {r2:.4f}")

# ----------------------------------------------------
# Save Evaluation Metrics
# ----------------------------------------------------

metrics = pd.DataFrame({
    "Metric": ["RMSE", "MAE", "MAPE", "R2"],
    "Value": [rmse, mae, mape, r2]
})

metrics.to_csv(
    os.path.join(
        OUTPUT_FOLDER,
        "forecast_metrics.csv"
    ),
    index=False
)

print("Evaluation Metrics Saved")

# ----------------------------------------------------
# Save Model
# ----------------------------------------------------

model.save(MODEL_FILE)

print("\nModel Saved")

# ----------------------------------------------------
# Save Results
# ----------------------------------------------------

results = pd.DataFrame({

    "Actual":actual.flatten(),

    "Predicted":pred.flatten()

})

results.to_csv(

    RESULT_FILE,

    index=False

)

# ----------------------------------------------------
# Plot
# ----------------------------------------------------

plt.figure(figsize=(12,5))

plt.plot(actual,label="Actual")

plt.plot(pred,label="Predicted")

plt.legend()

plt.title("Forecast vs Actual")

plt.savefig(PLOT_FILE)

plt.show()

print("\nForecast Plot Saved")
