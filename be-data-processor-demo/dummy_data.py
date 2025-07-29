import pandas as pd
from datetime import datetime
import random

def generate_dummy_df(code: str) -> pd.DataFrame:
    if code == "bulk_metrics_1":
        return pd.DataFrame({
            "col1": [f"user_{i}" for i in range(10)],
            "col2": [f"username_{i}" for i in range(10)],
            "col3": [f"metrics1_{i}" for i in range(10)],
            "col4": [datetime.now().isoformat()] * 10,
            "col5": [random.randint(1, 10) for _ in range(10)],
        })

    elif code == "bulk_metrics_2":
        return pd.DataFrame({
            "col1": [f"user_{i}" for i in range(10)],
            "col2": [f"username_{i}" for i in range(10)],
            "col3": [f"metrics2_{i}" for i in range(10)],
            "col4": [datetime.now().isoformat()] * 10,
            "col5": [random.randint(1, 10) for _ in range(10)],
        })

    elif code == "bulk_metrics_3":
        return pd.DataFrame({
            "col1": [f"user_{i}" for i in range(10)],
            "col2": [f"username_{i}" for i in range(10)],
            "col3": [f"metrics3_{i}" for i in range(10)],
            "col4": [datetime.now().isoformat()] * 10,
            "col5": [random.randint(1, 10) for _ in range(10)],
        })

    else:
        raise ValueError(f"No dummy data defined for code '{code}'")