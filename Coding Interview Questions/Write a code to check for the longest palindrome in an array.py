#  Write a code to check for the longest palindrome in an array. :

def longest_palindrome(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest = ""
    for i in range(len(s)):
        # Check palindrome with odd length
        palindrome_odd = expand_around_center(i, i)
        if len(palindrome_odd) > len(longest):
            longest = palindrome_odd

        # Check palindrome with even length
        palindrome_even = expand_around_center(i, i + 1)
        if len(palindrome_even) > len(longest):
            longest = palindrome_even

    return longest

# Example usage:
input_string = "babad"

result = longest_palindrome(input_string)
print(f"The longest palindrome in '{input_string}' is: {result}")
