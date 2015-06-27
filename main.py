import time
from info_matrix import InfoMatrix
from weather import weather_info
from bus import bus_info


CHANGE_INTERVAL = 5
WEATHER_INTERVAL = 300


def timestamp():
    return int(time.time())


def main():
    matrix = InfoMatrix()
    last_weather_reading = timestamp()
    weather = weather_info()
    while True:
        if timestamp() - last_weather_reading >= WEATHER_INTERVAL:
            weather = weather_info()
            last_weather_reading = timestamp()
        matrix.update_weather(weather['temperature'], weather.get('precipType', 'None'))
        time.sleep(CHANGE_INTERVAL)
        buses = bus_info()
        for route, predictions in buses.iteritems():
            matrix.write_bus(route, predictions)
            time.sleep(CHANGE_INTERVAL)


if __name__ == '__main__':
    main()
