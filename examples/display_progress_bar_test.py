import board
import time
import displayio
from display_layouts.absolute_layout import AbsoluteLayout


f = open("layouts/progress_bar_test.json", "r")
layout_str = f.read()
f.close()
main_layout = AbsoluteLayout(board.DISPLAY, layout_str)

board.DISPLAY.show(main_layout.view)

_progress = main_layout.sub_view_by_id("main_progress").view

while True:
    for current_progress in range(0, 101, 1):
        print("Progress: {}%".format(current_progress))
        _progress.progress = current_progress / 100  # convert to decimal
        time.sleep(0.01)
    time.sleep(0.3)
    _progress.progress = 0.0
    time.sleep(0.3)