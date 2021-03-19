import pytest

from sandwiches import count_students


def test_count_students():
    assert count_students([1, 1, 0, 0], [0, 1, 0, 1]) == 0
    assert count_students([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]) == 3
    assert (
        count_students(
            [
                1,
                0,
                1,
                0,
                1,
                1,
                0,
                1,
                1,
                1,
                1,
                0,
                0,
                0,
                1,
                1,
                1,
                0,
                1,
                1,
                1,
                1,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
                0,
            ],
            [
                0,
                1,
                0,
                0,
                1,
                1,
                1,
                1,
                1,
                1,
                0,
                1,
                1,
                0,
                0,
                0,
                1,
                1,
                0,
                0,
                1,
                1,
                1,
                1,
                0,
                0,
                1,
                0,
                1,
                0,
            ],
        )
        == 2
    )
