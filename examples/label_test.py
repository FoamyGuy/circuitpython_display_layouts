import board
import terminalio
from adafruit_display_text import label
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

text = "Hello world"
text_area = label.Label(terminalio.FONT, text=text)
text_area.x = 10
text_area.y = 10
display.show(text_area)
print("showing")
while True:
    pass