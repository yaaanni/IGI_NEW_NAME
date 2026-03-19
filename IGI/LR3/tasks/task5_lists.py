# Purpose: Implementation of Task 5.  Processing lists of real numbers.
# Lab: #3 - Standard Data Types, Collections, Functions, Modules.
# Version: 1.0.0.
# Developer: Popova Yana Georgievna.
# Date: 18.03.2026.

from utils.decorators import timer_decorator
from utils.printer import display_list_data


def find_min_abs_index(data):
    """
    Finds the index of the element with the minimum absolute value.
    """
    if not data:
        return None

    min_val = min(data, key=abs)
    return data.index(min_val)


def sum_after_first_positive(data):
    """
    Calculates the sum of elements located after the first positive element.
    """
    first_pos_idx = -1

    for i, val in enumerate(data):
        if val > 0:
            first_pos_idx = i
            break

    if first_pos_idx == -1 or first_pos_idx == len(data) - 1:
        return 0.0

    return sum(data[first_pos_idx + 1:])


@timer_decorator
def run_task_5(data):
    """
    Business function for Task 5.  Displays the list and processing results.
    """
    print("\n--- Task 5: List Processing Results ---")
    display_list_data(data)

    idx = find_min_abs_index(data)
    if idx is not None:
        print(f"1) Index of min absolute element: {idx} (Value: {data[idx]}).")

    total_sum = sum_after_first_positive(data)
    print(f"2) Sum of elements after the first positive: {total_sum:.2f}.")
