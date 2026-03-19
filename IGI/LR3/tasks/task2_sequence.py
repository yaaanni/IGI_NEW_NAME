# Purpose: Implementation of Task 2.  Product calculation for an integer sequence.
# Lab: #3 - Standard Data Types, Collections, Functions, Modules.
# Version: 1.0.0.
# Developer: Popova Yana Georgievna.
# Date: 18.03.2026.

from utils.validators import get_int
from utils.decorators import timer_decorator


def calculate_sequence_product():
    """
    Reads integers and multiplies them until a positive number is entered.

    This function continues to prompt the user for input.  It stops
    execution immediately when a number greater than zero is detected.

    Returns:
        int: The final product of all entered non-positive integers.
    """

    product = 1

    print("\nEnter integers to multiply.  Enter a positive number to stop.")

    while True:
        number = get_int("Enter an integer (<= 0): ")
        if number > 0:
            print(f"Detected positive number {number}.  Stopping...")
            break

        product *= number

    return product


@timer_decorator
def run_task_2():
    """
    Executes the business logic for Task 2.  Orchestrates the process.

    This function manages the multiplication of an integer sequence
    provided by the user.  It continues the operation until a positive
    number is entered as a termination signal.  The final product
    is calculated and displayed in a user-friendly format.

    Note:
        This function does not require external arguments.  It handles
        all data input internally using specialized integer validators.
    """

    print("\n--- Task 2: Sequence Product ---")

    final_result = calculate_sequence_product()

    print(f"\nTask 2 Finished.  The final product is: {final_result}.")
