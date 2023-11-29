# Write a code to Sort the element of the array :

def sort_array(arr):
    sorted_arr = sorted(arr)
    return sorted_arr

# Example usage:
my_array = list(map(int,input("Enter a array elements : ").split()))

result = sort_array(my_array)

print(f"Original Array: {my_array}")
print(f"Sorted Array: {result}")
