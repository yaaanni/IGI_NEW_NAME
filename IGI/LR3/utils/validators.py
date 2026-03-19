# Purpose: Utility module for safe data input and exception handling.
# Lab: #3 - Standard Data Types, Collections, Functions, Modules.
# Version: 1.0.0.
# Developer: Popova Yana Georgievna.
# Date: 18.03.2026.

def get_float(prompt):
    """
    Safely gets a float value from the user.
    Handles ValueError if the input is not a number.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: That's not a valid number. Please try again.")


def get_int(prompt):
    """
    Safely gets an int value from the user.
    Handles ValueError if the input is not a number.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error: That's not a valid number. Please try again.")


def get_positive_float(prompt):
    """
    Safely gets a positive float.
    """
    while True:
        value = get_float(prompt)
        if value > 0:
            return value
        print("Error: The value must be greater than zero.")


def get_choice(prompt, min_val, max_val):
    """
    Ensures the user selects a valid task number between min_val and max_val.
    """
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Error: Please choose a task from {min_val} to {max_val}.")
        except ValueError:
            print("Error: Invalid input. Please enter a task number (integer).")


def get_x_for_series(prompt):
    """
    Gets x and ensures it is within the convergence range (-1, 1).
    """
    while True:
        try:
            val = float(input(prompt))
            if -1 < val < 1:
                return val
            print("Error: For this series, x must be between -1 and 1.")
        except ValueError:
            print("Error: Invalid input.  Please enter a number.")
