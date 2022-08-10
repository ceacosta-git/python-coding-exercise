import pytest
from exercise import find_first_neighbors


def test_neighbors_target_has_both_neighbors():
    test_sample = [43, 67, 5, 23, 87]
    neighbors = find_first_neighbors(test_sample, 5)
    assert neighbors == [67, 23]


