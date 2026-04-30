# Purpose: Module handling matplotlib drawing for geometric figures.
# Lab: #4 - Files, Classes, Serializers, Regular Expressions, and Standard Libraries.
# Version: 1.0.0.
# Developer: Popova Yana Georgievna.
# Date: 10.04.2026.

import matplotlib.pyplot as plt
import math
import os
from task_4.models import Parallelogram


class ShapePlotter:
    """Class responsible for generating, displaying, and saving shape charts."""

    def draw_parallelogram(self, figure: Parallelogram, text_label: str) -> None:
        """
        Calculates vertices from diagonals, draws the shape, fills it, and adds a label.

        Args:
            figure (Parallelogram): The geometric figure instance to draw.
            text_label (str): The text to display inside the shape.
        """
        d1 = figure.d1
        d2 = figure.d2
        angle_rad = math.radians(figure.angle)

        hx1, hy1 = d1 / 2, 0
        hx2, hy2 = (d2 / 2) * math.cos(angle_rad), (d2 / 2) * math.sin(angle_rad)

        x_coords = [-hx1, hx2, hx1, -hx2, -hx1]
        y_coords = [0, hy2, 0, -hy2, 0]

        fig, ax = plt.subplots(figsize=(8, 6))

        ax.fill(x_coords, y_coords, color=figure.color_obj.color, alpha=0.7)
        ax.plot(x_coords, y_coords, color='black', linewidth=2)

        ax.plot([-hx1, hx1], [0, 0], color='gray', linestyle='--', linewidth=1)
        ax.plot([-hx2, hx2], [-hy2, hy2], color='gray', linestyle='--', linewidth=1)

        ax.text(0, 0, text_label, fontsize=12, ha='center', va='center',
                color='black', weight='bold')

        ax.set_aspect('equal', adjustable='datalim')
        ax.grid(True, linestyle=':', alpha=0.6)
        ax.set_title(f"{figure.get_figure_name()} (Area: {figure.calculate_area():.2f})")
        ax.set_xlabel("X Axis")
        ax.set_ylabel("Y Axis")

        filepath = os.path.join("task_4/data", "parallelogram.png")
        plt.savefig(filepath)
        print(f"[Plot OK] Figure image saved to {filepath}")
        print("[Plot Info] Displaying figure on screen. Close the window to continue.")
        plt.show()