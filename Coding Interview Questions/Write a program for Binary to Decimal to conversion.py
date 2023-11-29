# Write a program for Binary to Decimal to conversion :

def binary_to_decimal(binary_str):
    decimal = int(binary_str, 2)
    return decimal

# Example usage:
binary_number = "1101"  # You can change this to any binary number
decimal_result = binary_to_decimal(binary_number)

print(f"The decimal equivalent of binary number '{binary_number}' is: {decimal_result}")
