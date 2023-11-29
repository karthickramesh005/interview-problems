# Write code to Calculate frequency of characters in a string :
def character_frequency(input_string):
    # Initialize an empty dictionary to store character frequencies
    frequency_dict = {}

    # Iterate through each character in the string
    for char in input_string:
        # Increment the count for the character in the dictionary
        frequency_dict[char] = frequency_dict.get(char, 0) + 1

    return frequency_dict

# Example usage:
input_string = "hello world"

result = character_frequency(input_string)
print(f"Character frequencies in '{input_string}': {result}")
