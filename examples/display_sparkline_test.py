import random
import time

import board
import displayio
from display_layouts.absolute_layout import AbsoluteLayout

display = board.DISPLAY

f = open("layouts/sparkline_test.json", "r")
layout_str = f.read()
f.close()
main_layout = AbsoluteLayout(display, layout_str)

display.show(main_layout.view)

_sparkline = main_layout.sub_view_by_id("main_sparkline").sparkline

# Loop and look for touches
while True:
    # turn off the auto_refresh of the display while modifying the sparkline
    display.auto_refresh = False

    # add_value: add a new value to a sparkline
    # Note: The y-range for mySparkline1 is set to 0 to 10, so all these random
    # values (between 0 and 10) will fit within the visible range of this sparkline
    _sparkline.add_value(random.uniform(0, 10))

    # turn the display auto_refresh back on
    display.auto_refresh = True

    # The display seems to be less jittery if a small sleep time is provided
    # You can adjust this to see if it has any effect
    time.sleep(0.01)