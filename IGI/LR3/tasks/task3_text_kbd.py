# Purpose: Implementation of Task 3.  Counting uppercase English letters and digits.
# Lab: #3 - Standard Data Types, Collections, Functions, Modules.
# Version: 1.0.0.
# Developer: Popova Yana Georgievna.
# Date: 18.03.2026.

from utils.decorators import timer_decorator


def count_chars_and_digits(text):
    """
    Analyzes the input string to count uppercase English letters and digits.

    This function iterates through each character of the string.  It checks
    if the character is an uppercase English letter (A-Z) or a digit (0-9).

    Args:
        text (str): The string provided by the user via keyboard input.

    Returns:
        tuple: (upper_count, digit_count) containing the respective counts.
    """

    upper_count = 0
    digit_count = 0

    for char in text:
        if char.isdigit():
            digit_count += 1
        elif 'A' <= char <= 'Z':
            upper_count += 1

    return upper_count, digit_count


@timer_decorator
def run_task_3():
    """
    Executes the business logic for Task 3.  Displays the analysis results.

    This function prompts the user to enter a string from the keyboard.
    It then calls the analysis function and outputs the final counts.
    """
    print("\n--- Task 3: Text Analysis ---")

    user_input = input("Enter a string for analysis: ")

    up_cnt, dig_cnt = count_chars_and_digits(user_input)

    print(f"\nAnalysis results for your input:")
    print(f"- Uppercase English letters (A-Z): {up_cnt}.")
    print(f"- Digits (0-9): {dig_cnt}.")
