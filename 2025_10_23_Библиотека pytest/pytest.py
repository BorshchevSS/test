
import pytest

add = lambda a, b: a+b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


