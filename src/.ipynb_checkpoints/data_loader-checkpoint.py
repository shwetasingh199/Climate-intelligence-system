import pandas as pd

def load_data():
    df = pd.read_csv("data/climate.csv")

    # rename date column
    if 'dt' in df.columns:
        df.rename(columns={'dt': 'date'}, inplace=True)

    # rename temperature column (IMPORTANT FIX)
    if 'LandAverageTemperature' in df.columns:
        df.rename(columns={'LandAverageTemperature': 'temperature'}, inplace=True)

    elif 'AverageTemperature' in df.columns:
        df.rename(columns={'AverageTemperature': 'temperature'}, inplace=True)

    return df