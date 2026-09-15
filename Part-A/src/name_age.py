"""Ask for a name and age, then calculate and display the birth year.

Input:
    user_name: String entered by the user in the console.
    user_age: Integer converted from the user's console input.
    CURRENT_YEAR: Integer obtained from the system date.
Process:
    Subtract user_age from CURRENT_YEAR to calculate birth_year.

Output:
    A formatted string showing the user's name and birth year in the console.

Typical usage example:
    What is your name? Crissie
    How old are you? 30
    Hello Crissie! You were born in 1996.
"""

# === Imports ===
from datetime import date

# === Constants ===
CURRENT_YEAR = date.today().year  # Get current year from system as integer


# === Main Function ===
def main() -> None:
    """Run the name-age program."""

    # Get user input.
    user_name = input("What is your name? ")
    user_age = int(input("How old are you? "))
    # Calculate user's approximate birth year.
    birth_year = CURRENT_YEAR - user_age
    # Output personalized message with user's name and birth year.
    print(f"Hello {user_name}! You were born in {birth_year}.")

# === Main Guard ===
if __name__ == "__main__":
    main()


# === References ===

# TODO: Replace with another APA-style reference, or delete this TODO line.
