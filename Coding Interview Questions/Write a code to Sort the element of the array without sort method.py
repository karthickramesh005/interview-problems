# Write a code to Sort the element of the array without sort method :

def bubble_sort(arr):
    n = len(arr)

    # Traverse through all elements in the array
    for i in range(n):
        # Last i elements are already in place, so we don't need to check them
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage:
my_array = list(map(int,input("Enter a array elements : ").split()))

print(f"Original Array: {my_array}")

# Sort the array using Bubble Sort
bubble_sort(my_array)

print(f"Sorted Array: {my_array}")
