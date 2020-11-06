import random
import time
from display_layouts.absolute_layout import AbsoluteLayout
from blinka_displayio_pygamedisplay import PyGameDisplay
import os
os.chdir("..")
display = PyGameDisplay(width=800, height=600)

f = open("layouts/sparkline_test.json", "r")
layout_str = f.read()
f.close()
main_layout = AbsoluteLayout(display, layout_str)

display.show(main_layout.view)

_sparkline = main_layout.sub_view_by_id("main_sparkline").sparkline

# Loop and look for touches
while display.running:
    # add_value: add a new value to a sparkline
    # Note: The y-range for mySparkline1 is set to 0 to 10, so all these random
    # values (between 0 and 10) will fit within the visible range of this sparkline
    _sparkline.add_value(random.uniform(0, 10))

    # The display seems to be less jittery if a small sleep time is provided
    # You can adjust this to see if it has any effect
    time.sleep(0.05)