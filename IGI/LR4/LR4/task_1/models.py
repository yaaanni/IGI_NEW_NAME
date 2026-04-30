# Purpose: Module containing business logic classes, models, and mixins.
# Lab: #4 - Files, Classes, Serializers, Regular Expressions, and Standard Libraries.
# Version: 1.0.0.
# Developer: Popova Yana Georgievna.
# Date: 10.04.2026.

class DisplayMixin:
    """
    A mixin class to provide a standardized display capability.
    """

    def display_info(self) -> None:
        """
        Prints the string representation of the instance to the console.

        Args:
            None

        Returns:
            None
        """
        print(f">>> {self}")


class Person:
    """
    Base class representing a person.
    """

    def __init__(self, name: str):
        """
        Initializes a base person object.

        Args:
            name (str): The first name or surname of the person.
        """
        self.name = name


class Candidate(Person, DisplayMixin):
    """
    Class representing an election candidate.
    Inherits from Person and DisplayMixin.
    """

    TOTAL_VOTERS = 2000
    PASS_THRESHOLD = 1 / 3

    def __init__(self, name: str, votes: int):
        """
        Initializes the candidate object.

        Args:
            name (str): The name of the candidate.
            votes (int): The number of votes received.
        """
        super().__init__(name)
        self.votes = votes

    @property
    def votes(self) -> int:
        """
        Getter for retrieving the number of votes.

        Args:
            None

        Returns:
            int: The current number of votes the candidate has.
        """
        return self._votes

    @votes.setter
    def votes(self, value: int) -> None:
        """
        Setter for updating the number of votes with strict validation.

        Args:
            value (int): The new vote count to be set.

        Raises:
            ValueError: If the vote count is negative or exceeds the total number of voters.

        Returns:
            None
        """
        if value < 0:
            raise ValueError("Votes cannot be negative.")
        if value > self.TOTAL_VOTERS:
            raise ValueError(f"Votes cannot exceed total voters ({self.TOTAL_VOTERS}).")
        self._votes = value

    def check_status(self) -> bool:
        """
        Checks if the candidate gathered enough votes to pass the election threshold.

        Args:
            None

        Returns:
            bool: True if the candidate passed (>= 1/3 of total voters), False otherwise.
        """
        return self.votes >= (self.TOTAL_VOTERS * self.PASS_THRESHOLD)

    def __str__(self) -> str:
        """
        Magic method for creating a user-friendly string representation of the candidate.

        Args:
            None

        Returns:
            str: Formatted string containing the candidate's name, votes, and election status.
        """
        status = "PASSED" if self.check_status() else "FAILED (Needs Re-election)"
        return f"Candidate: {self.name:10} | Votes: {self.votes:4} | Status: {status}"

    def __lt__(self, other) -> bool:
        """
        Magic method for sorting candidates by the number of votes (Less Than comparison).

        Args:
            other (Candidate): Another candidate object to compare against.

        Raises:
            TypeError: If the 'other' object is not an instance of the Candidate class.

        Returns:
            bool: True if the current candidate has fewer votes than the other candidate.
        """
        if not isinstance(other, Candidate):
            raise TypeError("Candidate must be an instance of Candidate.")
        return self.votes < other.votes