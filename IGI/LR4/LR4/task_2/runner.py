# Purpose: User interface, menu, and testing logic specifically for Task 2.
# Lab: #4 - Files, Classes, Serializers, Regular Expressions, and Standard Libraries.
# Version: 1.0.0.
# Developer: Popova Yana Georgievna.
# Date: 10.04.2026.

import os
from task_2.models import VariantTextAnalyzer
from utils.validators import Validator


class TextAnalyzerRunner:
    """
    Main runner class for Task 2: Text Analyzer & Regular Expressions.
    Encapsulates file paths, current state, and UI logic.
    """

    def __init__(self):
        """
        Initializes the runner with default file paths and an empty state.
        """
        self.input_file = "task_2/data/input.txt"
        self.output_file = "task_2/data/results.txt"
        self.zip_file = "task_2/data/results_archive.zip"

        self.current_text = ""
        self.analyzer = None

    def _read_from_file(self) -> None:
        """
        Reads content from a specified text file with exception handling.

        Args:
            None

        Returns:
            None
        """
        try:
            with open(self.input_file, "r", encoding="utf-8") as file:
                self.current_text = file.read()
                print(f"[OK] Successfully read {len(self.current_text)} characters from {self.input_file}.")
        except FileNotFoundError:
            print(f"[Error] File not found: {self.input_file}. Please create it first.")
        except IOError as e:
            print(f"[Error] OS Error occurred while reading: {e}")

    def _enter_manually(self) -> None:
        """
        Captures text input directly from the user via keyboard.

        Args:
            None

        Returns:
            None
        """
        self.current_text = input("Type or paste your text here:\n>> ")
        print(f"[OK] Captured {len(self.current_text)} characters from keyboard.")

    def _save_results(self, results: dict) -> None:
        """
        Formats and saves the analysis dictionary to a text file.

        Args:
            results (dict): The dictionary containing analysis data.

        Returns:
            None
        """
        os.makedirs(os.path.dirname(self.output_file), exist_ok=True)
        try:
            with open(self.output_file, 'w', encoding='utf-8') as f:
                f.write("=== TEXT ANALYSIS RESULTS ===\n\n")
                for key, value in results.items():
                    if isinstance(value, dict):
                        f.write(f"{key}:\n")
                        for sub_k, sub_v in value.items():
                            f.write(f"  {sub_k}: {sub_v}\n")
                    elif isinstance(value, list):
                        f.write(f"{key}:\n")
                        for item in value:
                            f.write(f"  - {item}\n")
                    else:
                        f.write(f"{key}: {value}\n")
                f.write("\n=============================\n")
            print(f"[OK] Results successfully saved to {self.output_file}")
        except IOError as e:
            print(f"[Error] Failed to save results to file: {e}")

    def _display_results(self, results: dict) -> None:
        """
        Prints the analysis results to the console in a readable format.

        Args:
            results (dict): The dictionary containing analysis data.

        Returns:
            None
        """
        print("\n" + "*" * 40)
        print("   ANALYSIS REPORT   ")
        print("*" * 40)
        for key, value in results.items():
            if isinstance(value, (dict, list)) and not value:
                print(f"{key}: None")
            else:
                print(f"{key}: {value}")
        print("*" * 40 + "\n")

    def _run_analysis(self) -> None:
        """
        Instantiates the analyzer, performs text analysis, and delegates saving and displaying.

        Args:
            None

        Returns:
            None
        """
        if not self.current_text:
            print("[!] No text loaded. Please read from file or enter manually first.")
            return

        try:
            self.analyzer = VariantTextAnalyzer(self.current_text)
            print(f"\n[Info] {self.analyzer} initialized. Total length: {len(self.analyzer)} characters.")

            results = self.analyzer.analyze()

            self._display_results(results)
            self._save_results(results)
        except (ValueError, TypeError) as e:
            print(f"[Class Validation Error] {e}")

    def _archive_results(self) -> None:
        """
        Archives the results text file into a ZIP archive.

        Args:
            None

        Returns:
            None
        """
        if not os.path.exists(self.output_file):
            print("[!] Results file does not exist yet. Please run Analysis (Option 3) first.")
            return

        VariantTextAnalyzer.archive_file(self.output_file, self.zip_file)

    def _display_archive_info(self) -> None:
        """
        Displays structural information and contents of the generated ZIP archive.

        Args:
            None

        Returns:
            None
        """
        if not os.path.exists(self.zip_file):
            print("[!] Archive does not exist. Please create it first (Option 4).")
            return

        VariantTextAnalyzer.display_archive_info(self.zip_file)

    def start(self) -> None:
        """
        Main interactive loop for Task 2.
        Provides menu options to read, analyze, save, and archive text.

        Args:
            None

        Returns:
            None
        """
        while True:
            print("\n" + "=" * 50)
            print("   TASK 2: TEXT ANALYZER & REGULAR EXPRESSIONS   ")
            print("=" * 50)
            print("1. Read text from source file")
            print("2. Enter text manually via keyboard")
            print("3. Analyze text, display on screen, and save to file")
            print("4. Archive results file into ZIP")
            print("5. Read information from ZIP archive")
            print("0. Return to Main Router")
            print("=" * 50)

            choice = Validator.get_choice("Select an option (0-5): ", 0, 5)

            if choice == 1:
                self._read_from_file()
            elif choice == 2:
                self._enter_manually()
            elif choice == 3:
                self._run_analysis()
            elif choice == 4:
                self._archive_results()
            elif choice == 5:
                self._display_archive_info()
            elif choice == 0:
                print("\nReturning to the Main Application Router...")
                break


def run_task() -> None:
    """
    Initializes and starts the Text Analyzer application runner.

    Args:
        None

    Returns:
        None
    """
    runner = TextAnalyzerRunner()
    runner.start()