"""
This examples shows the use color and background_color
"""
import time
import board
import displayio


# from adafruit_st7789 import ST7789
from adafruit_ili9341 import ILI9341
from adafruit_bitmap_font import bitmap_font
from adafruit_display_text import label

#  Setup the SPI display

print("Starting the display...")  # goes to serial only
displayio.release_displays()


spi = board.SPI()
tft_cs = board.D9  # arbitrary, pin not used
tft_dc = board.D10
tft_backlight = board.D12
tft_reset = board.D11

while not spi.try_lock():
    spi.configure(baudrate=32000000)
spi.unlock()

display_bus = displayio.FourWire(
    spi,
    command=tft_dc,
    chip_select=tft_cs,
    reset=tft_reset,
    baudrate=32000000,
    polarity=1,
    phase=1,
)

print("spi.frequency: {}".format(spi.frequency))

DISPLAY_WIDTH = 320
DISPLAY_HEIGHT = 240

# display = ST7789(display_bus, width=240, height=240, rotation=0, rowstart=80, colstart=0)
display = ILI9341(
    display_bus,
    width=DISPLAY_WIDTH,
    height=DISPLAY_HEIGHT,
    rotation=180,
    auto_refresh=True,
)

display.show(None)

# font=terminalio.FONT # this is the Builtin fixed dimension font

font = bitmap_font.load_font("fonts/Helvetica-Bold-16.bdf")


text = []
text.append("none")  # no ascenders or descenders
text.append("pop quops")  # only descenders
text.append("MONSTERs are tall")  # only ascenders
text.append("MONSTERs ate pop quops")  # both ascenders and descenders
text.append("MONSTER quops\nnewline quops")  # with newline

display.auto_refresh = True
myGroup = displayio.Group(max_size=6)
display.show(myGroup)

text_area = []
myPadding = 4

for i, thisText in enumerate(text):
    text_area.append(
        label.Label(
            font,
            text=thisText,
            color=0xFFFFFF,
            background_color=None,
            background_tight=False,
            padding_top=myPadding,
            padding_bottom=myPadding,
            padding_left=myPadding,
            padding_right=myPadding,
        )
    )

    this_x = 10
    this_y = 10 + i * 40
    text_area[i].x = 10
    text_area[i].y = 3 + i * 50
    text_area[i].anchor_point = (0, 0)
    text_area[i].anchored_position = (this_x, this_y)
    myGroup.append(text_area[i])

print("background color is {}".format(text_area[0].background_color))


while True:
    time.sleep(2)
    text_area[0].text = "text"  # change some text in an existing text box
    # Note: changed text must fit within existing number of characters
    # when the Label was created

    for area in text_area:
        area.background_color = 0xFF0000
    print("background color is {:06x}".format(text_area[0].background_color))
    time.sleep(2)
    for area in text_area:
        area.background_color = 0x000088
    print("background color is {:06x}".format(text_area[0].background_color))
    time.sleep(2)
    for area in text_area:
        area.background_color = 0x00FF00
    print("background color is {:06x}".format(text_area[0].background_color))
    time.sleep(2)
    for area in text_area:
        area.background_color = 0xFF0000
    print("background color is {:06x}".format(text_area[0].background_color))
    time.sleep(2)
    for area in text_area:
        area.background_color = None
    print("background color is {}".format(text_area[0].background_color))
