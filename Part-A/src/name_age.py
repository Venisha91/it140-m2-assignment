""" Ask for a user's name and age, then display their birth year.

Input:
    The user's name as a string from user input.
    The user's age as an integer from user input.
    The current year as an integer from the sytem date.

Process:
    Subtract the user's age fromthe current year to calculate the birth year.

Output:
    A personalized console message with the user's name and birth year.

Typical usage example:
    What is your name? Jordan
    How old are you? 25
    Hello Jordan! You were born in 2001. 
"""

# === Imports ===
from datetime import date

# === Constants ===
CURRENT_YEAR = date.today().year  # Get current year from system as integer


# === Main Function ===
def main() -> None:
    """Run the name-age program."""

    # Get user input.
        name= input(What is your name? ")
        # age= int(input("How old are you?"))

    # Calculate user's approximate birth year.
    # birth_year = CURRENT_YEAR - age

    # Output personalized message with user's name and birth year.
    # print(f"\nHello {name}! You were born in {birth_year}.")


# === Main Guard ===
if __name__ == "__main__":
    main()


# === References ===

# TODO: Replace with another APA-style reference, or delete this TODO line.
