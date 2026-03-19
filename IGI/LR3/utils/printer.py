def display_list_data(data, message="Current list"):
    """
    Displays the elements of the list on the screen.

    This is a utility function used to fulfill Requirement 4 of Task 5.
    It formats the list elements for better readability.

    Args:
        data (list): The list of float numbers to display.
        message (str): A custom message to show before the list.
    """
    if not data:
        print(f"{message}:  The list is empty.")
    else:
        formatted_list = [f"{x:.2f}" for x in data]
        print(f"{message}:  [{', '.join(formatted_list)}]")
