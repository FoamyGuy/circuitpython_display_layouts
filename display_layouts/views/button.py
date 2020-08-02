import displayio
import terminalio
from adafruit_button import Button
from display_layouts.layout_exceptions import MissingTypeError, IncorrectTypeError, MissingRequiredAttributesError, \
    MissingAttributesError, InvalidAttributeValue
from display_layouts.views.view import View

REQUIRED_ATTRIBUTES = ["x", "y", "height", "width"]


class ButtonView(View):
    def __init__(self, display, layout_json):
        self.json = layout_json
        if "view_type" not in layout_json:
            raise MissingTypeError
        if layout_json["view_type"] != "Button":
            raise IncorrectTypeError(
                "view_type '{}' does not match Layout Class 'Button'".format(layout_json["view_type"])
            )
        self._display = display
        if "attributes" in layout_json:
            _missing_attrs = []
            for attribute in REQUIRED_ATTRIBUTES:
                if attribute not in layout_json['attributes']:
                    _missing_attrs.append(attribute)
            if len(_missing_attrs) > 0:
                raise MissingRequiredAttributesError("Missing required attributes: {}".format(_missing_attrs))

            _outline = 0xFFFFFF
            if "outline_color" in layout_json["attributes"]:
                _outline = int(layout_json["attributes"]["outline_color"], 16)

            _fill = 0x444444
            if "fill_color" in layout_json["attributes"]:
                _fill = int(layout_json["attributes"]["fill_color"], 16)

            _label_color = 0xFFFFFF
            if "label_color" in layout_json["attributes"]:
                _label_color = int(layout_json["attributes"]["label_color"], 16)

            _style = Button.ROUNDRECT
            if "style" in layout_json["attributes"]:
                _styles = {
                    "RECT": Button.RECT,
                    "ROUNDRECT": Button.ROUNDRECT,
                    "SHADOWRECT": Button.SHADOWRECT,
                    "SHADOWROUNDRECT": Button.SHADOWROUNDRECT
                }
                if layout_json["attributes"]["style"] in _styles.keys():
                    _style = _styles[layout_json["attributes"]["style"]]
                else:
                    raise InvalidAttributeValue(
                        "'{}'.\nValid values are: [{}]".format(layout_json["attributes"]["style"],
                                                               ", ".join(_styles.keys())))

            _label = ""
            if "label" in layout_json["attributes"]:
                _label = layout_json["attributes"]["label"]

            _width = 0
            if "width" in layout_json["attributes"]:
                _width = self.keyword_compiler(layout_json["attributes"]["width"])

            _height = 0
            if "height" in layout_json["attributes"]:
                _height = self.keyword_compiler(layout_json["attributes"]["height"])

            _font = terminalio.FONT
            if "font" in layout_json["attributes"]:
                _font = self.keyword_compiler(layout_json["attributes"]["font"])

            _x = 0
            if "x" in layout_json["attributes"]:
                _x = self.keyword_compiler(layout_json["attributes"]["x"], {"WIDTH": _width, "HEIGHT": _height})

            _y = 0
            if "y" in layout_json["attributes"]:
                _y = self.keyword_compiler(layout_json["attributes"]["y"], {"WIDTH": _width, "HEIGHT": _height})

            print(_label)
            self.button = Button(
                x=_x, y=_y, width=_width, height=_height, style=_style,
                fill_color=_fill, outline_color=_outline, label=_label,
                label_color=_label_color, label_font=_font
            )
            self.view = self.button

        else:
            raise MissingAttributesError()