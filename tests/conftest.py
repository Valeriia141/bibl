import pytest


@pytest.fixture
def invalid_body():
    body = {
        "title": 123,
        "author": "ZZZZ",
        "pages": "YYY",
        "section": 25
    }
    return body


@pytest.fixture
def valid_body():
    body = {
        "title": "XXXX",
        "author": "ZZZZ",
        "pages": 13456,
        "section": 25
    }
    return body