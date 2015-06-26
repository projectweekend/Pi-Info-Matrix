import forecastio
from weather.config import LATITUDE, LONGITUDE, FORECAST_IO_KEY


FORECAST = forecastio.load_forecast(FORECAST_IO_KEY, LATITUDE, LONGITUDE)


def weather_info():
    # currently = FORECAST.currently()
    # return currently.d
    return 'Weather'
