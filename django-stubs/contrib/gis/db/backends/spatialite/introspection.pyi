from typing import Any

from django.db.backends.sqlite3.introspection import (
    DatabaseIntrospection as DatabaseIntrospection,
)
from django.db.backends.sqlite3.introspection import (
    FlexibleFieldLookupDict as FlexibleFieldLookupDict,
)

class GeoFlexibleFieldLookupDict(FlexibleFieldLookupDict):
    base_data_types_reverse: Any = ...

class SpatiaLiteIntrospection(DatabaseIntrospection):
    data_types_reverse: Any = ...
    def get_geometry_type(self, table_name: Any, description: Any): ...
    def get_constraints(self, cursor: Any, table_name: Any): ...
