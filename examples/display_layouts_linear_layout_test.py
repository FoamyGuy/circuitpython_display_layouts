import board
import displayio
from display_layouts.absolute_layout import AbsoluteLayout

f = open("layouts/linear_layout_test.json", "r")
layout_str = f.read()
f.close()
main_layout = AbsoluteLayout(board.DISPLAY, layout_str)

board.DISPLAY.show(main_layout.view)

while True:
    pass