#  Write a code to find the factorial of a number :
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage:
number = int(input("Enter a number : "))  # You can change this to any non-negative integer
result = factorial(number)
print(f"The factorial of {number} is: {result}")
