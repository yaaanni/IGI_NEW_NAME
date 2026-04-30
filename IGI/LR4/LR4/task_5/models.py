# Purpose: Implementation of Task 5. NumPy arrays, math, stats, and OOP.
# Lab: #4 - Files, Classes, Serializers, Regular Expressions, and Standard Libraries.
# Version: 1.0.0.
# Developer: Popova Yana Georgievna.
# Date: 10.04.2026.

import numpy as np
import pandas as pd
import math
from abc import ABC, abstractmethod


class NumpyTaskError(Exception):
    """Base exception class for errors in Task 5."""
    pass


class InvalidMatrixShapeError(NumpyTaskError):
    """Raised when provided matrix dimensions are invalid (<= 0)."""
    pass


class NoMatchingElementsError(NumpyTaskError):
    """Raised when the specific variant conditions find no matching elements in the matrix."""
    pass


class NumpyDemoMixin:
    """
    Mixin class to demonstrate general NumPy capabilities (Part A and B of the assignment).
    """

    def demonstrate_creation_and_indexing(self) -> None:
        """Demonstrates array creation, specific shape generation, and indexing/slicing."""
        print("\n--- NumPy Demonstration: Creation & Indexing ---")

        pd_series = pd.Series([100, 200, 300])
        arr_from_values = pd_series.values
        print(f"Extracted via values: {arr_from_values}")
        print(f"Type after .values: {type(arr_from_values)}")

        basic_arr = np.array([1, 2, 3, 4, 5])
        zeros_arr = np.zeros((2, 3), dtype=int)
        ones_arr = np.ones((2, 3), dtype=int)
        arrange_arr = np.arange(10, 60, 10)

        print(f"Basic Array: {basic_arr}")
        print(f"Zeros Matrix:\n{zeros_arr}")
        print(f"Ones Matrix:\n{ones_arr}")
        print(f"Arrange Array: {arrange_arr}")

        demo_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        print("\nDemo Matrix:\n", demo_matrix)
        print("Element at [1, 2] (Index):", demo_matrix[1, 2])
        print("Slice of rows 0:2, cols 1:3 (Slicing):\n", demo_matrix[0:2, 1:3])

    def demonstrate_operations_and_stats(self) -> None:
        """Demonstrates universal element-wise functions and statistical operations."""
        print("\n--- NumPy Demonstration: Operations & Statistics ---")

        arr = np.array([1.5, 4.0, 9.0, 16.0])
        print(f"Original Array: {arr}")
        print(f"Square root (np.sqrt): {np.sqrt(arr)}")
        print(f"Add 10 (np.add): {np.add(arr, 10)}")

        stats_arr = np.array([10, 20, 20, 40, 50])
        print(f"\nStats Array: {stats_arr}")
        print(f"1. Mean (mean): {np.mean(stats_arr)}")
        print(f"2. Median (median): {np.median(stats_arr)}")
        print(f"4. Variance (var): {np.var(stats_arr):.2f}")
        print(f"5. Standard Deviation (std): {np.std(stats_arr):.2f}")

        x = np.array([1, 2, 3, 4])
        y = np.array([2, 4, 6, 8])
        print(f"\n3. Correlation Coefficient between {x} and {y}:\n{np.corrcoef(x, y)}")


class BaseMatrixAnalyzer(ABC):
    """
    Abstract base class for matrix analysis using OOP properties and polymorphism.
    """

    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols

    @property
    def rows(self) -> int:
        return self._rows

    @rows.setter
    def rows(self, value: int) -> None:
        if value <= 0:
            raise InvalidMatrixShapeError("Number of rows must be positive.")
        self._rows = value

    @property
    def cols(self) -> int:
        return self._cols

    @cols.setter
    def cols(self, value: int) -> None:
        if value <= 0:
            raise InvalidMatrixShapeError("Number of columns must be positive.")
        self._cols = value

    @abstractmethod
    def analyze(self) -> dict:
        """Abstract method to perform variant-specific analysis."""
        pass


class VariantNumPyAnalyzer(BaseMatrixAnalyzer, NumpyDemoMixin):
    """
    Concrete class for analyzing the randomly generated integer matrix
    according to the specific variant rules.
    """

    RANDOM_MIN = -50
    RANDOM_MAX = 50

    def __init__(self, rows: int, cols: int):
        """Initializes the object using super() and generates the random matrix."""
        super().__init__(rows, cols)
        temp_arr = np.random.randint(self.RANDOM_MIN, self.RANDOM_MAX, size=(self.rows, self.cols))
        self.matrix = temp_arr

    def _get_matrix(self) -> np.ndarray:
        return self._matrix

    def _set_matrix(self, new_matrix: np.ndarray) -> None:
        if not isinstance(new_matrix, np.ndarray):
            raise TypeError("Expected a NumPy array")

        if new_matrix.shape != (self.rows, self.cols):
            raise InvalidMatrixShapeError(f"Shape {new_matrix.shape} != {(self.rows, self.cols)}")

        self._matrix = new_matrix

    matrix = property(_get_matrix, _set_matrix)

    def _manual_std(self, arr: np.ndarray) -> float:
        """
        Calculates standard deviation using manual programming logic.
        Formula: sqrt( sum((x - mean)^2) / N )
        """
        n = len(arr)
        if n == 0:
            return 0.0

        mean_val = sum(arr) / n
        variance = sum((x - mean_val) ** 2 for x in arr) / n
        return math.sqrt(variance)

    def analyze(self) -> dict:
        """
        Polymorphic method implementing the specific variant logic:
        - Filters negative odd elements.
        - Sums their absolute values.
        - Calculates STD using NumPy.
        - Calculates STD using manual formula.
        """
        mask = (self._matrix < 0) & (self._matrix % 2 != 0)
        target_elements = self._matrix[mask]

        if target_elements.size == 0:
            raise NoMatchingElementsError("No negative odd elements found in the generated matrix.")

        abs_sum = np.sum(np.abs(target_elements))

        np_std = np.std(target_elements)
        manual_std = self._manual_std(target_elements)

        return {
            "Target Elements": target_elements.tolist(),
            "Sum of Absolute Values": abs_sum,
            "NumPy STD": round(np_std, 2),
            "Manual STD": round(manual_std, 2)
        }

    def __str__(self) -> str:
        """Magic method for string representation."""
        return f"<VariantNumPyAnalyzer: Matrix {self.rows}x{self.cols}>"

    def __len__(self) -> int:
        """Magic method returning the total number of elements in the matrix."""
        return self.rows * self.cols
