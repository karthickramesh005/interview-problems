# Write a code to find circular rotation of an array by K positions. :

def rotate_circular(arr, k):
    n = len(arr)

    # Ensure k is within the range of array length
    k = k % n

    # Rotate the array by K positions
    rotated_array = arr[n - k:] + arr[:n - k]

    return rotated_array

# Example usage:
original_array = [1, 2, 3, 4, 5]
rotation_positions = 2

result = rotate_circular(original_array, rotation_positions)
print(f"Original Array: {original_array}")
print(f"Rotated Array by {rotation_positions} positions: {result}")
