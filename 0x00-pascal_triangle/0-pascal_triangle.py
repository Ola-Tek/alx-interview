#!/usr/bin/python3
"""
a script defining a function which prints the pascal triangle
"""
def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the triangle with the first row

    for i in range(1, n):
        row = [1]  # Start each new row with 1
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)  # End each new row with 1
        triangle.append(row)

    return triangle

