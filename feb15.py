#Write a program to check whether a given square matrix is an Identity Matrix. An identity matrix is a square matrix in which all diagonal elements are 1 and all non-diagonal elements are 0.

def is_identity_matrix(matrix):
    n = len(matrix)

    for row in matrix:
        if len(row) != n:
            return False

    for i in range(n):
        for j in range(n):
            if i == j:
                if matrix[i][j] != 1:
                    return False
            else:
                if matrix[i][j] != 0:
                    return False

    return True

matrix = []
n = int(input("Enter size of square matrix: "))

print("Enter matrix elements row-wise:")
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

if is_identity_matrix(matrix):
    print("The matrix is an Identity Matrix.")
else:
    print("The matrix is NOT an Identity Matrix.")
