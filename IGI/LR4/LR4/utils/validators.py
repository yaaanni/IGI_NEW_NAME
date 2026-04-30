# Purpose: Utility module for safe data input and exception handling.
# Lab: #4 - Files, Classes, Serializers, Regular Expressions, and Standard Libraries.
# Version: 1.0.0.
# Developer: Popova Yana Georgievna.
# Date: 10.04.2026.

class Validator:
    """
    Prompts the user for a non-empty string.
    """

    @staticmethod
    def get_int(prompt: str) -> int:
        """Safely gets an int value from the user."""
        while True:
            value = input(prompt).strip()
            try:
                return int(value)
            except ValueError:
                print("Error: That's not a valid number. Please try again.")

    @staticmethod
    def get_float(prompt: str) -> float:
        """Safely gets a float value from the user."""
        while True:
            value = input(prompt).strip()
            try:
                return float(value)
            except ValueError:
                print("Error: That's not a valid number. Please try again.")

    @staticmethod
    def get_string(prompt: str) -> str:
        """Prompts the user for a non-empty string."""
        while True:
            value = input(prompt).strip()
            if value:
                return value

            print("Error: String cannot be empty. Please try again.")

    @staticmethod
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
