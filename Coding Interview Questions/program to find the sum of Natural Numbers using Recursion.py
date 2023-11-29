# Write a program to find the sum of Natural Numbers using Recursion. :

def sum_of_natural_numbers(n):
    if n <= 0:
        return 0
    else:
        return n + sum_of_natural_numbers(n - 1)

# Example usage:
n = 5  # You can change this to any positive integer
result = sum_of_natural_numbers(n)

print(f"The sum of the first {n} natural numbers is: {result}")
