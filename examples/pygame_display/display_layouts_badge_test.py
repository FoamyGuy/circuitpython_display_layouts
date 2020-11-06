from display_layouts.absolute_layout import AbsoluteLayout
from blinka_displayio_pygamedisplay import PyGameDisplay
display = PyGameDisplay(width=800, height=600)
f = open("../layouts/badge_test.json", "r")
layout_str = f.read()
f.close()
main_layout = AbsoluteLayout(display, layout_str)

display.show(main_layout.view)
main_layout.sub_view_by_id("name_lbl").label.text = "Blinka"
main_layout.sub_view_by_id("name_lbl").update_position()

while display.running:
    pass