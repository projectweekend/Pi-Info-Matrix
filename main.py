import time
from PIL import Image, ImageDraw, ImageFont
from rgbmatrix import Adafruit_RGBmatrix


INTERVAL = 5


class InfoMatrix(object):

    def __init__(self):
        self._matrix = Adafruit_RGBmatrix(32, 1)
        self._font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", 12)

    def clear_and_write(self, message):
        image = Image.new('RGB', (32, 32), 'black')
        draw = ImageDraw.Draw(image)
        draw.text((0, 0), message, (255, 0, 0), font=self._font)
        self._matrix.Clear()
        self._matrix.SetImage(image.im.id, 0, 0)


def weather_info():
    return "Weather"


def bus_info():
    return "Bus"


def main():
    matrix = InfoMatrix()
    while True:
        weather = weather_info()
        matrix.clear_and_write(weather)
        time.sleep(INTERVAL)
        bus = bus_info()
        matrix.clear_and_write(bus)
        time.sleep(INTERVAL)


if __name__ == '__main__':
    main()
