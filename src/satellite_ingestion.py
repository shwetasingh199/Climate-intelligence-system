import pandas as pd

def load_satellite_data(dates):

    # Example synthetic satellite data
    sat_df = pd.DataFrame({
        "date": dates,
        "NDVI": range(len(dates)),
        "LST": range(len(dates))
    })

    # 🔥 STEP 2: LIMIT DATA SIZE (IMPORTANT FIX)
    sat_df = sat_df.sort_values("date")
    sat_df = sat_df.iloc[::10]   # take every 10th record

    return sat_df