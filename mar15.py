# Construct a Binary Tree from the given level-order traversal.

from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def buildTree(arr):
    if not arr:
        return None

    root = Node(arr[0])
    q = deque([root])
    i = 1

    while q and i < len(arr):
        node = q.popleft()

        if arr[i] is not None:
            node.left = Node(arr[i])
            q.append(node.left)
        i += 1

        if i < len(arr) and arr[i] is not None:
            node.right = Node(arr[i])
            q.append(node.right)
        i += 1

    return root


# test
arr = [1,2,3,4,5,None,7]
root = buildTree(arr)

print(root.val)
print(root.left.val)
print(root.right.val)