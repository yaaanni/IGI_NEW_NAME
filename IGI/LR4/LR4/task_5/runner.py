# Purpose: User interface, menu, and testing logic specifically for Task 5.
# Lab: #4 - Files, Classes, Serializers, Regular Expressions, and Standard Libraries.
# Version: 1.0.0.
# Developer: Popova Yana Georgievna.
# Date: 10.04.2026.

from task_5.models import VariantNumPyAnalyzer, InvalidMatrixShapeError, NoMatchingElementsError
from utils.validators import Validator


class NumpyTaskRunner:
    """
    Controller class to orchestrate user inputs, matrix generation,
    and outputting the results of NumPy operations.
    """

    def _process_analysis(self) -> None:
        """Handles the creation and analysis of the matrix."""
        print("\n--- Generate Matrix A[n,m] ---")
        rows = Validator.get_int("Enter number of rows (n): ")
        cols = Validator.get_int("Enter number of columns (m): ")

        try:
            analyzer = VariantNumPyAnalyzer(rows, cols)
            print(f"\n[Info] Created: {analyzer}. Total elements: {len(analyzer)}")

            print("\nGenerated Matrix A:")
            print(analyzer.get_matrix())

            analyzer.demonstrate_creation_and_indexing()
            analyzer.demonstrate_operations_and_stats()

            print("\n" + "=" * 40)
            print("   VARIANT SPECIFIC ANALYSIS   ")
            print("=" * 40)

            results = analyzer.analyze()

            print(f"Negative Odd Elements Found: {results['Target Elements']}")
            print(f"Sum of their Absolute Values: {results['Sum of Absolute Values']}")
            print(f"Standard Deviation (NumPy func): {results['NumPy STD']}")
            print(f"Standard Deviation (Manual code): {results['Manual STD']}")

            if results['NumPy STD'] == results['Manual STD']:
                print("[SUCCESS] Both STD calculation methods yielded the exact same result!")

        except InvalidMatrixShapeError as e:
            print(f"\n[Shape Error] {e} Please enter positive integers.")
        except NoMatchingElementsError as e:
            print(f"\n[Data Notice] {e} Try generating a larger matrix.")

    def start(self) -> None:
        """Main loop for Task 5 interface."""
        while True:
            print("\n" + "=" * 50)
            print("   TASK 5: NUMPY LIBRARY & STATISTICS   ")
            print("=" * 50)
            print("1. Generate Matrix & Run Analysis")
            print("0. Return to Main Menu")
            print("=" * 50)

            choice = Validator.get_choice("Select an option (0-1): ", 0, 1)

            if choice == 1:
                self._process_analysis()
            elif choice == 0:
                print("Exiting Task 5...")
                break


def run_task() -> None:
    """Initializes and starts the Task 5 application runner."""
    runner = NumpyTaskRunner()
    runner.start()
