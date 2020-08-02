import displayio
from adafruit_display_shapes.polygon import Polygon

from display_layouts.layout_exceptions import MissingTypeError, IncorrectTypeError, MissingRequiredAttributesError, MissingAttributesError
from display_layouts.views.view import View

REQUIRED_ATTRIBUTES = ["points"]


class PolygonView(View):
    def __init__(self, display, layout_json):
        self.json = layout_json
        if "view_type" not in layout_json:
            raise MissingTypeError
        if layout_json["view_type"] != "Polygon":
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
            _outline = 0xFFFFFF

            if "outline" in layout_json["attributes"]:
                _outline = int(layout_json["attributes"]["outline"], 16)

            _points = []
            if "points" in layout_json["attributes"]:
                for _point in layout_json["attributes"]["points"]:
                    _points.append((self.keyword_compiler(_point[0]),self.keyword_compiler(_point[1])))

            self.polygon = Polygon(_points, outline=_outline)
            self.view = self.polygon
        else:
            raise MissingAttributesError()
