# Write a Program to Find out the Power of a Number :

def power_of_number(base, exponent):
    result = base ** exponent
    return result

# Example usage:
base_number = int(input("Enter a base number : "))
exponent_number = int(input("Enter a exponent number : "))

result = power_of_number(base_number, exponent_number)

print(f"{base_number} raised to the power of {exponent_number} is: {result}")
