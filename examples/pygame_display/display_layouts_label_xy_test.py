from display_layouts.absolute_layout import AbsoluteLayout
from blinka_displayio_pygamedisplay import PyGameDisplay
import os
os.chdir("..")
display = PyGameDisplay(width=800, height=600)
f = open("layouts/label_xy_test.json", "r")
layout_str = f.read()
f.close()
main_layout = AbsoluteLayout(display, layout_str)

display.show(main_layout.view)

#main_layout.sub_view_by_index(0).label.text = "Changed Text\nBy Index"
main_layout.sub_view_by_id("main_lbl").label.text = "Changed\nText By Id"
main_layout.sub_view_by_id("main_lbl").update_position()
while display.running:
    pass