import displayio
from adafruit_display_shapes.sparkline import Sparkline

from display_layouts.layout_exceptions import MissingTypeError, IncorrectTypeError, MissingRequiredAttributesError, MissingAttributesError
from display_layouts.views.view import View

REQUIRED_ATTRIBUTES = ["x", "y", "height", "width"]


class SparkLineView(View):
    def __init__(self, display, layout_json):
        self.json = layout_json
        if "view_type" not in layout_json:
            raise MissingTypeError
        if layout_json["view_type"] != "SparkLine":
            raise IncorrectTypeError(
                "view_type '{}' does not match Layout Class 'SparkLine'".format(layout_json["view_type"])
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
                _outline = int(layout_json["attributes"]["color"], 16)

            _width = 0
            if "width" in layout_json["attributes"]:
                _width = self.keyword_compiler(layout_json["attributes"]["width"])

            _height = 0
            if "height" in layout_json["attributes"]:
                _height = self.keyword_compiler(layout_json["attributes"]["height"])

            _y_min = None
            if "y_min" in layout_json["attributes"]:
                _y_min = self.keyword_compiler(layout_json["attributes"]["y_min"])

            _x_min = None
            if "x_min" in layout_json["attributes"]:
                _x_min = self.keyword_compiler(layout_json["attributes"]["x_min"])

            _max_items = 10
            if "max_items" in layout_json["attributes"]:
                _max_items = self.keyword_compiler(layout_json["attributes"]["max_items"])

            _x = 0
            if "x" in layout_json["attributes"]:
                _x = self.keyword_compiler(layout_json["attributes"]["x"], {"WIDTH":_width, "HEIGHT": _height})

            _y = 0
            if "y" in layout_json["attributes"]:
                _y = self.keyword_compiler(layout_json["attributes"]["y"], {"WIDTH":_width, "HEIGHT": _height})

            _points = None
            if "points" in layout_json["attributes"]:
                _points = layout_json["attributes"]["points"]

            self.sparkline = Sparkline(
                _width,
                _height,
                _max_items,
                y_min=_y_min,
                y_max=_x_min,
                x=_x,
                y=_y,
                color=_color
            )

            if _points != None:
                for _point in _points:
                    self.sparkline.add_value(_point)

            self.view = self.sparkline
        else:
            raise MissingAttributesError()
