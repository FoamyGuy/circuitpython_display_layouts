import json
import displayio
from display_layouts.layout_exceptions import MissingTypeError, IncorrectTypeError, MissingSubViewsError
from display_layouts.views.label import LabelView
from display_layouts.views.image import ImageView
from display_layouts.views.on_disk_bitmap import OnDiskBitmapView

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
        layout_group = displayio.Group(max_size=len(self.layout_json_obj["sub_views"]))

        for index, view in enumerate(self.layout_json_obj["sub_views"]):
            if "view_type" not in view:
                raise MissingTypeError("missing view_type on: {}".format(view))
            if "id" in view:
                self._sub_views_id_to_index[view["id"]] = index
            if view["view_type"] == "Label":
                lbl_view = LabelView(self._display, view)
                self._sub_views.append(lbl_view)
                layout_group.append(lbl_view.view)
            if view["view_type"] == "Image":
                img_view = ImageView(self._display, view)
                self._sub_views.append(img_view)
                layout_group.append(img_view.view)
            if view["view_type"] == "OnDiskBitmap":
                odb_view = OnDiskBitmapView(self._display, view)
                self._sub_views.append(odb_view)
                layout_group.append(odb_view.view)
        return layout_group