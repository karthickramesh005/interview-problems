#  Write a code for bubble sort :

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
my_list =list(map(int,input("Enter a elements : ").split()))

print("Original List:", my_list)

bubble_sort(my_list)

print("Sorted List:", my_list)
