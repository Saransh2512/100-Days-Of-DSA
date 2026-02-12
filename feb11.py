# Write a program to check whether a given matrix is symmetric.A matrix is said to be symmetric if it is a square matrix and is equal to its transpose (i.e., element at position [i][j] is equal to element at position [j][i] for all valid i and j).

m, n = map(int, input("Enter rows and columns: ").split())

if m != n:
    print("Not a Symmetric Matrix")
    exit()

matrix = []
print("Enter the matrix row by row:")

for _ in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)

is_symmetric = True

for i in range(m):
    for j in range(i + 1, n):
        if matrix[i][j] != matrix[j][i]:
            is_symmetric = False
            break
    if not is_symmetric:
        break

if is_symmetric:
    print("Symmetric Matrix")
else:
    print("Not a Symmetric Matrix")
