# -*- coding: utf-8 -*-

__author__ = 'Hemanth Sana'
__email__ = 'hesa@nmbu.no'


import pytest


def median(data):
    sorted_data = sorted(data)
    num_elements = len(sorted_data)
    if num_elements == 0:
        raise ValueError
    if num_elements % 2 == 1:
        return sorted_data[num_elements // 2]
    else:
        return ((
            sorted_data[num_elements // 2 - 1] + sorted_data[num_elements // 2]
        ) / 2)


def test_median_of_single_element():
    assert median([4]) == 4


def test_median_of_even_elements():
    data = [1, 3, 5, 7]
    assert median(data) == 4


def test_median_of_odd_elements():
    data = [1, 3, 5, 7, 9]
    assert median(data) == 5


def test_median_of_ordered_elements():
    data = [1, 3, 5, 7, 9]
    assert median(data) == 5


def test_median_of_reverse_ordered_elements():
    data = [9, 7, 5, 3, 1]
    assert median(data) == 5


def test_median_of_unordered_elements():
    data = [7, 1, 3, 9, 5]
    assert median(data) == 5


def test_median_raises_value_error_on_empty_list():
    with pytest.raises(ValueError):
        median([])


def test_median_original_data_unchanged():
    data = [7, 1, 3, 9, 5]
    median(data)
    assert data == [7, 1, 3, 9, 5]


def test_median_tuples():
    data = (7, 1, 3, 9, 5)
    assert median(data) == 5
