from omni_publisher.adapters.twitter import TwitterAdapter
from omni_publisher.core.models import UnifiedPost


def test_twitter_publish_dry_run():
    adapter = TwitterAdapter(credentials={})
    post = UnifiedPost(content="hi")
    payload = adapter.publish(post, commit=False)
    assert payload == {"text": "hi"}
