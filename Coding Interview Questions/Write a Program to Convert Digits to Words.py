# Write a Program to Convert Digits to Words. :

def digit_to_word(digit):
    words = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    return words[int(digit)]

def number_to_words(number):
    number_str = str(number)
    result = ' '.join(digit_to_word(digit) for digit in number_str)
    return result

# Example usage:
input_number = int(input("Enter a number : "))  # You can change this to any positive integer
result = number_to_words(input_number)

print(f"The words for the digits in {input_number} are: {result}")
