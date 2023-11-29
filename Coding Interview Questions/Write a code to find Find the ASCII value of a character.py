#  Write a code to find Find the ASCII value of a character :

def find_ascii_value(character):
    # Use the ord() function to get the ASCII value of the character
    ascii_value = ord(character)
    return ascii_value

# Example usage:`
input_char = input("Enter a caractor : ") # You can change this to any character
ascii_result = find_ascii_value(input_char)

print(f"The ASCII value of '{input_char}' is: {ascii_result}")
