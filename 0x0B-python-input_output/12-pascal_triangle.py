#!/usr/bin/python3

"""Define a pascal triangle function"""

def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal’s triangle of n"""

    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        last_row = triangle[-1]
        new_row = [1]
        for j in range(1, i+1):
            if j < len(last_row):
                new_row.append(last_row[j-1] + last_row[j])
            else:
                new_row.append(1)
        triangle.append(new_row)

    return triangle
