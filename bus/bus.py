import requests
from .config import BUS_STOPS, BUSTRACKER_API_KEY, PREDICTIONS_URL


def bus_info():
    params = {
        'key': BUSTRACKER_API_KEY,
        'stpid': BUS_STOPS['56']
    }
    r = requests.get(PREDICTIONS_URL, params=params)
    return r
