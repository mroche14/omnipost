from __future__ import annotations

import abc
from typing import Any, Dict

from omni_publisher.core.models import UnifiedPost


class BasePlatformAdapter(abc.ABC):
    """Base class for platform adapters."""

    CAPABILITIES: set[str] = set()
    NAME: str = ""
    DOCS_URL: str = ""

    def __init__(self, credentials: Dict[str, Any]):
        self.credentials = credentials

    @abc.abstractmethod
    def publish(self, post: UnifiedPost, *, commit: bool = False) -> Any:
        """Publish the UnifiedPost. Return payload when commit is False."""
        raise NotImplementedError
