import board
import displayio
from display_layouts.absolute_layout import AbsoluteLayout
import adafruit_ili9341

# Release any resources currently in use for the displays
displayio.release_displays()

spi = board.SPI()
tft_cs = board.CE0
tft_dc = board.D25

display_bus = displayio.FourWire(
    spi, command=tft_dc, chip_select=tft_cs, reset=board.D24
)
display = adafruit_ili9341.ILI9341(display_bus, width=320, height=240)

f = open("layouts/shapes_test.json", "r")
layout_str = f.read()
f.close()
main_layout = AbsoluteLayout(display, layout_str)

display.show(main_layout.view)

#main_layout.sub_view_by_index(0).label.text = "Changed Text\nBy Index"
#main_layout.sub_view_by_id("main_lbl").label.text = "Changed\nText By Id"

display.save_screenshot("/home/pi/display_layouts/examples/screenshots/simpletest.png")
while True:
    pass
