#!/usr/bin/python3
"""
0-pascal_triangle
"""
def pascal_triangle(n):
    """Generates a Pascal's triangle with 'n' rows.

    Args:
        n: The number of rows in the Pascal's triangle.

    Returns:
        A list of lists representing the Pascal's triangle.
    """

    if n <= 0:
        return []

    pascal_triangle = []

    for i in range(n):
        row = []

        if i == 0:
            row.append(1)
        else:
            prev_row = pascal_triangle[i - 1]
            row = [prev_row[j] + prev_row[j + 1] for j in range(len(prev_row) - 1)]
            row.insert(0, 1)
            row.append(1)

        pascal_triangle.append(row)

    return pascal_triangle