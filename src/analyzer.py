# analyzer.py
# Automated analysis and visualization of electrical measurement data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


def load_data(filepath: str) -> pd.DataFrame:
    """
    Load measurement data from a CSV file.
    Returns a pandas DataFrame.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Data file not found: {filepath}")

    df = pd.read_csv(filepath)
    print(f"Data loaded successfully — {len(df)} rows, {len(df.columns)} columns")
    return df

def analyze_data(df: pd.DataFrame) -> dict:
    """
    Compute statistical analysis for each measurement column.
    Returns a dictionary with min, max, mean and standard deviation.
    """
    # We skip the 'timestamp' column — it's not a measurement
    measurement_columns = [col for col in df.columns if col != "timestamp"]

    stats = {}
    for col in measurement_columns:
        stats[col] = {
            "min":   round(df[col].min(), 4),
            "max":   round(df[col].max(), 4),
            "mean":  round(df[col].mean(), 4),
            "std":   round(df[col].std(), 4)
        }
        print(f"{col} — min: {stats[col]['min']}, max: {stats[col]['max']}, "
              f"mean: {stats[col]['mean']}, std: {stats[col]['std']}")

    return stats