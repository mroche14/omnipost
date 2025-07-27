from __future__ import annotations

from importlib.metadata import entry_points
from typing import Dict, Type

from omni_publisher.adapters.base import BasePlatformAdapter


class AdapterRegistry:
    """Discover and store available platform adapters."""

    def __init__(self) -> None:
        self._adapters: Dict[str, Type[BasePlatformAdapter]] = {}
        self.discover()

    def discover(self) -> None:
        eps = entry_points(group="omni_publisher.adapters")
        for ep in eps:
            adapter_cls = ep.load()
            self._adapters[adapter_cls.NAME] = adapter_cls

    def get(self, name: str) -> Type[BasePlatformAdapter]:
        return self._adapters[name]


registry = AdapterRegistry()
