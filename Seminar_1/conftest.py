import pytest
from check_post import get_login



@pytest.fixture()
def token():
    return get_login()
