class MissingRequiredAttributesError(ValueError):
    def __init__(self, message="json layout is missing required attribute."):
        self.message = message
        super().__init__(self.message)

class MissingAttributesError(ValueError):
    def __init__(self, message="json layout is missing attributes."):
        self.message = message
        super().__init__(self.message)

class MissingSubViewsError(ValueError):
    def __init__(self, message="json layout is missing sub_views."):
        self.message = message
        super().__init__(self.message)

class MissingTypeError(ValueError):
    def __init__(self, message="view_type missing from json layout."):
        self.message = message
        super().__init__(self.message)

class IncorrectTypeError(Exception):
    def __init__(self, message="view_type does not match Layout Class."):
        self.message = message
        super().__init__(self.message)
