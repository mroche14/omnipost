from __future__ import annotations

import os
from typing import Any


def pull_from_env(key: str, default: Any | None = None) -> Any:
    """Retrieve environment variables with optional default."""
    return os.getenv(key, default)
