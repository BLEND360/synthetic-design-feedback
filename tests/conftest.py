import pytest

from tests import TEST_API_KEY


@pytest.fixture(autouse=True)
def _set_api_key(monkeypatch):
    """Set API_KEY env var and patch the settings object for all tests.

    The env var is set for any code that reads os.environ directly. The settings
    object is also patched because pydantic-settings creates it at module load time,
    so env var changes after import won't affect it.
    """
    monkeypatch.setenv("API_KEY", TEST_API_KEY)

    # Patch the already-instantiated settings object so middleware sees the test key
    from api.config import settings

    monkeypatch.setattr(settings, "api_key", TEST_API_KEY)
