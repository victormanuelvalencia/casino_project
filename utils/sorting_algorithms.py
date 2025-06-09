# Bubble Sort algorithm for sorting elements in a JSON file by a given criteria.
# utils/data_management.py

import json
from utils.file_administration import *

def sort_elements_by(criteria, file):
    """
    Sorts a list of elements (dictionaries) stored in a JSON file based on a given criteria.
    The sorting algorithm used is Bubble Sort, which compares adjacent elements and swaps them
    if they are in the wrong order. It operates on numerical or comparable values extracted by key.

    Args:
        criteria (str): The key in each dictionary to sort by (e.g., 'balance', 'games_won').
        file (str): The path to the JSON file that contains the list of elements.

    The sorted list is written back to the same JSON file after sorting.
    """
    # Read data from the JSON file
    elemets = read_json(file)
    n = len(elemets)

    # Bubble Sort algorithm: O(n^2)
    for i in range(n):
        for j in range(0, n - i - 1):
            current_value = elemets[j].get(criteria, 0)
            next_value = elemets[j + 1].get(criteria, 0)

            # Swap if current element is greater than the next one
            if current_value > next_value:
                elemets[j], elemets[j + 1] = elemets[j + 1], elemets[j]

    # Write the sorted list back to the JSON file
    write_json(elemets, file)