import pytest
from src.interview.exercise import find_first_neighbors


def test_neighbors_target_has_both_neighbors():
    test_sample = [43, 67, 5, 23, 87]
    neighbors = find_first_neighbors(test_sample, 5)
    assert neighbors == [67, 23]


def test_neighbors_target_with_only_right_neighbor():
    test_sample = [11, 58, 99, 14]
    neighbors = find_first_neighbors(test_sample, 11)
    assert neighbors == [58]


def test_neighbors_target_with_only_left_neighbor():
    test_sample = [11, 58, 99, 14]
    neighbors = find_first_neighbors(test_sample, 14)
    assert neighbors == [99]


def test_neighbors_target_with_no_neighbors():
    test_sample = [11]
    neighbors = find_first_neighbors(test_sample, 11)
    assert neighbors == []


def test_neighbors_target_not_present():
    test_sample = [5, 13, 88, 109, 9, 77, 11]
    with pytest.raises(ValueError) as e:
        find_first_neighbors(test_sample, 99999)

    assert '99999 is not in the list' in str(e.value)
