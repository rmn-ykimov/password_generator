"""
Module for generating random passwords
"""
import secrets


def get_valid_password_length() -> int:
    """
    Prompts the user to input a password length, validates the input, and
    returns it as an integer.

    Returns:
        int: The desired password length between 8 and 128 inclusive.
    
    Raises:
        ValueError: If the user provides an invalid input after 3 attempts.
    """
    # Constants
    max_attempts = 3
    min_length = 8
    max_length = 128

    # Prompt to display to the user
    prompt = (f"Enter a positive integer between {min_length} and {max_length}"
              f" inclusive as the desired password length: ")

    def is_valid_password_length(password_length_input: str) -> bool:
        """
        Validates that the input is a positive integer within the valid
        password length range.

        Args:
            password_length_input (str): The input provided by the user.

        Returns:
            bool: True if the input is a valid password length, False
            otherwise.
        """
        if not password_length_input.isdigit():
            return False
        password_length = int(password_length_input)
        return min_length <= password_length <= max_length

    # Loop over the maximum number of attempts
    for _ in range(max_attempts):
        # Get the password length from the user
        password_length_input = input(prompt)

        if is_valid_password_length(password_length_input):
            return int(password_length_input)
        else:
            print(f"Password length must be a positive integer between"
                  f"{min_length} and {max_length} inclusive.")

    # Raise an error if the user provided too many invalid inputs
    raise ValueError(f"Too many invalid inputs. The maximum number of attempts"
                     f"is {max_attempts}.")

def generate_password(length):
    """
    Generates a random password of the specified length using characters from
    a character pool.

    :param length: The length of the password to generate. It is the
    responsibility of the caller to ensure this is a positive integer.
    :return: A random password string consisting of characters from the
    following character pool:
        "abcdefghijklmnopqrstuvwxyz"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "0123456789"
        "!@#$%^&*_"
    """
    # Create a string of possible characters for the password
    character_pool = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ012"
                      "3456789!@#$%^&*_")
    password_length = length()
    return (''.join(secrets.choice(character_pool)
                    for _ in range(password_length)))
