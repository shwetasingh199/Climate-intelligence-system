import pandas as pd

def preprocess(df):

    print("DEBUG COLUMNS:", df.columns)

    # SAFETY CHECKS
    if 'date' not in df.columns:
        raise Exception(f"Missing 'date' column. Found: {df.columns}")

    if 'temperature' not in df.columns:
        raise Exception(f"Missing 'temperature' column. Found: {df.columns}")

    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    df = df.dropna(subset=['date', 'temperature'])

    df = df.sort_values('date')

    return df