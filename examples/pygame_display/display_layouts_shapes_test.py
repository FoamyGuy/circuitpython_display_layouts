
from display_layouts.absolute_layout import AbsoluteLayout
from blinka_displayio_pygamedisplay import PyGameDisplay
import os
os.chdir("..")
display = PyGameDisplay(width=800, height=600)
f = open("layouts/shapes_test.json", "r")
layout_str = f.read()
f.close()
main_layout = AbsoluteLayout(display, layout_str)

display.show(main_layout.view)

while display.running:
    pass