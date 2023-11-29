# Write a code to replace each element in an array by its rank in the array :

def replace_with_rank(arr):
    # Create a sorted copy of the array to get the ranks
    sorted_arr = sorted(arr)
    
    # Create a dictionary to store the rank of each element
    rank_dict = {element: rank + 1 for rank, element in enumerate(sorted_arr)}
    
    # Replace each element with its rank
    ranked_arr = [rank_dict[element] for element in arr]
    
    return ranked_arr

# Example usage:
input_array = [10, 5, 8, 15, 2]

result = replace_with_rank(input_array)
print(f"Original Array: {input_array}")
print(f"Array with Ranks: {result}")
