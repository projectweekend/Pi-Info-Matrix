import os


BUS_STOPS = {
    '56': '5518'
}

BUSTRACKER_API_KEY = os.getenv('BUSTRACKER_API_KEY')
assert BUSTRACKER_API_KEY

PREDICTIONS_URL = 'http://www.ctabustracker.com/bustime/api/v1/getpredictions'
