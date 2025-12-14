#!/usr/bin/python3
"""
pascal triangle
"""


def factorial(n):
    """
    inside the factorial function
    """
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * factorial(n-1)


def c(left, right):
    """
    inside the combination function
    """
    return factorial(left) // (factorial(right) * factorial(left - right))


def pascal_triangle(n):
    """
    inside the function
    """
    result = []
    if n<=0:
        return result
    for i in range(n):
        app = []
        for j in range(i+1):
            app.append(c(i, j))
        result.append(app)
    return result
