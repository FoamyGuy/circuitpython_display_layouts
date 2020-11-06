import time
from display_layouts.absolute_layout import AbsoluteLayout
from blinka_displayio_pygamedisplay import PyGameDisplay
import os
os.chdir("..")
display = PyGameDisplay(width=800, height=600)

f = open("layouts/progress_bar_test.json", "r")
layout_str = f.read()
f.close()
main_layout = AbsoluteLayout(display, layout_str)

display.show(main_layout.view)

_progress = main_layout.sub_view_by_id("main_progress").view

while display.running:
    for current_progress in range(0, 101, 1):
        print("Progress: {}%".format(current_progress))
        _progress.progress = current_progress / 100  # convert to decimal
        time.sleep(0.01)
    time.sleep(0.3)
    _progress.progress = 0.0
    time.sleep(0.3)