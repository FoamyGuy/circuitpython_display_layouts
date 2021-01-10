import json
import displayio
from display_layouts.layout_exceptions import MissingTypeError, IncorrectTypeError, MissingSubViewsError
class LinearLayout:
    def __init__(self, display, layout_json, portrait_orientation=True):
        self.layout_json_obj = json.loads(layout_json)
        self.portrait_orientation = portrait_orientation
        self._view_type_dict = {}
        self._display = display
        self._sub_views = []
        self._sub_views_id_to_index = {}
        if "view_type" not in self.layout_json_obj:
            raise MissingTypeError
        if self.layout_json_obj["view_type"] != "LinearLayout":
            raise IncorrectTypeError(
                "view_type '{}' does not match Layout Class 'LinearLayout'".format(self.layout_json_obj["view_type"])
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
            if view_type == "BitmapLabel":
                from display_layouts.views.bitmap_label import LabelView
                self._view_type_dict[view_type] = LabelView

        layout_group = displayio.Group(max_size=len(self.layout_json_obj["sub_views"]))

        self._prev_view_end = 0
        for index, view in enumerate(self.layout_json_obj["sub_views"]):
            if "view_type" not in view:
                raise MissingTypeError("missing view_type on: {}".format(view))
            if "id" in view:
                self._sub_views_id_to_index[view["id"]] = index
            if view["view_type"] != "Label":
                view_layout = self._view_type_dict[view["view_type"]](self._display, view)
                self._sub_views.append(view_layout)
                if self.portrait_orientation:
                    view_layout.view.y = self._prev_view_end + view_layout.view.y
                    try:
                        self._prev_view_end = view_layout.view.y + view_layout.view.height
                    except AttributeError as e:
                        print(e)
                        try:
                            self._prev_view_end = view_layout.view.y + view_layout.view._height
                        except AttributeError as e:
                            print(e)
                            self._prev_view_end = view_layout.view.y + view_layout.height
                else:
                    view_layout.view.x = self._prev_view_end
                    self._prev_view_end = view_layout.view.x + view_layout.view.width

                layout_group.append(view_layout.view)
            if view["view_type"] == "Label":
                label_view = self._view_type_dict[view["view_type"]](self._display, view)
                self._sub_views.append(label_view)
                if self.portrait_orientation:
                    label_view.view.anchor_point = (0,0)
                    print("before {}".format(self._prev_view_end))
                    print("y before {}".format(label_view.view.y))
                    print("setting y to: {}".format(self._prev_view_end + label_view.view.y))
                    label_view.view.anchored_position = (label_view.view.x, self._prev_view_end + label_view.view.y)
                    self._prev_view_end = label_view.view.y + label_view.view.height
                    print("after {}".format(self._prev_view_end))
                else:
                    label_view.view.x = self._prev_view_end
                    self._prev_view_end = view_layout.view.x + view_layout.view.width
                layout_group.append(label_view.view)

        return layout_group