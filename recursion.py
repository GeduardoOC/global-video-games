import sys

print(sys.getrecursionlimit())

def factorial(n):
    """Calculates the factorial of n.

    Args:
        n (int): Number to calculate the factorial of.

    Returns:
        int: Factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Input a number to compute the factorial : "))
print(factorial(n))