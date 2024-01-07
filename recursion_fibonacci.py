def fibonacci(n):
    """Fibonacci sequence.

    Args:
        n (int): Number to calculate the fibonacci sequence of.

    Returns:
        int: Fibonacci sequence of n.
    """
    #print(n)
    if n == 0 or n == 1:
        return 1
    else: 
        return fibonacci(n-1) + fibonacci(n-2)
    
n = int(input("Enter a number: "))
print(fibonacci(n))