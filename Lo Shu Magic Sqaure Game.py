
import random

# Magic square sum
MAGIC_SUM = 15

# Example of a winning Lo Shu Magic Square
EXAMPLE_SQUARE = [
    [4, 9, 2],
    [3, 5, 7],
    [8, 1, 6]
]

# Custom exception
class InvalidNumberError(Exception):
    pass


# Get numbers manually from the player
def get_manual_numbers():
    numbers = []

    print("\nEnter 9 different numbers from 1 to 9.")

    while len(numbers) < 9:
        try:
            number = int(input(
                f"Enter number {len(numbers) + 1}: "
            ))

            if number < 1 or number > 9:
                raise InvalidNumberError(
                    "Please enter a number between 1 and 9."
                )

            if number in numbers:
                raise InvalidNumberError(
                    "This number has already been used."
                )

            numbers.append(number)

        except ValueError:
            print("Invalid input! Please enter a whole number.")

        except InvalidNumberError as error:
            print(error)

    return numbers


# Generate random numbers
def get_random_numbers():
    numbers = list(range(1, 10))
    random.shuffle(numbers)
    return numbers


# Convert numbers into a 3x3 grid
def build_grid(numbers):
    return [
        numbers[0:3],
        numbers[3:6],
        numbers[6:9]
    ]


# Check whether the square is a magic square
def check_magic_square(grid):
    lines = {}

    # Check rows and columns
    for i in range(3):
        lines[f"Row {i + 1}"] = sum(grid[i])

        lines[f"Column {i + 1}"] = (
            grid[0][i] + grid[1][i] + grid[2][i]
        )

    # Check diagonals
    lines["Diagonal 1"] = (
        grid[0][0] + grid[1][1] + grid[2][2]
    )

    lines["Diagonal 2"] = (
        grid[0][2] + grid[1][1] + grid[2][0]
    )

    failed = []

    for name, total in lines.items():
        if total != MAGIC_SUM:
            failed.append(f"{name} = {total}")

    return len(failed) == 0, failed


# Display the 3x3 grid
def print_grid(grid):
    print("+---+---+---+")

    for row in grid:
        print("|", end=" ")

        for number in row:
            print(number, end=" | ")

        print()
        print("+---+---+---+")


# Display game instructions
def show_instructions():
    print("=" * 50)
    print("       WELCOME TO LO SHU MAGIC SQUARE")
    print("=" * 50)

    print("""
RULES:

1. Fill the 3x3 grid with numbers from 1 to 9.
2. Each number can only be used once.
3. Each row must add up to 15.
4. Each column must add up to 15.
5. Both diagonals must add up to 15.

If each condition is met, YOU WIN!
If not, YOU LOSE!
""")

    print("Example of a winning square:")
    print_grid(EXAMPLE_SQUARE)


# Play one round
def play_round(mode, session_wins, session_losses):

    if mode == "MANUAL":
        numbers = get_manual_numbers()
    else:
        numbers = get_random_numbers()

    grid = build_grid(numbers)

    is_magic, failed = check_magic_square(grid)

    print("\nYour Magic Square:")
    print_grid(grid)

    if is_magic:
        print("\nCONGRATULATIONS! YOU WIN!")
        print("Every row, column, and diagonal adds up to 15.")
        session_wins += 1

    else:
        print("\nSORRY! YOU LOSE.")

        print("The following lines do not add up to 15:")

        for item in failed:
            print(item)

        session_losses += 1

    return session_wins, session_losses


# Main program
def main():

    session_wins = 0
    session_losses = 0

    show_instructions()

    while True:

        print("\n========== MENU ==========")
        print("1. Play - Manual Numbers")
        print("2. Play - Random Numbers")
        print("3. View Statistics")
        print("4. Quit")
        print("==========================")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":

            session_wins, session_losses = play_round(
                "MANUAL", session_wins, session_losses
            )

        elif choice == "2":

            session_wins, session_losses = play_round(
                "RANDOM", session_wins, session_losses
            )

        elif choice == "3":

            print("\n========== STATISTICS ==========")
            print("Total Wins:", session_wins)
            print("Total Losses:", session_losses)
            print("Total Games:", session_wins + session_losses)
            print("================================")

        elif choice == "4":

            print("\nThank you for playing!")

            print("Final Score:")
            print("Wins:", session_wins)
            print("Losses:", session_losses)

            break

        else:
            print("Invalid choice! Please select 1, 2, 3, or 4.")


# Start the game
if __name__ == "__main__":
    main()