def moving_average(df):
    df['temp_ma'] = df['temperature'].rolling(window=30).mean()
    return df