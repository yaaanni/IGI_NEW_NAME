# Purpose: Module handling matplotlib graph generation and saving.
# Lab: #4 - Files, Classes, Serializers, Regular Expressions, and Standard Libraries.
# Version: 1.0.0.
# Developer: Popova Yana Georgievna.
# Date: 10.04.2026.

import matplotlib.pyplot as plt
import os


class SeriesPlotter:
    """Class responsible for generating and saving matplotlib charts."""

    def plot_and_save(self, x_values: list, series_values: list, math_values: list) -> None:
        """
        Draws coordinate axes, lines, legend, annotations and saves to file.

        Args:
            x_values (list): X-axis coordinates.
            series_values (list): Y-axis values calculated via series.
            math_values (list): Y-axis reference values from math module.
        """
        fig, ax = plt.subplots(figsize=(10, 6))

        ax.plot(x_values, series_values, label="Series F(x)", color="blue", marker="o", linestyle="-")
        ax.plot(x_values, math_values, label="Math F(x)", color="red", linestyle="--")

        ax.axhline(0, color='black', linewidth=1)
        ax.axvline(0, color='black', linewidth=1)
        ax.grid(color='gray', linestyle=':', linewidth=0.5)

        ax.set_title("Function Decomposition vs Math Module")
        ax.set_xlabel("Argument (X)")
        ax.set_ylabel("Function Value (Y)")

        zero_idx = min(range(len(x_values)), key=lambda i: abs(x_values[i]))

        target_x = x_values[zero_idx]
        target_y = series_values[zero_idx]

        if x_values:
            ax.annotate(f'Center (x≈{target_x:.2f})',
                         xy=(target_x, target_y),
                         xytext=(target_x + 0.2, target_y + 0.5),
                         arrowprops=dict(facecolor='black', shrink=0.05))

        ax.legend(loc="upper left")

        filepath = os.path.join("task_3/data", "series_plot.png")
        plt.savefig(filepath)
        plt.close()

        print(f"[Plot OK] Graph saved successfully to {filepath}")