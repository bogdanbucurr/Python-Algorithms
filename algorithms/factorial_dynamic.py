def factorial(n, memory={0:1, 1:1}):
    """Calculates factorial using dynamic programming.

    Args:
        n: the natural number that is the input for the algorithm.
        memory: the results dictionary will be updated with each function call.
    Returns:
        factorial of number n.
    """
    if n in memory:
        return memory[n]
    else:
        memory[n] = n * factorial(n-1)
        return memory[n]


if __name__ == '__main__':
    print(factorial(5))
    print(factorial(3))
    print(factorial(6))