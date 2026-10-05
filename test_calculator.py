import pytest

from calculator import add_numbers


@pytest.mark.parametrize(
    ("left", "right", "expected"),
    [(2, 2, 4), (0, 0, 0), (-2, -3, -5), (-2, 3, 1), (5, 0, 5)],
)
def test_add(left, right, expected):
    assert add_numbers(left, right) == expected
