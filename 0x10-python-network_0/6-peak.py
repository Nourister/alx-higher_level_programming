#!/usr/bin/python3
"""Module that finds a peak in a list of integers"""
def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    Args:
    - list_of_integers: List of unsorted integers.

    Returns:
    - Peak element.
    """

    if not list_of_integers:
        return None

    low, high = 0, len(list_of_integers) - 1

    while low <= high:
        mid = (low + high) // 2

        # Check if mid is a peak
        if (mid == 0 or list_of_integers[mid - 1] <= list_of_integers[mid]) and \
           (mid == len(list_of_integers) - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]

        # If the element to the left of mid is greater, search in the left half
        elif mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            high = mid - 1

        # If the element to the right of mid is greater, search in the right half
        else:
            low = mid + 1

    return (None)

