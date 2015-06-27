import time
from PIL import Image, ImageDraw, ImageFont
from rgbmatrix import Adafruit_RGBmatrix
from weather import weather_info
from bus import bus_info


CHANGE_INTERVAL = 5
WEATHER_INTERVAL = 300


def timestamp():
    return int(time.time())


class InfoMatrix(object):

    def __init__(self):
        self._matrix = Adafruit_RGBmatrix(32, 1)
        self._font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", 14)

    @staticmethod
    def _image_draw():
        image = Image.new('RGB', (32, 32), 'black')
        draw = ImageDraw.Draw(image)
        return image, draw

    def update_weather(self, temp, percip):

        image, draw = self._image_draw()
        draw.text(
            (1, 0),
            '{0} F'.format(int(round(temp))),
            (255, 0, 0),
            font=self._font)
        draw.text(
            (1, 13),
            percip,
            (255, 0, 0),
            font=self._font)
        self._matrix.Clear()
        self._matrix.SetImage(image.im.id, 0, 0)

    def write_bus(self):
        image, draw = self._image_draw()
        draw.text((0, 0), 'Bus', (255, 0, 0), font=self._font)


def main():
    matrix = InfoMatrix()
    last_weather_reading = timestamp()
    weather = weather_info()
    print(weather)
    while True:
        if timestamp() - last_weather_reading >= WEATHER_INTERVAL:
            print("Updating weather")
            weather = weather_info()
            print(weather)
            last_weather_reading = timestamp()
        matrix.update_weather(weather['temperature'], weather['precipType'])
        time.sleep(CHANGE_INTERVAL)

        matrix.write_bus()
        time.sleep(CHANGE_INTERVAL)


if __name__ == '__main__':
    main()
