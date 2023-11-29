# Write a program to add Two Matrices using Multi-dimensional Array :

def add_matrices(mat1, mat2):
    # Check if the matrices have the same dimensions
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        print("Matrices have different dimensions. Addition is not possible.")
        return None

    # Create a result matrix filled with zeros
    result = [[0 for _ in range(len(mat1[0]))] for _ in range(len(mat1))]

    # Perform matrix addition
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            result[i][j] = mat1[i][j] + mat2[i][j]

    return result

# Example usage:
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

result_matrix = add_matrices(matrix1, matrix2)

if result_matrix:
    print("Matrix 1:")
    for row in matrix1:
        print(row)

    print("\nMatrix 2:")
    for row in matrix2:
        print(row)

    print("\nSum of Matrices:")
    for row in result_matrix:
        print(row)
