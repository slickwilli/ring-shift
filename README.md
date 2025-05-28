# Python Matrix Solver Project (Ring-Shift)

This project contains a Python script (`main.py`) that attempts to solve a specific matrix problem:
Given a matrix of numbers (read from `matrix.txt`), can each row be circularly shifted (left or right) such that every column in the resulting matrix sums to 100?

## Features

- Reads a matrix from a `matrix.txt` file.
- The first line of `matrix.txt` can be a comment starting with `//`.
- Subsequent lines should contain comma-separated integers representing the rows of the matrix.
- Attempts to find a combination of circular shifts for each row.
- Checks if the column sums of the shifted matrix all equal 100.
- Prints the solution (shifts and resulting matrix) if found, or a message if no solution is found.

## Prerequisites

- Python 3.x
- NumPy library (and other dependencies as listed in `requirements.txt`)

## How to Run

1.  **Prepare `matrix.txt`**:
    *   Create a file named `matrix.txt` in the same directory as `main.py`.
    *   The first line can optionally be a comment (e.g., `// My matrix data`).
    *   Each subsequent line should represent a row of your matrix, with numbers separated by commas.
    *   Example `matrix.txt`:
        ```
        // Example 6x6 matrix
        22,31,3,9,15,20
        17,12,14,23,7,27
        32,0,11,16,28,13
        8,21,19,24,2,26
        18,5,34,33,0,10
        25,29,6,35,1,4
        ```

2.  **Set up Environment and Install Dependencies**:
    It's recommended to use a virtual environment.
    ```bash
    # Create a virtual environment (if you haven't already)
    python3 -m venv .venv
    # Activate the virtual environment
    source .venv/bin/activate 
    # Install dependencies from requirements.txt
    pip3 install -r requirements.txt
    ```
    If you are not using a virtual environment, you can install globally (though not recommended):
    ```bash
    pip3 install -r requirements.txt
    ```

3.  **Run the Script**:
    Execute the `main.py` script from your terminal (ensure your virtual environment is activated if you are using one):
    ```bash
    python3 main.py
    ```
    The script will read `matrix.txt` and attempt to find a solution.
