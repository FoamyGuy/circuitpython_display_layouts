from adafruit_display_text import label
import terminalio
from adafruit_bitmap_font import bitmap_font
import displayio
from display_layouts.layout_exceptions import MissingTypeError, IncorrectTypeError, MissingRequiredAttributesError
from display_layouts.views.view import View

REQUIRED_ATTRIBUTES = []


class LabelView(View):
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

            _line_spacing = 1.25
            if "line_spacing" in layout_json["attributes"]:
                _line_spacing = layout_json["attributes"]["line_spacing"]


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

            self._scale = 1
            if "scale" in layout_json["attributes"]:
                self._scale = int(layout_json["attributes"]["scale"])

            self.label = label.Label(
                _font, text=_text, color=_color,
                max_glyphs=_max_glyphs,
                background_color=_background_color,
                line_spacing=_line_spacing,
                background_tight=_background_tight,
                padding_bottom=_padding_bottom,
                padding_left=_padding_left,
                padding_right=_padding_right,
                padding_top=_padding_top, scale=self._scale
            )

            self.update_position()

            if "anchor_point" in layout_json["attributes"]:
                point = layout_json["attributes"]["anchor_point"]
                self.label.anchor_point = (point[0], point[1])

            if "anchored_position" in layout_json["attributes"]:
                pos = layout_json["attributes"]["anchored_position"]
                self.label.anchored_position = (self.keyword_compiler(pos[0]), self.keyword_compiler(pos[1]))
        else:
            #default attributes
            pass
    def update_position(self):
        layout_json = self.json
        print(self.label.bounding_box)
        _width = self.label.bounding_box[2]
        _height = self.label.bounding_box[3]
        print((_width,_height))
        _x = 0
        if "x" in layout_json["attributes"]:
            _x = self.keyword_compiler(layout_json["attributes"]["x"], {"WIDTH":_width*self._scale, "HEIGHT": _height*self._scale})
            self.label.x = _x
        _y = 0
        if "y" in layout_json["attributes"]:
            _y = self.keyword_compiler(layout_json["attributes"]["y"], {"WIDTH":_width*self._scale, "HEIGHT": _height*self._scale})
            self.label.y = _y