import displayio
from adafruit_display_shapes.line import Line

from display_layouts.layout_exceptions import MissingTypeError, IncorrectTypeError, MissingRequiredAttributesError, MissingAttributesError
from display_layouts.views.view import View

REQUIRED_ATTRIBUTES = ["x1", "x0", "y1", "y0"]


class LineView(View):
    def __init__(self, display, layout_json):
        self.json = layout_json
        if "view_type" not in layout_json:
            raise MissingTypeError
        if layout_json["view_type"] != "Line":
            raise IncorrectTypeError(
                "view_type '{}' does not match Layout Class 'Line'".format(layout_json["view_type"])
            )
        self._display = display
        if "attributes" in layout_json:
            _missing_attrs = []
            for attribute in REQUIRED_ATTRIBUTES:
                if attribute not in layout_json['attributes']:
                    _missing_attrs.append(attribute)
            if len(_missing_attrs) > 0:
                raise MissingRequiredAttributesError("Missing required attributes: {}".format(_missing_attrs))

            _color = 0xFFFFFF
            if "color" in layout_json["attributes"]:
                _color = int(layout_json["attributes"]["color"], 16)

            _x0 = 0
            if "x0" in layout_json["attributes"]:
                _x0 = self.keyword_compiler(layout_json["attributes"]["x0"])

            _x1 = 0
            if "x1" in layout_json["attributes"]:
                _x1 = self.keyword_compiler(layout_json["attributes"]["x1"])

            _y0 = 0
            if "y0" in layout_json["attributes"]:
                _y0 = self.keyword_compiler(layout_json["attributes"]["y0"])

            _y1 = 0
            if "y1" in layout_json["attributes"]:
                _y1 = self.keyword_compiler(layout_json["attributes"]["y1"])

            self.line = Line(_x0, _y0, _x1, _y1, color=_color)
            self.view = self.line
        else:
            raise MissingAttributesError()
