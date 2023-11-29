#  Write the code to for Armstrong number :

def is_armstrong_number(number):
    num_str = str(number)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    return armstrong_sum == number

# Example usage:
num_to_check = int(input("Enter a number : "))  # You can change this to any positive integer
result = is_armstrong_number(num_to_check)

if result:
    print(f"{num_to_check} is an Armstrong number.")
else:
    print(f"{num_to_check} is not an Armstrong number.")
