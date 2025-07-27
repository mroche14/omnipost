from omni_publisher.adapters.twitter import TwitterAdapter
from omni_publisher.core.models import UnifiedPost


def test_dry_run():
    adapter = TwitterAdapter(credentials={})
    post = UnifiedPost(content="integration")
    payload = adapter.publish(post, commit=False)
    assert payload["text"] == "integration"
