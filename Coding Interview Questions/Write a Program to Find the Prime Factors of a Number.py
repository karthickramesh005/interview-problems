# Write a Program to Find the Prime Factors of a Number. :


def prime_factors(number):
    factors = []
    divisor = 2

    while divisor <= number:
        if number % divisor == 0:
            factors.append(divisor)
            number = number // divisor
        else:
            divisor += 1

    return factors

# Example usage:
input_number = int(input("Enter a number : "))  # You can change this to any positive integer
result = prime_factors(input_number)

print(f"The prime factors of {input_number} are: {result}")
