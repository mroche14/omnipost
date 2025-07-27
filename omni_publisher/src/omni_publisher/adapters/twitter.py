from __future__ import annotations

from typing import Any, Dict

from omni_publisher.core.models import UnifiedPost

from .base import BasePlatformAdapter


class TwitterAdapter(BasePlatformAdapter):
    CAPABILITIES = {"text", "image"}
    NAME = "twitter"
    DOCS_URL = "https://developer.twitter.com/en/docs"

    def publish(self, post: UnifiedPost, *, commit: bool = False) -> Dict[str, Any]:
        payload = {"text": post.content}
        if commit:
            # In real implementation, call integration layer here
            return {"status": "posted", "payload": payload}
        return payload
