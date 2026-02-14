#Write a program to check whether a given square matrix is an Identity Matrix. An identity matrix is a square matrix in which all diagonal elements are 1 and all non-diagonal elements are 0.

def is_identity_matrix(matrix):
    n = len(matrix)

    # Check if matrix is square
    for row in matrix:
        if len(row) != n:
            return False

    # Check identity matrix condition
    for i in range(n):
        for j in range(n):
            if i == j:
                if matrix[i][j] != 1:
                    return False
            else:
                if matrix[i][j] != 0:
                    return False

    return True


# Taking input from user
n = int(input("Enter the size of the square matrix: "))
matrix = []

print("Enter the matrix row by row:")
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Check and display result
if is_identity_matrix(matrix):
    print("The matrix is an Identity Matrix.")
else:
    print("The matrix is NOT an Identity Matrix.")

