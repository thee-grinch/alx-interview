#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """prints a pascals triangle"""

    answer = [[1]]
    if n <= 0:
        return []
    for i in range(n - 1):
        row = [1]
        row.extend([answer[i][j] + answer[i][j + 1]
                    for j in range(len(answer[i]) - 1)])
        row.append(1)
        answer.append(row)
    return answer
