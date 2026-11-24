# lo-shu-magic-square-game
An interactive console-based Python game simulating the Lo Shu Magic Square puzzle, featuring manual and random gameplay modes, custom exception handling, and session win/loss tracking.
# Lo Shu Magic Square Game (Python)

An interactive console-based puzzle game built in Python based on the mathematical **Lo Shu Magic Square**—a 3×3 grid using the numbers 1 through 9 exactly once so that every row, column, and diagonal adds up to **15**.

## Features & Gameplay Modes
* **Manual Mode:** Prompts the user to enter 9 unique integers (1–9) with real-time validation and custom exception handling to reject duplicates or out-of-range inputs.
* **Random Mode:** Uses Python's `random` module to automatically generate and shuffle a 1–9 grid.
* **Automated Validation & Feedback:** Evaluates all 8 lines (3 rows, 3 columns, 2 diagonals) against the magic sum of `15` and pinpoints the exact lines that failed on a loss.
* **Session Statistics:** Tracks and displays total wins, losses, and games played across a session.

## Tech Stack
* **Language:** Python 3 (Standard Library — `random`)
* **Development Environment:** Visual Studio Code (VS Code)

## Repository Contents
* `README.md` — Project overview, game rules, sample output, and setup instructions.
* `lo_shu_magic_square.py` — Complete Python source code implementing the game loop, grid evaluation, custom exceptions, and CLI interface.

## How to Run Locally
1. Ensure **Python 3** is installed on your machine.
2. Download or clone this repository and navigate to the project folder.
3. Run the script in your terminal or VS Code:
   ```bash
   python lo_shu_magic_square.py
   ```

## Sample Output
```text
Your Magic Square:
+---+---+---+

| 4 | 9 | 2 |
+---+---+---+

| 3 | 5 | 7 |
+---+---+---+

| 8 | 1 | 6 |
+---+---+---+

CONGRATULATIONS! YOU WIN!
Every row, column, and diagonal adds up to 15.
```

## Key Python Concepts Demonstrated
* **2D Lists & Slicing:** Converting flat 9-element lists into a 3×3 nested matrix structure.
* **Custom Exceptions:** Defining `InvalidNumberError` alongside `ValueError` handling inside `try/except` blocks for resilient input validation.
* **Modular Functions:** Separating input collection, grid construction, line summation checks, and UI rendering into clean, reusable functions.
