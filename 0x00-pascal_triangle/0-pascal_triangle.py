#!/usr/bin/python3
"""
0-pascal_triangle
"""

def pascal_triangle(n):
    """
    Generates a Pascal's triangle with 'n' rows.

    Args:
        n: The number of rows in the Pascal's triangle.

    Returns:
        A list of lists representing the Pascal's triangle.
    """

    if n <= 0:
        return []

    pascal_triangle = [[1]]

    for i in range(1, n):
        row = [1]
        prev_row = pascal_triangle[i - 1]

        for j in range(len(prev_row) - 1):
            row.append(prev_row[j] + prev_row[j + 1])

        row.append(1)
        pascal_triangle.append(row)

    return pascal_triangle