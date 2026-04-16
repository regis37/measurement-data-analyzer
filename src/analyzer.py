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

def generate_plots(df: pd.DataFrame, output_dir: str) -> None:
    """
    Generate and save plots for each measurement column.
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # We skip the 'timestamp' column
    measurement_columns = [col for col in df.columns if col != "timestamp"]

    for col in measurement_columns:
        fig, ax = plt.subplots(figsize=(10, 5))

        ax.plot(df["timestamp"], df[col], color="steelblue", linewidth=1.5)

        ax.set_title(f"Measurement: {col}", fontsize=14)
        ax.set_xlabel("Time (s)")
        ax.set_ylabel(col)
        ax.grid(True)

        # Save the plot as a PNG file
        output_path = os.path.join(output_dir, f"{col}.png")
        plt.savefig(output_path)
        plt.close(fig)

        print(f"Plot saved: {output_path}")

def export_report(stats: dict, output_dir: str) -> None:
    """
    Export a text report with all statistical results.
    """
    os.makedirs(output_dir, exist_ok=True)
    report_path = os.path.join(output_dir, "report.txt")

    with open(report_path, "w") as f:
        f.write("=" * 50 + "\n")
        f.write("   MEASUREMENT DATA ANALYSIS REPORT\n")
        f.write("=" * 50 + "\n\n")

        for col, values in stats.items():
            f.write(f"[ {col} ]\n")
            f.write(f"  Min      : {values['min']}\n")
            f.write(f"  Max      : {values['max']}\n")
            f.write(f"  Mean     : {values['mean']}\n")
            f.write(f"  Std Dev  : {values['std']}\n")
            f.write("\n")

        f.write("=" * 50 + "\n")
        f.write("End of report\n")

    print(f"Report saved: {report_path}")