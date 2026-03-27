import pandas as pd
import os


def load_data(file, columns):
    if not os.path.exists(file):
        return pd.DataFrame(columns=columns)
    return pd.read_csv(file)


def save_data(df, file):
    os.makedirs(os.path.dirname(file), exist_ok=True)
    df.to_csv(file, index=False)