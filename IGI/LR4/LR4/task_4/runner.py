# Purpose: User interface, menu, and testing logic specifically for Task 4.
# Demonstrates OOP controller pattern, mixins, and specific exception handling.
# Lab: #4 - Files, Classes, Serializers, Regular Expressions, and Standard Libraries.
# Version: 1.0.0.
# Developer: Popova Yana Georgievna.
# Date: 10.04.2026.

from task_4.models import Parallelogram, NegativeDimensionError, InvalidAngleError
from task_4.plotter import ShapePlotter
from utils.validators import Validator


class GeometryTaskRunner:
    """
    Main runner class for Task 4: Geometric Figures & OOP.
    Coordinates input validation, object instantiation, and visualization.
    """

    def __init__(self):
        """Initializes the runner and instantiates the shape plotter."""
        self.plotter = ShapePlotter()

    def _process_figure_creation(self) -> None:
        """
        Handles user input, triggers object creation, and dispatches to the plotter.
        Catches specific geometric exceptions.
        """
        print("\n--- Parallelogram Builder ---")

        d1 = Validator.get_float("Enter length of first diagonal (d1): ")
        d2 = Validator.get_float("Enter length of second diagonal (d2): ")
        angle = Validator.get_float("Enter intersection angle in degrees (0-180): ")

        color_name = Validator.get_string("Enter fill color (e.g., 'blue', 'red', 'green'): ")
        text_label = Validator.get_string("Enter text label for the figure: ")

        try:
            figure = Parallelogram(d1, d2, angle, color_name)

            print("\n" + figure.get_formatted_info() + "\n")

            self.plotter.draw_parallelogram(figure, text_label)

        except NegativeDimensionError as e:
            print(f"\n[Geometry Error] Invalid dimension: {e}")
        except InvalidAngleError as e:
            print(f"\n[Geometry Error] Invalid angle: {e}")
        except ValueError as e:
            print(f"\n[Validation Error] {e}")

    def start(self) -> None:
        """Main interactive loop for Task 4."""
        while True:
            print("\n" + "=" * 50)
            print("   TASK 4: GEOMETRIC FIGURES & OOP   ")
            print("=" * 50)
            print("1. Build and plot a Parallelogram")
            print("0. Return to Main Menu")
            print("=" * 50)

            choice = Validator.get_choice("Select an option (0-1): ", 0, 1)

            if choice == 1:
                self._process_figure_creation()
            elif choice == 0:
                print("Exiting Task 4...")
                break


def run_task() -> None:
    """Initializes and starts the Task 4 application runner."""
    runner = GeometryTaskRunner()
    runner.start()
