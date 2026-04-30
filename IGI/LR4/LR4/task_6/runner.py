# Purpose: User interface and execution logic for Task 6.
# Lab: #4 - Files, Classes, Serializers, Regular Expressions, and Standard Libraries.
# Version: 1.0.0.
# Developer: Popova Yana Georgievna.
# Date: 10.04.2026.

from task_6.models import WeatherDatasetAnalyzer, PandasTaskError
from utils.validators import Validator


class PandasTaskRunner:
    """
    Controller class to manage the Pandas analysis flow.
    """

    def __init__(self):
        self.analyzer = WeatherDatasetAnalyzer()

    def start(self) -> None:
        """Main loop for Task 6 interface."""
        while True:
            print("\n" + "=" * 55)
            print("   TASK 6: PANDAS DATA ANALYSIS   ")
            print("=" * 55)
            print("1. Show DataFrame General Information (Part B General)")
            print("2. Execute Variant Part A (7-Day Subset & Custom Index)")
            print("3. Execute Variant Part B (Decile Temperature Ratio)")
            print("0. Return to Main Menu")
            print("=" * 55)

            choice = Validator.get_choice("Select an option (0-3): ", 0, 4)

            try:
                if choice == 1:
                    self.analyzer.get_dataframe_info()

                elif choice == 2:
                    print("\n--- Variant Part A: Custom Index DataFrame ---")
                    result_df = self.analyzer.execute_part_a_variant()
                    print(result_df)

                elif choice == 3:
                    print("\n--- Variant Part B: Decile Temperature Ratio ---")
                    ratio = self.analyzer.execute_part_b_variant()
                    print(f"Average temperature of hottest days is {ratio} times greater than coldest days.")

                elif choice == 0:
                    print("Exiting Task 6...")
                    break

            except PandasTaskError as e:
                print(f"\n[Data Error] {e}")


def run_task() -> None:
    """Entry point for Task 6."""
    runner = PandasTaskRunner()
    runner.start()
