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