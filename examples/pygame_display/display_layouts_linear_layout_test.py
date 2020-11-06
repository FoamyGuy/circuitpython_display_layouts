from display_layouts.linear_layout import LinearLayout
from blinka_displayio_pygamedisplay import PyGameDisplay
import os
os.chdir("..")
display = PyGameDisplay(width=800, height=600)
f = open("layouts/linear_layout_test.json", "r")
layout_str = f.read()
f.close()
main_layout = LinearLayout(display, layout_str)

display.show(main_layout.view)

while display.running:
    pass