from PIL import Image, ImageDraw, ImageFont
from rgbmatrix import Adafruit_RGBmatrix


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
