# Perform zigzag (spiral) level order traversal of a binary tree. Alternate levels should be traversed left-to-right and right-to-left.

from collections import deque

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def build_tree(arr):
    if not arr or arr[0] == -1:
        return None
    
    root = Node(arr[0])
    q = deque([root])
    
    i = 1
    while q and i < len(arr):
        curr = q.popleft()
        
        if arr[i] != -1:
            curr.left = Node(arr[i])
            q.append(curr.left)
        i += 1
        
        if i < len(arr) and arr[i] != -1:
            curr.right = Node(arr[i])
            q.append(curr.right)
        i += 1
    
    return root

def zigzag_traversal(root):
    if not root:
        return []
    
    result = []
    q = deque([root])
    left_to_right = True
    
    while q:
        size = len(q)
        level = [0] * size
        
        for i in range(size):
            curr = q.popleft()
            
            index = i if left_to_right else size - 1 - i
            level[index] = curr.data
            
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        
        result.extend(level)
        left_to_right = not left_to_right
    
    return result

n = int(input())
arr = list(map(int, input().split()))

root = build_tree(arr)
ans = zigzag_traversal(root)

print(*ans)