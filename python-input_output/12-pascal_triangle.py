#!/usr/bin/python3
"""Generates Pascal's Triangle to a given integer"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the
    Pascal’s triangle of n:

    Parameters:
    n: The integer used

    Returns:
    The lists representing the triangle
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle


if __name__ == "__main__":
    print(pascal_triangle(5))
