def fibonacci_iterative(n):
    """
    Generate Fibonacci series using iterative approach
    Returns a list of first n Fibonacci numbers
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[i-1] + fib_series[i-2])
    
    return fib_series

def fibonacci_recursive(n):
    """
    Generate nth Fibonacci number using recursive approach
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_generator(n):
    """
    Generate Fibonacci series using generator
    Yields Fibonacci numbers up to n terms
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def fibonacci_memoization(n, memo={}):
    """
    Generate nth Fibonacci number using memoization for efficiency
    """
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        memo[n] = fibonacci_memoization(n-1, memo) + fibonacci_memoization(n-2, memo)
        return memo[n]

def print_fibonacci_series(n):
    """
    Print Fibonacci series in a formatted way
    """
    print(f"Fibonacci Series (first {n} terms):")
    
    # Using iterative approach
    series = fibonacci_iterative(n)
    print(f"Iterative: {series}")
    
    # Using generator
    gen_series = list(fibonacci_generator(n))
    print(f"Generator:  {gen_series}")
    
    # Using recursive (individual numbers)
    print("Recursive (individual):", end=" ")
    for i in range(n):
        print(fibonacci_recursive(i), end=" ")
    print()
    
    # Using memoization
    print("Memoization (individual):", end=" ")
    for i in range(n):
        print(fibonacci_memoization(i), end=" ")
    print()

if __name__ == "__main__":
    # Example usage
    n = 10
    print("=" * 50)
    print_fibonacci_series(n)
    print("=" * 50)
    
    # Test with different values
    print("\nTesting with different values:")
    for test_n in [5, 8, 12]:
        print(f"\nFirst {test_n} Fibonacci numbers:")
        series = fibonacci_iterative(test_n)
        print(series) 