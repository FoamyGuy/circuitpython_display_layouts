import board
import displayio
from display_layouts.absolute_layout import AbsoluteLayout

f = open("layouts/simpletest.json", "r")
layout_str = f.read()
f.close()
main_layout = AbsoluteLayout(board.DISPLAY, layout_str)

board.DISPLAY.show(main_layout.view)

#main_layout.sub_view_by_index(0).view.text = "Changed Text\nBy Index"
main_layout.sub_view_by_id("main_lbl").view.text = "Changed\nText By Id"

while True:
    pass