import forecastio
from .config import LATITUDE, LONGITUDE, FORECAST_IO_KEY


def weather_info():
    forecast = forecastio.load_forecast(FORECAST_IO_KEY, LATITUDE, LONGITUDE)
    currently = forecast.currently()
    return currently.d
