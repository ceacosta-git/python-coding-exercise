import pytest
from exercise import find_first_neighbors


def test_neighbors_target_has_both_neighbors():
    test_sample = [43, 67, 5, 23, 87]
    neighbors = find_first_neighbors(test_sample, 5)
    assert neighbors == [67, 23]


def test_neigbhbors_target_with_only_right_neighbor():
    test_sample = [11, 58, 99, 14]
    neighbors = find_first_neighbors(test_sample, 11)
    pytest.fail("missing requirement - what to return when target is the first element in the list?")


@pytest.mark.skip
def test_neigbhbors_target_with_only_left_neighbor():
    test_sample = [11, 58, 99, 14]
    neighbors = find_first_neighbors(test_sample, 14)
    pytest.fail("missing requirement - what to return when target is the last element in the list?")
