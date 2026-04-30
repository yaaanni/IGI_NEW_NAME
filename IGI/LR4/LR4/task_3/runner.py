# Purpose: User interface, menu, and testing logic specifically for Task 3.
# Lab: #4 - Files, Classes, Serializers, Regular Expressions, and Standard Libraries.
# Version: 1.0.0.
# Developer: Popova Yana Georgievna.
# Date: 10.04.2026.

from task_3.models import GeometricSeries, DomainError
from task_3.plotter import SeriesPlotter
from utils.validators import Validator


class SeriesTaskRunner:
    """
    Main runner class for Task 3: Taylor Series & Matplotlib.
    Coordinates mathematical calculations, statistical analysis, and visualization.
    """

    def __init__(self):
        """
        Initializes the runner with a default GeometricSeries calculator and SeriesPlotter.
        """
        self.series_calc = GeometricSeries(0.001)
        self.plotter = SeriesPlotter()

    def _generate_data(self, start: float, end: float, step: float) -> tuple:
        """
        Generates data arrays for plotting and statistics by iterating through a range.
        Handles DomainError for values outside the convergence range.

        Args:
            start (float): Start value of X.
            end (float): End value of X.
            step (float): Step increment.

        Returns:
            tuple: (x_values, series_values, math_values) lists.
        """
        x_vals, series_vals, math_vals = [], [], []
        current_x = start

        while current_x <= end:
            try:
                s_val, _, m_val = self.series_calc(current_x)
                x_vals.append(current_x)
                series_vals.append(s_val)
                math_vals.append(m_val)
            except DomainError:
                pass

            current_x += step
            current_x = round(current_x, 4)

        return x_vals, series_vals, math_vals

    def _display_statistics(self, series_array: list) -> None:
        """
        Calculates and prints statistical parameters for the generated series values.

        Args:
            series_array (list): List of calculated series results.

        Returns:
            None
        """
        stats = self.series_calc.calculate_statistics(series_array)

        print("\n--- Sequence Statistics (Series Values) ---")
        for key, val in stats.items():
            if isinstance(val, float):
                print(f"{key}: {val:.6f}")
            else:
                print(f"{key}: {val}")

    def _process_calculation(self) -> None:
        """
        Handles the user input for range parameters, triggers data generation,
        displays results table, shows stats, and generates the plot.

        Args:
            None

        Returns:
            None
        """
        print("\nEnter range for X (Remember: must be between -0.99 and 0.99)")
        start = Validator.get_float("Start X: ")
        end = Validator.get_float("End X: ")
        step = Validator.get_float("Step (e.g., 0.1): ")

        if step <= 0:
            print("[!] Step must be greater than 0.")
            return

        x_arr, s_arr, m_arr = self._generate_data(start, end, step)

        if not x_arr:
            print("[!] No valid data generated. Ensure X is in (-1, 1).")
            return

        print("\n" + "-" * 38)
        print(f"{'x':<8} | {'Series F(x)':<12} | {'Math F(x)':<12}")
        print("-" * 38)
        for i in range(len(x_arr)):
            print(f"{x_arr[i]:<8.4f} | {s_arr[i]:<12.6f} | {m_arr[i]:<12.6f}")

        self._display_statistics(s_arr)

        print("\nGenerating plot...")
        self.plotter.plot_and_save(x_arr, s_arr, m_arr)

    def start(self) -> None:
        """
        Main interactive loop for Task 3.
        Provides a menu for updating precision and running the analysis.

        Args:
            None

        Returns:
            None
        """
        while True:
            print("\n" + "=" * 45)
            print("   TASK 3: TAYLOR SERIES & MATPLOTLIB   ")
            print("=" * 45)
            print(f"Current Epsilon (Precision): {self.series_calc.eps}")
            print("1. Set new Epsilon (Precision)")
            print("2. Calculate for a range, show stats, and plot graph")
            print("0. Return to Main Menu")
            print("=" * 45)

            choice = Validator.get_choice("Select an option (0-2): ", 0, 2)

            if choice == 1:
                try:
                    new_eps = Validator.get_float("Enter new epsilon (e.g., 0.0001): ")
                    self.series_calc.eps = new_eps
                    print(f"[OK] Epsilon updated to {self.series_calc.eps}")
                except ValueError as e:
                    print(f"[Error] {e}")

            elif choice == 2:
                self._process_calculation()

            elif choice == 0:
                print("Exiting Task 3...")
                break


def run_task() -> None:
    """
    Initializes and starts the Task 3 application runner.

    Args:
        None

    Returns:
        None
    """
    runner = SeriesTaskRunner()
    runner.start()
