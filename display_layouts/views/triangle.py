import displayio
from adafruit_display_shapes.triangle import Triangle

from display_layouts.layout_exceptions import MissingTypeError, IncorrectTypeError, MissingRequiredAttributesError, MissingAttributesError
from display_layouts.views.view import View

REQUIRED_ATTRIBUTES = ["x2", "x1", "x0", "y2", "y1", "y0"]


class TriangleView(View):
    def __init__(self, display, layout_json):
        self.json = layout_json
        if "view_type" not in layout_json:
            raise MissingTypeError
        if layout_json["view_type"] != "Triangle":
            raise IncorrectTypeError(
                "view_type '{}' does not match Layout Class 'Triangle'".format(layout_json["view_type"])
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
            if "outline" in layout_json["attributes"]:
                _outline = int(layout_json["attributes"]["outline"], 16)

            _fill = 0x000000
            if "fill" in layout_json["attributes"]:
                _fill = int(layout_json["attributes"]["fill"], 16)

            _x0 = 0
            if "x0" in layout_json["attributes"]:
                _x0 = self.keyword_compiler(layout_json["attributes"]["x0"])

            _x1 = 0
            if "x1" in layout_json["attributes"]:
                _x1 = self.keyword_compiler(layout_json["attributes"]["x1"])

            _x2 = 0
            if "x2" in layout_json["attributes"]:
                _x2 = self.keyword_compiler(layout_json["attributes"]["x2"])

            _y0 = 0
            if "y0" in layout_json["attributes"]:
                _y0 = self.keyword_compiler(layout_json["attributes"]["y0"])

            _y1 = 0
            if "y1" in layout_json["attributes"]:
                _y1 = self.keyword_compiler(layout_json["attributes"]["y1"])

            _y2 = 0
            if "y2" in layout_json["attributes"]:
                _y2 = self.keyword_compiler(layout_json["attributes"]["y2"])

            self.triangle = Triangle(_x0, _y0, _x1, _y1, _x2,_y2, fill=_fill, outline=_outline)

            self.view = self.triangle
        else:
            raise MissingAttributesError()