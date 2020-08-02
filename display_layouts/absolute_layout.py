import json
import displayio
from display_layouts.layout_exceptions import MissingTypeError, IncorrectTypeError, MissingSubViewsError
class AbsoluteLayout:
    def __init__(self, display, layout_json):
        self.layout_json_obj = json.loads(layout_json)

        self._display = display
        self._sub_views = []
        self._sub_views_id_to_index = {}
        if "view_type" not in self.layout_json_obj:
            raise MissingTypeError
        if self.layout_json_obj["view_type"] != "AbsoluteLayout":
            raise IncorrectTypeError(
                "view_type '{}' does not match Layout Class 'AbsoluteLayout'".format(self.layout_json_obj["view_type"])
            )
        if "sub_views" not in self.layout_json_obj:
            raise MissingSubViewsError

        self.view = self._build_group_from_layout_json()

    def sub_view_by_index(self, index):
        return self._sub_views[index]

    def sub_view_by_id(self, searching_id):
        return self.sub_view_by_index(self._sub_views_id_to_index[searching_id])


    def _build_group_from_layout_json(self):

        _imports_needed_dict = {}
        for view in self.layout_json_obj['sub_views']:
            _imports_needed_dict[view['view_type']] = ""
        #print(_imports_needed_dict)
        for view_type in _imports_needed_dict.keys():
            if view_type == "Line":
                from display_layouts.views.line import LineView
            if view_type == "RoundRect":
                from display_layouts.views.roundrect import RoundRectView
            if view_type == "Rect":
                from display_layouts.views.rect import RectView
            if view_type == "Triangle":
                from display_layouts.views.triangle import TriangleView
            if view_type == "SparkLine":
                from display_layouts.views.sparkline import SparkLineView
            if view_type == "Button":
                from display_layouts.views.button import ButtonView
            if view_type == "Circle":
                from display_layouts.views.circle import CircleView
            if view_type == "OnDiskBitmap":
                from display_layouts.views.on_disk_bitmap import OnDiskBitmapView
            if view_type == "Polygon":
                from display_layouts.views.polygon import PolygonView
            if view_type == "Image":
                from display_layouts.views.image import ImageView
            if view_type == "Label":
                from display_layouts.views.label import LabelView


        layout_group = displayio.Group(max_size=len(self.layout_json_obj["sub_views"]))

        for index, view in enumerate(self.layout_json_obj["sub_views"]):
            if "view_type" not in view:
                raise MissingTypeError("missing view_type on: {}".format(view))
            if "id" in view:
                self._sub_views_id_to_index[view["id"]] = index
            if view["view_type"] == "Label":
                lbl_view = LabelView(self._display, view)
                self._sub_views.append(lbl_view)
                layout_group.append(lbl_view.label)
            if view["view_type"] == "Image":
                img_view = ImageView(self._display, view)
                self._sub_views.append(img_view)
                layout_group.append(img_view.image)
            if view["view_type"] == "OnDiskBitmap":
                odb_view = OnDiskBitmapView(self._display, view)
                self._sub_views.append(odb_view)
                layout_group.append(odb_view.on_disk_bitmap)
            if view["view_type"] == "Line":
                line_view = LineView(self._display, view)
                self._sub_views.append(line_view)
                layout_group.append(line_view.line)
            if view["view_type"] == "Polygon":
                polygon_view = PolygonView(self._display, view)
                self._sub_views.append(polygon_view)
                layout_group.append(polygon_view.polygon)
            if view["view_type"] == "Rect":
                rect_view = RectView(self._display, view)
                self._sub_views.append(rect_view)
                layout_group.append(rect_view.rect)
            if view["view_type"] == "RoundRect":
                roundrect_view = RoundRectView(self._display, view)
                self._sub_views.append(roundrect_view)
                layout_group.append(roundrect_view.roundrect)
            if view["view_type"] == "Circle":
                circle_view = CircleView(self._display, view)
                self._sub_views.append(circle_view)
                layout_group.append(circle_view.circle)
            if view["view_type"] == "Triangle":
                triangle_view = TriangleView(self._display, view)
                self._sub_views.append(triangle_view)
                layout_group.append(triangle_view.triangle)
            if view["view_type"] == "Button":
                button_view = ButtonView(self._display, view)
                self._sub_views.append(button_view)
                layout_group.append(button_view.button.group)
            if view["view_type"] == "SparkLine":
                sparkline_view = SparkLineView(self._display, view)
                self._sub_views.append(sparkline_view)
                layout_group.append(sparkline_view.sparkline)
        return layout_group