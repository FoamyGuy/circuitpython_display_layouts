import board
import displayio
from display_layouts.absolute_layout import AbsoluteLayout
from adafruit_bitmapsaver import save_pixels
import time
import adafruit_ili9341

DIR = "./screenshots/"

# Release any resources currently in use for the displays
displayio.release_displays()

spi = board.SPI()
tft_cs = board.CE0
tft_dc = board.D25

display_bus = displayio.FourWire(
    spi, command=tft_dc, chip_select=tft_cs, reset=board.D24
)
display = adafruit_ili9341.ILI9341(display_bus, width=320, height=240)

board.DISPLAY = display

f = open("layouts/badge_test.json", "r")
layout_str = f.read()
f.close()
main_layout = AbsoluteLayout(board.DISPLAY, layout_str)
board.DISPLAY.show(main_layout.view)
main_layout.sub_view_by_id("name_lbl").label.text = "Blinka"
main_layout.sub_view_by_id("name_lbl").update_position()

time.sleep(2)
print('Taking Screenshot badge_test')
save_pixels('{}screenshot_badge.bmp'.format(DIR))
print('Screenshot taken badge_test')


f = open("layouts/blinka_simpletest.json", "r")
layout_str = f.read()
f.close()
main_layout = AbsoluteLayout(board.DISPLAY, layout_str)
board.DISPLAY.show(main_layout.view)
main_layout.sub_view_by_id("main_lbl").label.text = "Changed\nText By Id"

time.sleep(2)
print('Taking Screenshot simpletest')
save_pixels('{}screenshot_simpletest.bmp'.format(DIR))
print('Screenshot taken simpletest')


f = open("layouts/shapes_test.json", "r")
layout_str = f.read()
f.close()
main_layout = AbsoluteLayout(board.DISPLAY, layout_str)
board.DISPLAY.show(main_layout.view)

time.sleep(2)
print('Taking Screenshot shapes test')
save_pixels('{}screenshot_shapes_test.bmp'.format(DIR))
print('Screenshot taken shapes test')


f = open("layouts/label_xy_test.json", "r")
layout_str = f.read()
f.close()
main_layout = AbsoluteLayout(board.DISPLAY, layout_str)
board.DISPLAY.show(main_layout.view)
main_layout.sub_view_by_id("main_lbl").label.text = "Changed\nText By Id"
main_layout.sub_view_by_id("main_lbl").update_position()

time.sleep(2)
print('Taking Screenshot label_xy_test')
save_pixels('{}screenshot_label_xy_test.bmp'.format(DIR))
print('Screenshot taken label_xy_test')


f = open("layouts/button_test.json", "r")
layout_str = f.read()
f.close()
main_layout = AbsoluteLayout(board.DISPLAY, layout_str)

board.DISPLAY.show(main_layout.view)

time.sleep(2)
print('Taking Screenshot button_test')
save_pixels('{}screenshot_button_test.bmp'.format(DIR))
print('Screenshot taken button_test')

print("Finished")