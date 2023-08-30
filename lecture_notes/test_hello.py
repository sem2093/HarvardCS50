from hello import hello


def test_hello():
    assert hello("David") == "hello, David"
    assert hello() == "hello, world"

# break down into multiple functions
from hello import hello


def test_default():
    assert hello() == "hello, world"


def test_argument():
    assert hello("David") == "hello, David"
