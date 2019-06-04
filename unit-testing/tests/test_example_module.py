import pytest

# Module to test
from example_package.example_module import add

# Tests' names need to start with 'test'
# Generic test
def test_add():
    assert add(1, 2) == 3

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 1, 2),
        (2, 2, 4)
    ]
)
def test_parametrized_add(a, b, expected):
    assert add(a, b) == expected

