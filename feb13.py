#You are given a rectangular matrix of integers. Starting from the outer boundary, traverse the matrix in a clockwise manner and continue moving inward layer by layer until all elements are visited.

def spiral(matrix):
    ans = []
    
    if matrix == []:
        return ans
    
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        
        for i in range(left, right + 1):
            ans.append(matrix[top][i])
        top = top + 1
        
        for i in range(top, bottom + 1):
            ans.append(matrix[i][right])
        right = right - 1
    
        if top <= bottom:
            for i in range(right, left - 1, -1):
                ans.append(matrix[bottom][i])
            bottom = bottom - 1
        
        if left <= right:
            for i in range(bottom, top - 1, -1):
                ans.append(matrix[i][left])
            left = left + 1
    
    return ans

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(spiral(matrix))