from statsmodels.tsa.arima.model import ARIMA

def forecast(df):
    model = ARIMA(df['temperature'], order=(2,1,2))
    model_fit = model.fit()

    return model_fit.forecast(steps=30)