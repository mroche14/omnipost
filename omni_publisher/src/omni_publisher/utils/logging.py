from __future__ import annotations

import logging


def setup_logging(level: str = "INFO") -> None:
    logging.basicConfig(level=level)
