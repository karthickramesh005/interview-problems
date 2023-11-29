#  Write code to check if two strings match where one string contains wildcard characters :

import fnmatch

def is_match_with_wildcards(pattern, string):
    return fnmatch.fnmatch(string, pattern)

# Example usage:
wildcard_pattern = "h*llo"  # '*' can match any sequence of characters
test_string = "hello"

if is_match_with_wildcards(wildcard_pattern, test_string):
    print(f"'{test_string}' matches the pattern '{wildcard_pattern}'.")
else:
    print(f"'{test_string}' does not match the pattern '{wildcard_pattern}'.")
