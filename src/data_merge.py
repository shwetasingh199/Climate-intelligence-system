import pandas as pd

def merge_data(climate_df, satellite_df):

    # ---------------------------
    # 1. CLEAN DATE COLUMN
    # ---------------------------
    climate_df['date'] = pd.to_datetime(climate_df['date'], errors='coerce')
    satellite_df['date'] = pd.to_datetime(satellite_df['date'], errors='coerce')

    climate_df = climate_df.dropna(subset=['date'])
    satellite_df = satellite_df.dropna(subset=['date'])

    # ---------------------------
    # 2. KEEP ONLY NUMERIC DATA
    # (VERY IMPORTANT FIX)
    # ---------------------------
    climate_numeric = climate_df.select_dtypes(include=['number'])
    climate_numeric['date'] = climate_df['date']

    satellite_numeric = satellite_df.select_dtypes(include=['number'])
    satellite_numeric['date'] = satellite_df['date']

    # ---------------------------
    # 3. GROUP BY DATE SAFELY
    # ---------------------------
    climate_grouped = climate_numeric.groupby('date').mean().reset_index()
    satellite_grouped = satellite_numeric.groupby('date').mean().reset_index()

    # ---------------------------
    # 4. REDUCE SIZE (PREVENT CRASH)
    # ---------------------------
    climate_grouped = climate_grouped.iloc[::5]      # downsample
    satellite_grouped = satellite_grouped.iloc[::5]   # downsample

    # ---------------------------
    # 5. SAFE MERGE
    # ---------------------------
    merged = pd.merge(climate_grouped, satellite_grouped, on="date", how="left")

    return merged