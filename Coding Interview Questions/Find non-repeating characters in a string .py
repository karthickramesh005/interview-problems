#  Find non-repeating characters in a string :

def non_repeating_characters(input_string):
    char_count = {}
    
    # Count the occurrences of each character in the string
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Filter characters with count 1 (non-repeating)
    non_repeating_chars = [char for char, count in char_count.items() if count == 1]
    
    return non_repeating_chars

# Example usage:
input_str = "aabbccdeeff"

result = non_repeating_characters(input_str)
print(f"Non-repeating characters in '{input_str}': {result}")
