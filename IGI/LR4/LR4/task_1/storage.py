# Purpose: Module for data serialization handling CSV and Pickle formats.
# Demonstrates polymorphism.
# Lab: #4 - Files, Classes, Serializers, Regular Expressions, and Standard Libraries.
# Version: 1.0.0.
# Developer: Popova Yana Georgievna.
# Date: 10.04.2026.

from abc import ABC, abstractmethod
import csv
import pickle
import os


class BaseStorage(ABC):
    """Base abstract class for storage."""

    def __init__(self, filepath: str):
        """
        Initializes the base serializer.

        Args:
            filepath (str): Relative or absolute path to the file for saving/loading data.
        """
        self.filepath = filepath

    @abstractmethod
    def save(self, data: dict) -> None:
        """
        Abstract method for saving data to a file.

        Args:
            data (dict): Dictionary containing the data to be saved.

        Returns:
            None
        """
        pass

    @abstractmethod
    def load(self) -> dict:
        """
        Abstract method for loading data from a file.

        Args:
            None

        Returns:
            dict: Dictionary containing the loaded data.
        """
        pass


class CSVStorage(BaseStorage):
    """Handles CSV serialization."""

    def __init__(self, filepath: str):
        """
        Initializes the CSV serializer.

        Args:
            filepath (str): Path to the target CSV file.
        """
        super().__init__(filepath)

    def save(self, data: dict) -> None:
        """
        Saves data in CSV format.

        Args:
            data (dict): Data to be saved. Expects a structure compatible with csv.DictWriter.

        Returns:
            None: Prints a success or error message to the console.
        """

        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        try:
            with open(self.filepath, "w", newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["Candidate", "Votes"])
                for candidate_name, vote_count in data.items():
                    writer.writerow([candidate_name, vote_count])
            print(f"[OK] Data saved to CSV: {self.filepath}")
        except IOError as e:
            print(f"[Error] Failed to save CSV: {e}")

    def load(self) -> dict:
        """
        Loads data from a CSV file.

        Args:
            None

        Returns:
            dict: Dictionary with election results formatted as {"Name": "Votes"}.
                  Returns an empty dictionary in case of an error.
        """
        result = {}
        try:
            with open(self.filepath, 'r', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                next(reader, None)
                for row in reader:
                    if len(row) == 2:
                        result[row[0]] = int(row[1])
            return result
        except (FileNotFoundError, ValueError, IndexError):
            print(f"[Error] Failed to load CSV: {self.filepath}")
            return {}


class PickleStorage(BaseStorage):
    """Handles pickle serialization."""

    def __init__(self, filepath: str):
        """
        Initializes the Pickle serializer.

        Args:
            filepath (str): Path to the target binary Pickle file.
        """
        super().__init__(filepath)

    def save(self, data: dict) -> None:
        """
        Saves a dictionary into a binary file using the pickle module.

        Args:
            data (dict): Dictionary with election results to be serialized.

        Returns:
            None: Prints a success or error message to the console.
        """
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        try:
            with open(self.filepath, 'wb') as picklefile:
                pickle.dump(data, picklefile)
            print(f"[OK] Data saved to Pickle: {self.filepath}")

        except IOError as e:
            print(f"[Error] Failed to save Pickle: {e}")

    def load(self) -> dict:
        """
        Restores a dictionary from a binary pickle file.

        Args:
            None

        Returns:
            dict: Deserialized dictionary. Returns an empty dictionary if the file
                  is not found or corrupted.
        """
        result = {}
        try:
            with open(self.filepath, 'rb') as picklefile:
                return pickle.load(picklefile)
        except FileNotFoundError:
            print("[Warning] Pickle file not found. Starting with empty data.")
            return {}
        except pickle.PickleError:
            print("[Error] Failed to deserialize Pickle file.")
            return {}
