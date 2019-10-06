# -*- coding: utf-8 -*-

__author__ = 'Hemanth Sana'
__email__ = 'hesa@nmbu.no'


def bubble_sort(sort_list):
    """
    Here we give data as input and get a sorted list as output
    """
    sorted_list = list(sort_list)
    for i in range(len(sorted_list)):
        for j in range(i, len(sorted_list)):
            if sorted_list[i] > sorted_list[j]:
                sorted_list[i], sorted_list[j] = sorted_list[j], sorted_list[i]
    return sorted_list


def test_empty():
    """Test that the sorting function works for empty list"""
    assert bubble_sort([]) == []


def test_single():
    """Test that the sorting function works for single-element list"""
    assert bubble_sort([4]) == [4]


def test_sorted_is_not_original():
    """
    Test that the sorting function returns a new object.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now sorted_data shall be a different object than data,
    not just another name for the same object.
    """
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    assert sorted_data is not data


def test_original_unchanged():
    """
    Test that sorting leaves the original data unchanged.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now data shall still contain [3, 2, 1].
    """
    data = [3, 2, 1]
    bubble_sort(data)

    assert data == [3, 2, 1]


def test_sort_sorted():
    """Test that sorting works on sorted data."""
    data = [1, 2, 3]
    sorted_data = bubble_sort(data)

    assert sorted_data == data


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data."""
    data = [5, 4, 3, 2, 1]
    sorted_data = bubble_sort(data)

    assert sorted_data == [1, 2, 3, 4, 5]


def test_sort_all_equal():
    """Test that sorting handles data with identical elements."""
    data = [4, 4, 4, 4, 4]
    sorted_data = bubble_sort(data)

    assert sorted_data == data


def test_sorting():
    """
    Test sorting for various test cases.

    This test case should test sorting of a range of data sets and
    ensure that they are sorted correctly. These could be lists of
    numbers of different length or lists of strings.
    """
    data = ['b', 'd', 'c', 'e', 'a']
    sorted_data = bubble_sort(data)

    assert sorted_data == ['a', 'b', 'c', 'd', 'e']

    data = [-52, 12, 78, 9, 176, 16]
    sorted_data = bubble_sort(data)

    assert sorted_data == [-52, 9, 12, 16, 78, 176]
