from typing import Any, Optional

from django.db.models.query_utils import DeferredAttribute

class SpatialProxy(DeferredAttribute):
    def __init__(
        self, klass: Any, field: Any, load_func: Optional[Any] = ...
    ) -> None: ...
    def __get__(self, instance: Any, cls: Optional[Any] = ...): ...
    def __set__(self, instance: Any, value: Any): ...
