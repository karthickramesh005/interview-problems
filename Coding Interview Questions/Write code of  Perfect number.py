# Write code of  Perfect number :
def is_perfect_number(num):
    if num <= 0:
        return False

    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisors_sum == num

# Example usage:
number_to_check = int(input("Enter a number : "))  # You can change this to any positive integer
result = is_perfect_number(number_to_check)

if result:
    print(f"{number_to_check} is a perfect number.")
else:
    print(f"{number_to_check} is not a perfect number.")
