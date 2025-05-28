import numpy as np
from itertools import product
import os

def read_matrix(filename="matrix.txt"):
    """
    Reads a matrix from a file.
    The first line is assumed to be a comment and is skipped.
    Each subsequent line should contain comma-separated integers.
    """
    matrix = []
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        return None
    with open(filename, 'r') as f:
        lines = f.readlines()
        if not lines:
            print(f"Error: File '{filename}' is empty.")
            return None
        
        # Start from the second line if the first line is a comment,
        # otherwise start from the first line.
        start_line = 0
        if lines[0].strip().startswith("//"):
            start_line = 1

        for line in lines[start_line:]:
            try:
                row = [int(val) for val in line.strip().split(',')]
                matrix.append(row)
            except ValueError:
                print(f"Warning: Could not parse line: {line.strip()}. Skipping.")
                continue
    
    if not matrix:
        print("Error: No valid matrix data found in file.")
        return None
    
    # Check if all rows have the same number of columns
    first_row_len = len(matrix[0])
    if not all(len(row) == first_row_len for row in matrix):
        print("Error: Matrix rows have inconsistent number of columns.")
        return None
        
    return matrix

def shift_row(row, shift_amount):
    """
    Performs a circular (right) shift on a list.
    shift_amount is the number of positions to shift to the right.
    """
    if not row:
        return []
    n = len(row)
    # Ensure shift_amount is positive and within the bounds of the row length
    # A positive shift_amount means shifting to the right.
    effective_shift = shift_amount % n
    return row[-effective_shift:] + row[:-effective_shift]

def check_column_sums(matrix_list, target_sum=100):
    """
    Checks if all column sums of the given matrix (list of lists) equal target_sum.
    """
    if not matrix_list or not matrix_list[0]:
        return False
    try:
        np_matrix = np.array(matrix_list)
        return np.all(np_matrix.sum(axis=0) == target_sum)
    except Exception as e:
        print(f"Error during column sum check: {e}")
        return False

def solve_matrix_problem(filename="matrix.txt"):
    """
    Attempts to find a configuration of row shifts such that all column sums are 100.
    """
    original_matrix = read_matrix(filename)

    if original_matrix is None:
        print("Exiting due to matrix reading error.")
        return

    num_rows = len(original_matrix)
    if num_rows == 0:
        print("Matrix is empty. Cannot solve.")
        return
    num_cols = len(original_matrix[0])
    if num_cols == 0:
        print("Matrix rows are empty. Cannot solve.")
        return

    # Generate all possible shift amounts for each row (0 to num_cols-1)
    possible_shifts_per_row = range(num_cols)
    
    # Create all combinations of shifts for all rows
    # For a 6x6 matrix, this will be 6^6 = 46,656 combinations
    total_combinations = num_cols ** num_rows
    print(f"Trying {total_combinations} possible shift combinations...")

    for i, shift_combination in enumerate(product(possible_shifts_per_row, repeat=num_rows)):
        if (i + 1) % 5000 == 0: # Print progress
            print(f"Checked {i+1}/{total_combinations} combinations...")

        shifted_matrix_list = []
        for row_idx in range(num_rows):
            row_to_shift = original_matrix[row_idx]
            shift = shift_combination[row_idx]
            shifted_matrix_list.append(shift_row(list(row_to_shift), shift))

        if check_column_sums(shifted_matrix_list, 100):
            print("\nSolution found!")
            print("Shifts applied (0-indexed, right shifts for each row):", shift_combination)
            print("Resulting matrix:")
            for r in shifted_matrix_list:
                print(r)
            return # Found a solution

    print("\nNo solution found after checking all combinations.")

if __name__ == "__main__":
    solve_matrix_problem(filename="matrix.txt")
