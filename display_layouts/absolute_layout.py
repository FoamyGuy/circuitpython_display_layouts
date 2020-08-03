import json
import displayio
from display_layouts.layout_exceptions import MissingTypeError, IncorrectTypeError, MissingSubViewsError
class AbsoluteLayout:
    def __init__(self, display, layout_json):
        self.layout_json_obj = json.loads(layout_json)
        self._view_type_dict = {}
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
                self._view_type_dict[view_type] = LineView
            if view_type == "RoundRect":
                from display_layouts.views.roundrect import RoundRectView
                self._view_type_dict[view_type] = RoundRectView
            if view_type == "Rect":
                from display_layouts.views.rect import RectView
                self._view_type_dict[view_type] = RectView
            if view_type == "Triangle":
                from display_layouts.views.triangle import TriangleView
                self._view_type_dict[view_type] = TriangleView
            if view_type == "SparkLine":
                from display_layouts.views.sparkline import SparkLineView
                self._view_type_dict[view_type] = SparkLineView
            if view_type == "Button":
                from display_layouts.views.button import ButtonView
                self._view_type_dict[view_type] = ButtonView
            if view_type == "Circle":
                from display_layouts.views.circle import CircleView
                self._view_type_dict[view_type] = CircleView
            if view_type == "OnDiskBitmap":
                from display_layouts.views.on_disk_bitmap import OnDiskBitmapView
                self._view_type_dict[view_type] = OnDiskBitmapView
            if view_type == "Polygon":
                from display_layouts.views.polygon import PolygonView
                self._view_type_dict[view_type] = PolygonView
            if view_type == "Image":
                from display_layouts.views.image import ImageView
                self._view_type_dict[view_type] = ImageView
            if view_type == "ProgressBar":
                from display_layouts.views.progress_bar import ProgressBarView
                self._view_type_dict[view_type] = ProgressBarView
            if view_type == "Label":
                from display_layouts.views.label import LabelView
                self._view_type_dict[view_type] = LabelView

        layout_group = displayio.Group(max_size=len(self.layout_json_obj["sub_views"]))

        for index, view in enumerate(self.layout_json_obj["sub_views"]):
            if "view_type" not in view:
                raise MissingTypeError("missing view_type on: {}".format(view))
            if "id" in view:
                self._sub_views_id_to_index[view["id"]] = index
            if view["view_type"] != "Button":
                view_layout = self._view_type_dict[view["view_type"]](self._display, view)
                self._sub_views.append(view_layout)
                layout_group.append(view_layout.view)
            if view["view_type"] == "Button":
                button_view = self._view_type_dict[view["view_type"]](self._display, view)
                self._sub_views.append(button_view)
                layout_group.append(button_view.view.group)
        return layout_group
