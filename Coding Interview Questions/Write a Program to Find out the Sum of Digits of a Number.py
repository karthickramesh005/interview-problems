# Write a Program to Find out the Sum of Digits of a Number :


def sum_of_digits(number):
    # Convert the number to a string to iterate through its digits
    number_str = str(number)

    # Sum the individual digits
    digit_sum = sum(int(digit) for digit in number_str)

    return digit_sum

# Example usage:
input_number = input("Entera numbers : ")  # You can change this to any positive integer
result = sum_of_digits(input_number)

print(f"The sum of digits in {input_number} is: {result}")
