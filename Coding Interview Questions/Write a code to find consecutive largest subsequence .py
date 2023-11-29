#  Write a code to find consecutive largest subsequence :

def consecutive_largest_subsequence(arr):
    arr_set = set(arr)
    longest_subsequence = []
    
    for num in arr_set:
        if num - 1 not in arr_set:
            current_num = num
            current_subsequence = [current_num]

            while current_num + 1 in arr_set:
                current_num += 1
                current_subsequence.append(current_num)

            if len(current_subsequence) > len(longest_subsequence):
                longest_subsequence = current_subsequence

    return longest_subsequence

# Example usage:
my_array = [1, 2, 5, 6, 8, 9, 10, 11, 12, 15]

result = consecutive_largest_subsequence(my_array)

print(f"The consecutive largest subsequence is: {result}")
