"""
Module: Tic-Tac-Toe with NumPy (OOP Version)
Description: This module implements a 2-player Tic-Tac-Toe game using NumPy,
             object-oriented programming, inheritance, polymorphism, and
             operator overloading. It supports both human and AI players.
Author: Ian Patricio
Version: 1.0.0
"""

class User:
    """ Class representing a user account.
    Attributes:
    id (int): The unique identifier of the user.
    username (str): The username associated with the account.
    email (str): The email address of the user.
"""

    def __init__(self, id: int, username: str, email: str):
        """
        Initialize a User object.

        Args:
            id (int): The unique identifier of the user.
            username (str): The username associated with the account.
            email (str): The email address of the user.
        """
        # Store the unique identifier for this user
        self.id = id
        # Store the username for this user
        self.username = username
        # Store the email address for this user
        self.email = email

    def get_id(self) -> int:
        """
        Get the user's unique identifier.

        Returns:
            int: The unique identifier of the user.
        """
        # Return the stored user ID
        return self.id

    def get_username(self) -> str:
        """
        Get the username associated with the account.

        Returns:
            str: The username of the user.
        """
        # Return the stored username
        return self.username

    def get_email(self) -> str:
        """
        Get the email address of the user.

        Returns:
            str: The email address of the user.
        """
        # Return the stored email address
        return self.email

# Retrieve and print the user's unique identifier
if __name__ == "__main__":
    user = User(1, "ianpatricio", "ianpatricio@example.com")
    user_id = user.get_id()
    print(f"User ID: {user_id}")