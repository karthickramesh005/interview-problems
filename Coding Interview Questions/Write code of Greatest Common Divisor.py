#  Write code of Greatest Common Divisor :
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage:
num1 =int(input("Enter a first number : "))
num2 =int(input("Enter a second number : "))

result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is: {result}")
