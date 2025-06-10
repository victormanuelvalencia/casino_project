# Bubble Sort algorithm for sorting elements in a JSON file by a given criteria.
# utils/data_management.py

import json
from utils.file_administration import *

def sort_elements_by(criteria, file):
    """
    Sorts elements in a JSON file using the Bubble Sort algorithm based on a specified criterion.

    This function reads a list of dictionaries from a JSON file, sorts them in ascending order
    based on the specified key (criterion), and writes the sorted list back to the same file.
    The sorting algorithm used is Bubble Sort, which is simple but not optimized for large datasets.

    Parameters:
    - criteria (str): The dictionary key to sort by (e.g., 'balance', 'games_won', 'games_lost').
    - file (str): The path to the JSON file containing the list of elements (players, games, etc.).

    Returns:
    - None. The sorted data is directly written back to the input file.
    """

    # Read data from the JSON file
    elemets = read_json(file)
    n = len(elemets)

    # Perform Bubble Sort (O(n^2) complexity)
    for i in range(n):
        for j in range(0, n - i - 1):
            current_value = elemets[j].get(criteria, 0)
            next_value = elemets[j + 1].get(criteria, 0)

            if current_value > next_value:
                # Swap adjacent elements if out of order
                elemets[j], elemets[j + 1] = elemets[j + 1], elemets[j]

    # Write the sorted list back to the file
    write_json(elemets, file)

def sort_elements_by_merge(criteria, file):
    """
    Sorts elements in a JSON file using the Merge Sort algorithm based on a specified criterion.

    Parameters:
    - criteria (str): The dictionary key to sort by.
    - file (str): The path to the JSON file.

    Returns:
    - None. The sorted list is written back to the same file.
    """
    elements = read_json(file)

    def merge_sort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)

    def merge(left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            left_value = left[i].get(criteria, 0)
            right_value = right[j].get(criteria, 0)
            if left_value <= right_value:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    sorted_elements = merge_sort(elements)
    write_json(sorted_elements, file)