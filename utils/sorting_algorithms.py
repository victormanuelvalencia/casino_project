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