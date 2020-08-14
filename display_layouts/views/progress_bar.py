import displayio
from adafruit_progressbar import ProgressBar
from display_layouts.layout_exceptions import MissingTypeError, IncorrectTypeError, MissingRequiredAttributesError
from display_layouts.views.view import View

REQUIRED_ATTRIBUTES = []


class ProgressBarView(View):
    def __init__(self, display, layout_json):
        self.json = layout_json
        if "view_type" not in layout_json:
            raise MissingTypeError
        if layout_json["view_type"] != "ProgressBar":
            raise IncorrectTypeError(
                "view_type '{}' does not match Layout Class 'ProgressBar'".format(layout_json["view_type"])
            )
        self._display = display
        if "attributes" in layout_json:
            _missing_attrs = []
            for attribute in REQUIRED_ATTRIBUTES:
                if attribute not in layout_json:
                    _missing_attrs.append(attribute)
            if len(_missing_attrs) > 0:
                raise MissingRequiredAttributesError("Missing required attributes: {}".format(_missing_attrs))

            _bar_color = 0xFFFFFF
            if "bar_color" in layout_json["attributes"]:
                _bar_color = int(layout_json["attributes"]["bar_color"], 16)

            _outline_color = 0x000000
            if "outline_color" in layout_json["attributes"]:
                _outline_color = int(layout_json["attributes"]["outline_color"], 16)

            _progress = 0.0
            if "progress" in layout_json["attributes"]:
                _progress = layout_json["attributes"]["progress"]

            _stroke = 1
            if "stroke" in layout_json["attributes"]:
                _stroke = int(layout_json["attributes"]["stroke"])

            _width = 30
            if "width" in layout_json["attributes"]:
                _width = self.keyword_compiler(layout_json["attributes"]["width"])

            _height = 10
            if "height" in layout_json["attributes"]:
                _height = self.keyword_compiler(layout_json["attributes"]["height"])

            _x = 0
            if "x" in layout_json["attributes"]:
                _x = self.keyword_compiler(layout_json["attributes"]["x"], {"WIDTH": _width, "HEIGHT": _height})

            _y = 0
            if "y" in layout_json["attributes"]:
                _y = self.keyword_compiler(layout_json["attributes"]["y"], {"WIDTH": _width, "HEIGHT": _height})

            self.progress_bar = ProgressBar(
                _x, _y, _width, _height,
                0.0, _bar_color,
                _outline_color, _stroke
            )
            self.progress_bar.progress = _progress

            self.view = self.progress_bar
        else:
            #default attributes
            pass