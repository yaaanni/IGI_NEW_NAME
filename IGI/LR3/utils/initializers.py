# Purpose: Sequence initialization module.  Contains manual input and generators.
# Lab: #3 - Standard Data Types, Collections, Functions, Modules.
# Version: 1.0.0.
# Developer: Popova Yana Georgievna.
# Date: 18.03.2026.

import random
from utils.validators import get_float


def manual_initialization(size):
    """
    Creates a list of floats by asking the user to enter each value.
    """
    result = []
    for i in range(size):
        val = get_float(f"Enter element {i + 1}: ")
        result.append(val)
    return result


def generator_initialization(size):
    """
    A generator function that yields random float values.
    """
    for _ in range(size):
        yield round(random.uniform(-10.0, 10.0), 2)
