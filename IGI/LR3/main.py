# Purpose: To master basic Python syntax and gain skills in working with types.
#          This is achieved by developing an interactive application.
# Lab: #3 - Standard Data Types, Collections, Functions, Modules.
# Version: 1.0.0.
# Developer: Popova Yana Georgievna.
# Date: 18.03.2026.

import tasks
from utils.validators import get_x_for_series, get_positive_float, get_int, get_choice
from utils.initializers import manual_initialization, generator_initialization


def main_menu():
    """
    Provides a user-friendly interface for selecting and running tasks.
    """
    while True:
        print("\n" + "=" * 30)
        print("  LABORATORY WORK #3 MENU  ")
        print("=" * 30)
        print("1. Task 1: Taylor Series")
        print("2. Task 2: Sequence Product")
        print("3. Task 3: Text Analysis")
        print("4. Task 4: Alice Text")
        print("5. Task 5: List Processing")
        print("0. Exit")

        choice = get_choice("Select a task number: ", 0, 5)

        if choice == 1:
            x = get_x_for_series("Enter x (-1 < x < 1): ")
            eps = get_positive_float("Enter precision eps: ")
            tasks.run_task_1(x, eps)

        elif choice == 2:
            tasks.run_task_2()

        elif choice == 3:
            tasks.run_task_3()

        elif choice == 4:
            tasks.run_task_4()

        elif choice == 5:
            size = get_int("Enter list size: ")
            print("Choose initialization: 1 - Manual, 2 - Generator.")
            init_type = get_choice("> ", 1, 2)

            if init_type == 1:
                data = manual_initialization(size)
            else:
                data = list(generator_initialization(size))
            tasks.run_task_5(data)

        elif choice == 0:
            print("Exiting program.")
            break

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main_menu()
