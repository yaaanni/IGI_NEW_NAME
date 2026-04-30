# Purpose: To master Object-Oriented Programming, file handling, and data serialization.
#          This is achieved by developing an interactive application using regular
#          expressions and Python standard libraries.
# Lab: #4 - Files, Classes, Serializers, Regular Expressions, and Standard Libraries.
# Version: 1.0.0.
# Developer: Popova Yana Georgievna.
# Date: 10.04.2026.

from utils.validators import Validator
import task_1.runner
import task_2.runner
import task_3.runner
import task_4.runner
import task_5.runner
import task_6.runner


def main() -> None:
    """
    Global application loop. Acts as a router to dispatch execution to specific tasks.

    Args:
        None

    Returns:
        None
    """
    while True:
        print("\n" + "=" * 50)
        print("   LABORATORY WORK #4 - MAIN ROUTER   ")
        print("=" * 50)
        print("1. Run Task 1 (Election System & Serialization)")
        print("2. Run Task 2 (Text Analyzer & RegEx)")
        print("3. Run Task 3 (Taylor Series & Matplotlib)")
        print("4. Run Task 4 (Geometric Figures & OOP)")
        print("5. Run Task 5 (NumPy & Statistics)")
        print("6. Run Task 6 (Pandas Data Analysis)")
        print("0. Exit Application")
        print("=" * 50)

        choice = Validator.get_choice("Select a task to run (0-6): ", 0, 10)

        if choice == 1:
            print("\n>>> Launching Task 1 Module...\n")
            task_1.runner.run_task()
        elif choice == 2:
            print("\n>>> Launching Task 2 Module...\n")
            task_2.runner.run_task()
        elif choice == 3:
            print("\n>>> Launching Task 3 Module...\n")
            task_3.runner.run_task()
        elif choice == 4:
            print("\n>>> Launching Task 4 Module...\n")
            task_4.runner.run_task()
        elif choice == 5:
            print("\n>>> Launching Task 5 Module...\n")
            task_5.runner.run_task()
        elif choice == 6:
            print("\n>>> Launching Task 6 Module...\n")
            task_6.runner.run_task()
        elif choice == 0:
            print("\nTerminating the main application. Goodbye!")
            break
        else:
            print("\n[Error] Invalid task number selected.")


if __name__ == "__main__":
    main()
