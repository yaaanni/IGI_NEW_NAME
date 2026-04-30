# Purpose: Implementation of Task 6. Pandas data manipulation and statistical analysis.
# Lab: #4 - Files, Classes, Serializers, Regular Expressions, and Standard Libraries.
# Version: 1.0.0.
# Developer: Popova Yana Georgievna.
# Date: 10.04.2026.

import pandas as pd
import numpy as np
import os
from abc import ABC, abstractmethod


class PandasTaskError(Exception):
    """Base exception class for errors in Task 6."""
    pass


class DatasetNotFoundError(PandasTaskError):
    """Raised when the target CSV dataset cannot be found."""
    pass


class MissingColumnError(PandasTaskError):
    """Raised when required columns are missing from the dataframe."""
    pass


class BaseDataAnalyzer(ABC):
    """
    Abstract base class for dataset analyzers using OOP properties.
    """

    def __init__(self, filepath: str):
        self.filepath = filepath
        self._df = None

    @property
    def filepath(self) -> str:
        return self._filepath

    @filepath.setter
    def filepath(self, value: str) -> None:
        if not value.endswith('.csv'):
            raise ValueError("Filepath must point to a .csv file.")
        self._filepath = value

    @abstractmethod
    def load_data(self) -> None:
        """Abstract method to load data into the dataframe."""
        pass


class WeatherDatasetAnalyzer(BaseDataAnalyzer):
    """
    Concrete class for weather dataset analysis (Part A & B variant specific).
    Inherits from BaseDataAnalyzer and utilizes PandasDemoMixin.
    """

    def __init__(self, filepath: str = "task_6/data/weatherHistory.csv"):
        super().__init__(filepath)

    def load_data(self) -> None:
        """Loads data from CSV into a Pandas DataFrame."""
        try:
            self._df = pd.read_csv(self.filepath)
            print(f"[OK] Successfully loaded dataset: {self.filepath}")
        except FileNotFoundError:
            raise DatasetNotFoundError(f"Dataset not found at {self.filepath}")

    def get_dataframe_info(self) -> None:
        """Prints general information about the DataFrame (Part B basic requirement)."""
        if self._df is None:
            self.load_data()

        print("\n--- DataFrame Information ---")
        print(f"Shape: {self._df.shape}")
        print("\nColumns and Data Types:")
        print(self._df.dtypes)
        print("\nGeneral Statistics:")
        print(self._df.describe())

    def execute_part_a_variant(self) -> pd.DataFrame:
        """
        Executes Part A variant specific task:
        Create a DataFrame of the first 7 days, containing only 'Temperature_c' and 'Humidity'.
        Change indices to days of the week.
        """
        if self._df is None:
            self.load_data()

        required_columns = ['Temperature_c', 'Humidity']
        for col in required_columns:
            if col not in self._df.columns:
                raise MissingColumnError(f"Column '{col}' is missing from the dataset.")

        subset_df = self._df[required_columns].head(7).copy()

        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        subset_df.index = weekdays[:len(subset_df)]

        return subset_df

    def execute_part_b_variant(self) -> float:
        """
        Executes Part B variant specific task:
        Ratio of average temperature in top decile (hottest days)
        vs bottom decile (coldest days).
        """
        if self._df is None:
            self.load_data()

        if 'Temperature_c' not in self._df.columns:
            raise MissingColumnError("Column 'Temperature_c' is missing.")

        q90 = self._df['Temperature_c'].quantile(0.90)
        q10 = self._df['Temperature_c'].quantile(0.10)

        hottest_days = self._df[self._df['Temperature_c'] >= q90]
        coldest_days = self._df[self._df['Temperature_c'] <= q10]

        avg_hot = hottest_days['Temperature_c'].mean()
        avg_cold = coldest_days['Temperature_c'].mean()

        if avg_cold == 0:
            return 0.0

        ratio = avg_hot / avg_cold
        return round(ratio, 2)

    def __str__(self) -> str:
        """Magic method for string representation."""
        status = "Loaded" if self._df is not None else "Not Loaded"
        return f"<WeatherDatasetAnalyzer | Status: {status}>"
