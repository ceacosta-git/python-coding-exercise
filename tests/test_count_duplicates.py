import pytest
from src.interview.count_duplicates import count_duplicates


def test_count_duplicates_string_items():
    test_sample = ['foo', 'bar', 'foos', 'bars', 'foo', 'bar']
    expected_map = {"foo": 2, "bar": 2, "foos": 1, "bars": 1}
    actual_map = count_duplicates(test_sample)
    assert actual_map == expected_map


def test_count_duplicates_case_sensitive():
    test_sample = ['foo', 'bar', 'Foo', 'Bar', 'foo', 'bar']
    expected_map = {"foo": 2, "bar": 2, "Foo": 1, "Bar": 1}
    actual_map = count_duplicates(test_sample)
    assert actual_map == expected_map


def test_count_duplicates_int_items():
    test_sample = [1, 2, 1, 2, 3, 0]
    expected_map = {1: 2, 2: 2, 3: 1, 0: 1}
    actual_map = count_duplicates(test_sample)
    assert actual_map == expected_map


def test_count_duplicates_boolean_items():
    test_sample = [True, False, False, True, True]
    expected_map = {True: 3, False: 2}
    actual_map = count_duplicates(test_sample)
    assert  actual_map == expected_map


def test_count_duplicates_mixed_items():
    test_sample = ["foo", "bar", 5, "foo", 7, True, False, 5, False, None, "bars", None]
    expected_map  = {"foo": 2, "bar": 1, 5: 2, 7: 1, True: 1, False: 2, None: 2, "bars": 1}
    actual_map = count_duplicates(test_sample)
    assert actual_map == expected_map


def test_count_duplicates_empty_items():
    assert {} == count_duplicates([])


def test_count_duplicates_none_as_param():
    with pytest.raises(ValueError) as e:
        count_duplicates(None)

    assert "You must pass a non-null array" in str(e.value)

