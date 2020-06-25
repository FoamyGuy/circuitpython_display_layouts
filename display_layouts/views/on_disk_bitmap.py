import displayio
import adafruit_imageload

from display_layouts.layout_exceptions import MissingTypeError, IncorrectTypeError, MissingRequiredAttributesError
from display_layouts.views.view import View

REQUIRED_ATTRIBUTES = []


class OnDiskBitmapView(View):

    def __init__(self, display, layout_json):
        self.json = layout_json
        if "view_type" not in layout_json:
            raise MissingTypeError
        if layout_json["view_type"] != "OnDiskBitmap":
            raise IncorrectTypeError(
                "view_type '{}' does not match Layout Class 'Image'".format(layout_json["view_type"])
            )
        self._display = display
        if "attributes" in layout_json:
            _missing_attrs = []
            for attribute in REQUIRED_ATTRIBUTES:
                if attribute not in layout_json:
                    _missing_attrs.append(attribute)
            if len(_missing_attrs) > 0:
                raise MissingRequiredAttributesError("Missing required attributes: {}".format(_missing_attrs))

            _image_filepath = None
            if "image_file" in layout_json["attributes"]:
                _image_filepath = layout_json["attributes"]["image_file"]

            _background_color = None
            if "background_color" in layout_json["attributes"]:
                _background_color = int(layout_json["attributes"]["background_color"], 16)

            _x = 0
            if "x" in layout_json["attributes"]:
                _x = self.keyword_compiler(layout_json["attributes"]["x"])

            _y = 0
            if "y" in layout_json["attributes"]:
                _y = self.keyword_compiler(layout_json["attributes"]["y"])

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

            _padding = 0
            if "padding" in layout_json["attributes"]:
                _padding= int(layout_json["attributes"]["padding"])

            f = open(_image_filepath, "rb")
            odb = displayio.OnDiskBitmap(f)

            odb_grid = displayio.TileGrid(odb, pixel_shader=displayio.ColorConverter())
            group = displayio.Group()
            odb_grid.x = _padding // 2
            odb_grid.y = _padding // 2
            group.x = _x
            group.y = _y
            if _padding and _background_color:
                # Draw a green background
                bg_bitmap = displayio.Bitmap(odb.width + _padding, odb.height + _padding, 1)
                bg_palette = displayio.Palette(1)
                bg_palette[0] = _background_color

                bg_sprite = displayio.TileGrid(bg_bitmap, pixel_shader=bg_palette, x=0, y=0)
                group.append(bg_sprite)

            group.append(odb_grid)
            self.view = group

            if "anchor_point" in layout_json["attributes"]:
                point = layout_json["attributes"]["anchor_point"]
                self.view.anchor_point = (point[0], point[1])

            if "anchored_position" in layout_json["attributes"]:
                pos = layout_json["attributes"]["anchored_position"]
                self.view.anchored_position = (self.keyword_compiler(pos[0]), self.keyword_compiler(pos[1]))
        else:
            #default attributes
            pass