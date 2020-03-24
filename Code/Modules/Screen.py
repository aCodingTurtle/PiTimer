import Adafruit_SSD1306 as AdaOLED
import RPi.GPIO as GPIO

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def startup():
    RST = 4
    disp = AdaOLED.SSD1306_128_64(rst=RST)
    disp.begin()

    width = disp.width
    height = disp.height
    padding = -2
    top = padding
    bottom = height - padding

    x = 0

    disp.clear()
    disp.display()

    image = Image.new('1', (width, height))
    #font = ImageFont.load_default()
    font = ImageFont.truetype('Minecraftia-Regular.ttf', 8)
    draw = ImageDraw.Draw(image)

    draw.rectangle((0,0,width,height), outline=0, fill=0)

    disp.image(image)
    disp.display()
