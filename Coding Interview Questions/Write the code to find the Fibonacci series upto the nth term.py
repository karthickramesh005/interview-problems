#  Write the code to find the Fibonacci series upto the nth term : 

def fibonacci_series(n):
    fib_series = [0, 1]

    while len(fib_series) < n:
        next_term = fib_series[-1] + fib_series[-2]
        fib_series.append(next_term)

    return fib_series[:n]

# Example usage:
n_terms = int(input("Enter a number : "))# You can change this to any positive integer
result = fibonacci_series(n_terms)
print(f"The Fibonacci series up to {n_terms} terms is: {result}")
