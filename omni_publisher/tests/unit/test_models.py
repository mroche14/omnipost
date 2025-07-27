from omni_publisher.core.models import MediaItem, MediaType, UnifiedPost


def test_unified_post():
    post = UnifiedPost(content="hello")
    assert post.content == "hello"
    assert post.media == []


def test_media_item_enum():
    item = MediaItem(url="http://x", media_type="image")
    assert item.type == MediaType.IMAGE
