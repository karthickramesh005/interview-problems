#  Write a code to Reverse the element of the array :

def reverse_array(arr):
    reversed_arr = arr[::-1]
    return reversed_arr

# Example usage:
my_array = list(map(int,input("Enter a array elemets : ").split()))

result = reverse_array(my_array)

print(f"Original Array: {my_array}")
print(f"Reversed Array: {result}")
