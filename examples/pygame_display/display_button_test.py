import board
import displayio
from display_layouts.absolute_layout import AbsoluteLayout
import adafruit_touchscreen

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
main_layout = AbsoluteLayout(board.DISPLAY, layout_str)

board.DISPLAY.show(main_layout.view)

_button = main_layout.sub_view_by_id("main_btn").button

# Loop and look for touches
while True:
    p = ts.touch_point
    if p:
        if _button.contains(p):
            _button.selected = True
    else:
        _button.selected = False