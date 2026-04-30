# Purpose: Mathematical models, statistical mixins, and custom exceptions.
# Lab: #4 - Files, Classes, Serializers, Regular Expressions, and Standard Libraries.
# Version: 1.0.0.
# Developer: Popova Yana Georgievna.
# Date: 10.04.2026.

import statistics
from abc import ABC, abstractmethod


class DomainError(ValueError):
    """Custom exception for math domain errors."""
    pass


class StatisticsMixin:
    """
    Mixin class to provide statistical calculations for a sequence.
    Demonstrates Interface Segregation Principle.
    """

    @staticmethod
    def calculate_statistics(sequence: list) -> dict:
        """
        Calculates mean, median, mode, variance, and standard deviation.

        Args:
            sequence (list): A list of numerical values.

        Returns:
            dict: Dictionary containing statistical parameters.
        """
        if not sequence:
            return {}

        modes = statistics.multimode(sequence)

        if len(modes) > 1:
            mode_val = "No unique mode"
        else:
            mode_val = modes[0]

        return {
            "Mean": statistics.mean(sequence),
            "Median": statistics.median(sequence),
            "Mode": mode_val,
            "Variance": statistics.variance(sequence) if len(sequence) > 1 else 0.0,
            "Standard Deviation": statistics.stdev(sequence) if len(sequence) > 1 else 0.0
        }


class BaseSeries(ABC):
    """
    Abstract base class for series calculation.
    """

    def __init__(self, eps: float):
        self.eps = eps

    @property
    def eps(self) -> float:
        """Getter for epsilon (precision)."""
        return self._eps

    @eps.setter
    def eps(self, value: float) -> None:
        """Setter with strict validation."""
        if value <= 0 or value >= 1:
            raise ValueError("Epsilon must be between 0 and 1 exclusive.")
        self._eps = value

    @abstractmethod
    def calculate(self, x: float) -> tuple:
        """Abstract method to enforce implementation in subclasses."""
        pass


class GeometricSeries(BaseSeries, StatisticsMixin):
    """
    Concrete class for calculating the geometric series.
    Inherits from BaseSeries and utilizes StatisticsMixin.
    """

    MAX_ITERATIONS = 500

    def __init__(self, eps: float):
        """Initializes using super() to access parent class logic."""
        super().__init__(eps)

    def calculate(self, x: float) -> tuple:
        """
        Calculates the sum of the geometric series.

        Args:
            x (float): Argument value.

        Raises:
            DomainError: If absolute value of x is >= 1.

        Returns:
            tuple: (calculated_sum, iterations_count, math_reference_value)
        """
        if abs(x) >= 1:
            raise DomainError("Argument x must be in the range (-1, 1) for convergence.")

        n = 0
        current_sum = 0.0
        term = 1.0

        for _ in range(self.MAX_ITERATIONS):
            current_sum += term
            n += 1

            if abs(term) < self.eps:
                break

            term *= x

        math_f_x = 1 / (1 - x)
        return current_sum, n, math_f_x

    def __str__(self) -> str:
        """Magic method for string representation."""
        return f"Geometric Series Calculator (eps={self.eps})"

    def __call__(self, x: float) -> tuple:
        """Magic method to make the instance callable like a function."""
        return self.calculate(x)