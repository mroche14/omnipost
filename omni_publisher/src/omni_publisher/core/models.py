from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class MediaType(str, Enum):
    IMAGE = "image"
    VIDEO = "video"


class MediaItem(BaseModel):
    url: str
    type: MediaType = Field(..., alias="media_type")


class UnifiedPost(BaseModel):
    content: str
    media: List[MediaItem] = []
    scheduled_at: Optional[str] = None
