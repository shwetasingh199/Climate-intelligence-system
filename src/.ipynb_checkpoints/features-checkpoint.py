import pandas as pd

def add_features(df):

    df = df.sort_values("date")

    # -------------------------
    # ROLLING MEAN (FIX FOR YOUR ERROR)
    # -------------------------
    df['rolling_mean'] = df['temperature'].rolling(window=12).mean()

    # -------------------------
    # EXTRA FEATURES (OPTIONAL BUT GOOD FOR PORTFOLIO)
    # -------------------------
    df['rolling_std'] = df['temperature'].rolling(window=12).std()

    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year

    return df