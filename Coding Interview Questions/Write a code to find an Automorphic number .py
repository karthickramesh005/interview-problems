# Write a code to find an Automorphic number :

def is_automorphic(number):
    square = number ** 2
    num_digits = len(str(number))

    # Compare the last digits of the square with the original number
    return square % (10 ** num_digits) == number

# Example usage:
input_number = int(input("Enter a number : "))  # You can change this to any non-negative integer
result = is_automorphic(input_number)

if result:
    print(f"{input_number} is an Automorphic number.")
else:
    print(f"{input_number} is not an Automorphic number.")
