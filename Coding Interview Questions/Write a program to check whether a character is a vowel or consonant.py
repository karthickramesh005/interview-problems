# Write a program to check whether a character is a vowel or consonant :
def check_vowel_consonant(char):
    # Convert the character to lowercase for case-insensitive comparison
    char = char.lower()

    # Check if the character is a vowel or consonant
    if char.isalpha():
        if char in "aeiou":
            return f"The character '{char}' is a vowel."
        else:
            return f"The character '{char}' is a consonant."
    else:
        return f"The input '{char}' is not a valid alphabet character."

# Example usage:
input_char = input("Enter a caractor : ")  # You can change this to any alphabet character
result = check_vowel_consonant(input_char)

print(result)
