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


target_not_present_samples = \
    [([5, 13, 88], 9999),  # numbers is non-empty
     ([], 11),  # numbers is empty
     (None, 33)]  # numbers is none


@pytest.mark.parametrize("test_sample, test_target", target_not_present_samples)
def test_neighbors_target_not_present(test_sample, test_target):
    with pytest.raises(ValueError) as e:
        find_first_neighbors(test_sample, test_target)

    assert f'{test_target} is not in the list' in str(e.value)
