# Write a Program to Add two Fractions :

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def add_fractions(num1, denom1, num2, denom2):
    # Find the least common multiple (LCM) of denominators
    lcm = (denom1 * denom2) // gcd(denom1, denom2)

    # Calculate the new numerators
    new_num1 = num1 * (lcm // denom1)
    new_num2 = num2 * (lcm // denom2)

    # Add the numerators
    sum_num = new_num1 + new_num2

    # Simplify the result
    common_divisor = gcd(sum_num, lcm)
    
    # Calculate the simplified fraction
    result_num = sum_num // common_divisor
    result_denom = lcm // common_divisor

    return result_num, result_denom

# Example usage:
numerator1 = 1
denominator1 = 4

numerator2 = 2
denominator2 = 5

result_numerator, result_denominator = add_fractions(numerator1, denominator1, numerator2, denominator2)

print(f"The sum of {numerator1}/{denominator1} and {numerator2}/{denominator2} is: {result_numerator}/{result_denominator}")
