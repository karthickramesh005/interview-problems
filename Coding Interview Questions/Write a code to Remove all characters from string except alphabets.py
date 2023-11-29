# Write a code to Remove all characters from string except alphabets :

def keep_only_alphabets(input_string):
    # Use isalpha() to filter alphabets
    result_string = ''.join(char for char in input_string if char.isalpha())
    return result_string

# Example usage:
input_str = "Hello123, World!"

result = keep_only_alphabets(input_str)
print(f"Original String: {input_str}")
print(f"String with only alphabets: {result}")
