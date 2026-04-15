from src.data_loader import load_data
from src.preprocessing import preprocess
from src.eda import plot_temperature
from src.trend import moving_average
from src.anomaly import detect_anomaly
from src.forecast import forecast_temp

df = load_data("data/raw/climate.csv")
df = preprocess(df)

plot_temperature(df)

df = moving_average(df)
df = detect_anomaly(df)

forecast = forecast_temp(df)
print(forecast)