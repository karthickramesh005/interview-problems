# Write code Check if the given string is Palindrome or not:
def is_palindrome(s):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    s = s.replace(" ", "").lower()

    # Check if the string is the same when read backward
    return s == s[::-1]

# Example usage:
input_string =input("Enter a word : ")

if is_palindrome(input_string):
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")
