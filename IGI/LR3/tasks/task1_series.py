# Purpose: Implementation of Task 1.  Calculating function values using Taylor series.
# Lab: #3 - Standard Data Types, Collections, Functions, Modules.
# Version: 1.0.0.
# Developer: Popova Yana Georgievna.
# Date: 18.03.2026.

import math
from utils.decorators import timer_decorator


def calculate_geometric_series(x, eps):
    """
    Calculates the sum of the series 1 + x + x^2 + ...

    Args:
        x (float): The argument value (|x| must be less than 1).
        eps (float): The target precision for the sum calculation.

    Returns:
        tuple: (current_sum, n, reached_limit) where:
            - current_sum (float): The calculated sum of the series.
            - n (int): The number of terms summed.
            - reached_limit (bool): True if the 500 iterations limit was hit.
    """
    n = 0
    current_sum = 0.0
    term = 1.0
    max_iterations = 500
    reached_limit = False

    for i in range(max_iterations):
        current_sum += term
        n += 1

        if abs(term) < eps:
            break

        term *= x
    else:
        reached_limit = True

    return current_sum, n, reached_limit


@timer_decorator
def run_task_1(x, eps):
    """
        Executes the business logic for Task 1.  Orchestrates the process.

        This function coordinates the calculation of the geometric series
        and compares it with the reference value from the math formula.
        It is responsible for displaying the final results in a table.

        Args:
            x (float): The argument value for the series calculation.
            eps (float): The desired precision for the result.
        """

    print("\n--- Task 1: Taylor Series ---")

    f_x, n, limit_hit = calculate_geometric_series(x, eps)

    math_f_x = 1 / (1 - x)

    if limit_hit:
        print("\nWarning:  The maximum limit of 500 terms was reached.")
        print("The precision might be lower than requested.")

    print(f"\n{'x':<10} | {'F(x)':<12} | {'n':<5} | {'Math F(x)':<12} | {'eps':<10}")
    print("-" * 68)

    print(f"{x:<10.4f} | {f_x:<12.6f} | {n:<5} | {math_f_x:<12.6f} | {eps:<10.1e}")
