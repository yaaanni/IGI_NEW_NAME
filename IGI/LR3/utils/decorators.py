# Purpose: Decorator module for measuring execution time of functions.
# Lab: #3 - Standard Data Types, Collections, Functions, Modules.
# Version: 1.0.0.
# Developer: Popova Yana Georgievna.
# Date: 18.03.2026.

import time


def timer_decorator(func):
    """
    Decorator that measures the time it takes for a function to execute.
    Provides performance feedback to the user.
    """

    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        duration = end_time - start_time
        print(f"\n[Performance] Execution time: {duration:.8f} seconds")
        return result

    return wrapper