# Purpose: Implementation of Task 4. Geometric figures, inheritance, and properties.
# Lab: #4 - Files, Classes, Serializers, Regular Expressions, and Standard Libraries.
# Version: 1.0.0.
# Developer: Popova Yana Georgievna.
# Date: 10.04.2026.

import math
from abc import ABC, abstractmethod


class GeometryError(Exception):
    """Base exception class for geometry-related errors."""
    pass


class NegativeDimensionError(GeometryError):
    """Raised when a physical dimension is negative or zero."""
    pass


class InvalidAngleError(GeometryError):
    """Raised when an angle is outside the 0-180 degree range."""
    pass


class GeometryValidationMixin:
    """
    Mixin class to provide validation logic for geometric dimensions.
    Demonstrates the use of Mixins in Python OOP.
    """

    def validate_positive(self, value: float, name: str) -> None:
        """Validates that a given dimension is strictly positive."""
        if value <= 0:
            raise NegativeDimensionError(f"{name} must be strictly positive. Got: {value}")

    def validate_angle(self, angle: float) -> None:
        """Validates that an angle is strictly between 0 and 180 degrees."""
        if not (0 < angle < 180):
            raise InvalidAngleError(f"Angle must be strictly between 0 and 180. Got: {angle}")


class FigureColor:
    """
    Class encapsulating the color property of a geometric figure.
    Demonstrates properties and encapsulation.
    """

    def __init__(self, color: str):
        self.color = color

    @property
    def color(self) -> str:
        """Getter for the color property."""
        return self._color

    @color.setter
    def color(self, value: str) -> None:
        """Setter with strict validation for the color property."""
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Color must be a non-empty string.")
        self._color = value.strip().lower()


class GeometricFigure(ABC):
    """
    Abstract base class representing a generic geometric figure.
    """

    def __init__(self):
        """Initializes the base class using super()."""
        super().__init__()

    @abstractmethod
    def calculate_area(self) -> float:
        """
        Abstract method for calculating the area of the figure.
        Must be overridden in derived classes (Polymorphism).
        """
        pass


class Parallelogram(GeometricFigure, GeometryValidationMixin):
    """
    Concrete class representing a parallelogram built by diagonals and angle.
    Inherits from GeometricFigure and GeometryValidationMixin.
    """

    FIGURE_NAME = "Parallelogram"

    def __init__(self, d1: float, d2: float, angle: float, color_name: str):
        """
        Constructor for the Parallelogram class.

        Args:
            d1 (float): Length of the first diagonal.
            d2 (float): Length of the second diagonal.
            angle (float): Angle between the diagonals in degrees.
            color_name (str): The color of the figure.
        """
        super().__init__()

        self.validate_positive(d1, "Diagonal 1 (d1)")
        self.validate_positive(d2, "Diagonal 2 (d2)")
        self.validate_angle(angle)

        self.d1 = d1
        self.d2 = d2
        self.angle = angle

        self.color_obj = FigureColor(color_name)

    @classmethod
    def get_figure_name(cls) -> str:
        """Class method to return the static figure name."""
        return cls.FIGURE_NAME

    def calculate_area(self) -> float:
        """
        Overrides the abstract method to calculate the parallelogram area.
        Formula: Area = 0.5 * d1 * d2 * sin(angle)
        """
        rad_angle = math.radians(self.angle)
        return 0.5 * self.d1 * self.d2 * math.sin(rad_angle)

    def get_formatted_info(self) -> str:
        """
        Returns a formatted string containing basic parameters, color, and area.
        Demonstrates the use of the required .format() method.
        """
        area = self.calculate_area()
        name = self.get_figure_name()

        template = (
            "--- {0} Properties ---\n"
            "Color: {1}\n"
            "Diagonal 1 (d1): {2}\n"
            "Diagonal 2 (d2): {3}\n"
            "Intersection Angle: {4} degrees\n"
            "Calculated Area: {5:.2f}"
        )
        return template.format(name, self.color_obj.color, self.d1, self.d2, self.angle, area)

    def __str__(self) -> str:
        """Magic method for user-friendly string representation."""
        return f"<{self.get_figure_name()} | Area: {self.calculate_area():.2f}>"
