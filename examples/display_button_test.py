import board
import displayio
from display_layouts.absolute_layout import AbsoluteLayout
import adafruit_touchscreen
import adafruit_ili9341

# Release any resources currently in use for the displays
displayio.release_displays()

spi = board.SPI()
tft_cs = board.CE0
tft_dc = board.D25

display_bus = displayio.FourWire(
    spi, command=tft_dc, chip_select=tft_cs, reset=board.D24
)
display = adafruit_ili9341.ILI9341(display_bus, width=320, height=240)

# Setup touchscreen (PyPortal)
ts = adafruit_touchscreen.Touchscreen(
    board.TOUCH_XL,
    board.TOUCH_XR,
    board.TOUCH_YD,
    board.TOUCH_YU,
    calibration=((5200, 59000), (5800, 57000)),
    size=(320, 240),
)

f = open("layouts/button_test.json", "r")
layout_str = f.read()
f.close()
main_layout = AbsoluteLayout(display, layout_str)

display.show(main_layout.view)

_button = main_layout.sub_view_by_id("main_btn").button

display.save_screenshot("/home/pi/display_layouts/examples/screenshots/button_test.png")

# Loop and look for touches
while True:
    p = ts.touch_point
    if p:
        if _button.contains(p):
            _button.selected = True
    else:
        _button.selected = False