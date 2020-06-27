import board
import displayio
from display_layouts.absolute_layout import AbsoluteLayout

f = open("layouts/badge_test.json", "r")
layout_str = f.read()
f.close()
main_layout = AbsoluteLayout(board.DISPLAY, layout_str)

board.DISPLAY.show(main_layout.view)
main_layout.sub_view_by_id("name_lbl").label.text = "Blinka"
main_layout.sub_view_by_id("name_lbl").update_position()

while True:
    pass