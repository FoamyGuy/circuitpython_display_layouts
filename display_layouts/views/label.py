from adafruit_display_text import label
import terminalio
from adafruit_bitmap_font import bitmap_font
REQUIRED_ATTRIBUTES = []
class LabelView():
    def keyword_compiler(self, possible_keyword):
        if type(possible_keyword) == str:
            if "DISPLAY_WIDTH" in possible_keyword:
                if "/" in possible_keyword:
                    return self._display.width // int(possible_keyword.split("/")[1])
                elif "-" in possible_keyword:
                    return self._display.width - int(possible_keyword.split("-")[1])
                else:
                    return self._display.width

            elif "DISPLAY_HEIGHT" in possible_keyword:
                if "/" in possible_keyword:
                    return self._display.height // int(possible_keyword.split("/")[1])
                elif "-" in possible_keyword:
                    return self._display.height - int(possible_keyword.split("-")[1])
                else:
                    return self._display.height

            elif "/" in possible_keyword:
                return int(possible_keyword.split("/")[0]) // int(possible_keyword.split("/")[1])
            elif "-" in possible_keyword:
                return int(possible_keyword.split("-")[0]) - int(possible_keyword.split("-")[1])
            else:
                return possible_keyword
        else:
            return possible_keyword

    def __init__(self, display, layout_json):
        self.json = layout_json
        if "view_type" not in layout_json:
            raise MissingTypeError
        if layout_json["view_type"] != "Label":
            raise IncorrectTypeError(
                "view_type '{}' does not match Layout Class 'Label'".format(layout_json["view_type"])
            )
        self._display = display
        if "attributes" in layout_json:
            _missing_attrs = []
            for attribute in REQUIRED_ATTRIBUTES:
                if attribute not in layout_json:
                    _missing_attrs.append(attribute)
            if len(_missing_attrs) > 0:
                raise MissingRequiredAttributesError("Missing required attributes: {}".format(_missing_attrs))

            _font = terminalio.FONT
            if "font" in layout_json["attributes"]:
                _font = bitmap_font.load_font(layout_json["attributes"]["text"])

            _text = ""
            if "text" in layout_json["attributes"]:
                _text = layout_json["attributes"]["text"]

            _color = 0xFFFFFF
            if "color" in layout_json["attributes"]:
                _color = int(layout_json["attributes"]["color"], 16)

            _background_color = None
            if "background_color" in layout_json["attributes"]:
                _background_color = int(layout_json["attributes"]["background_color"], 16)

            _line_spacing = None
            if "line_spacing" in layout_json["attributes"]:
                _line_spacing = layout_json["attributes"]["line_spacing"]

            _x = 0
            if "x" in layout_json["attributes"]:
                _x = self.keyword_compiler(layout_json["attributes"]["x"])

            _y = 0
            if "y" in layout_json["attributes"]:
                _y = self.keyword_compiler(layout_json["attributes"]["y"])

            _max_glyphs = None
            if "max_glyphs" in layout_json["attributes"]:
                _max_glyphs = int(layout_json["attributes"]["max_glyphs"])

            _background_tight = False
            if "background_tight" in layout_json["attributes"]:
                _background_tight = int(layout_json["attributes"]["background_tight"])

            _padding_top = 0
            if "padding_top" in layout_json["attributes"]:
                _padding_top = int(layout_json["attributes"]["padding_top"])

            _padding_right = 0
            if "padding_right" in layout_json["attributes"]:
                _padding_right = int(layout_json["attributes"]["padding_right"])

            _padding_left = 0
            if "padding_left" in layout_json["attributes"]:
                _padding_left = int(layout_json["attributes"]["padding_left"])

            _padding_bottom = 0
            if "padding_bottom" in layout_json["attributes"]:
                _padding_bottom = int(layout_json["attributes"]["padding_bottom"])

            self.view = label.Label(
                _font, text=_text, color=_color,
                x=_x, y=_y, max_glyphs=_max_glyphs,
                background_color=_background_color,
                line_spacing=_line_spacing,
                background_tight=_background_tight,
                padding_bottom=_padding_bottom,
                padding_left=_padding_left,
                padding_right=_padding_right,
                padding_top=_padding_top
            )

            if "anchor_point" in layout_json["attributes"]:
                point = layout_json["attributes"]["anchor_point"]
                self.view.anchor_point = (point[0], point[1])

            if "anchored_position" in layout_json["attributes"]:
                pos = layout_json["attributes"]["anchored_position"]
                self.view.anchored_position = (self.keyword_compiler(pos[0]), self.keyword_compiler(pos[1]))
        else:
            #default attributes
            pass