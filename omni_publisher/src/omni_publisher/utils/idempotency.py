from __future__ import annotations

import uuid


def generate_key() -> str:
    return uuid.uuid4().hex
