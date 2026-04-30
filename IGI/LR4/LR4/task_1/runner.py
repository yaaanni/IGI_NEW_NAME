# Purpose: User interface, menu, and testing logic specifically for Task 1.
# Lab: #4 - Files, Classes, Serializers, Regular Expressions, and Standard Libraries.
# Version: 1.0.0.
# Developer: Popova Yana Georgievna.
# Date: 10.04.2026.

from task_1.models import Candidate
from task_1.storage import CSVStorage, PickleStorage
from utils.validators import Validator


class ElectionRunner:
    """
    Main runner class for Task 1: Election Management System.
    Encapsulates storage, state, and UI logic.
    """

    def __init__(self):
        """
        Initializes the runner with storage objects and an empty data dictionary.
        """
        self.csv_storage = CSVStorage("task_1/data/elections.csv")
        self.pickle_storage = PickleStorage("task_1/data/elections.pkl")
        self.current_data = {}

    def _get_candidate_objects(self) -> list:
        """
        Converts the internal dictionary of raw data into a list of Candidate objects.
        Handles potential ValueError if the data is invalid.

        Args:
            None

        Returns:
            list: A list containing instantiated Candidate objects.
        """
        candidates = []
        for name, votes in self.current_data.items():
            try:
                candidates.append(Candidate(name, int(votes)))
            except ValueError as e:
                print(f"[Data Error] Invalid data for candidate {name}: {e}")
        return candidates

    def _analyze_results(self) -> None:
        """
        Sorts candidates, displays their results, and determines if re-elections are necessary
        based on the 1/3 threshold rule.

        Args:
            None

        Returns:
            None
        """
        candidates = self._get_candidate_objects()

        if not candidates:
            print("[!] No candidates available to analyze.")
            return

        candidates.sort(reverse=True)
        passed_candidates = []

        print("\n--- ELECTION RESULTS (SORTED BY VOTES) ---")
        for candidate in candidates:
            candidate.display_info()
            if candidate.check_status():
                passed_candidates.append(candidate)

        print("\n--- FINAL ELECTION OUTCOME ---")
        if passed_candidates:
            print("The following candidates have PASSED the 1/3 threshold:")
            for passed_candidate in passed_candidates:
                print(f"- {passed_candidate.name} ({passed_candidate.votes} votes)")
        else:
            print("NO CANDIDATES passed the required threshold. RE-ELECTIONS ARE REQUIRED.")

    def _search_candidate(self) -> None:
        """
        Prompts the user for a candidate's name and displays their detailed information.

        Args:
            None

        Returns:
            None
        """
        candidates = self._get_candidate_objects()
        search_name = Validator.get_string("Enter candidate's last name to search: ")
        found = False

        for candidate in candidates:
            if candidate.name.lower() == search_name.lower():
                print("\n--- Search Result ---")
                candidate.display_info()
                found = True
                break

        if not found:
            print(f"\n[!] Candidate '{search_name}' was not found in the records.")

    def start(self) -> None:
        """
        Main interactive loop for Task 1.
        Provides a user-friendly menu for saving, loading, analyzing, and searching data.

        Args:
            None

        Returns:
            None
        """
        while True:
            print("\n" + "=" * 45)
            print("   TASK 1: ELECTION MANAGEMENT SYSTEM   ")
            print("=" * 45)
            print("1. Save current data to CSV format")
            print("2. Save current data to Pickle format")
            print("3. Load data from CSV")
            print("4. Load data from Pickle")
            print("5. Analyze and show election results (Sorting)")
            print("6. Search for a specific candidate")
            print("7. Add new candidate (Keyboard input)")
            print("0. Return to Main Menu")
            print("=" * 45)

            choice = Validator.get_choice("Select an option (0-7): ", 0, 7)

            if choice == 1:
                self.csv_storage.save(self.current_data)
            elif choice == 2:
                self.pickle_storage.save(self.current_data)
            elif choice == 3:
                loaded = self.csv_storage.load()
                if loaded:
                    self.current_data = loaded
            elif choice == 4:
                loaded = self.pickle_storage.load()
                if loaded:
                    self.current_data = loaded
            elif choice == 5:
                self._analyze_results()
            elif choice == 6:
                self._search_candidate()
            elif choice == 7:
                name = Validator.get_string("Enter candidate last name: ")
                votes = Validator.get_int(f"Enter number of votes for {name}: ")
                self.current_data[name] = votes
                print(f"[OK] {name} added to local data. Don't forget to SAVE (1 or 2)!")
            elif choice == 0:
                print("\nReturning to the Main Application...")
                break

def run_task() -> None:
    """
    Initializes and starts the Election Management System runner.

    Args:
        None

    Returns:
        None
    """
    runner = ElectionRunner()
    runner.start()