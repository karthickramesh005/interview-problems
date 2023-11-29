# Write a code to Print the smallest element of the array :


def find_smallest_element(arr):
    if not arr:
        return None  # Return None for an empty array

    smallest_element = min(arr)
    return smallest_element

# Example usage:
my_array =list(map(int,input().split()))

result = find_smallest_element(my_array)

if result is not None:
    print(f"The smallest element in the array is: {result}")
else:
    print("The array is empty.")
