# Find the height (maximum depth) of a given binary tree.

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
        current = q.popleft()

        if i < len(arr) and arr[i] != -1:
            current.left = Node(arr[i])
            q.append(current.left)
        i += 1

        if i < len(arr) and arr[i] != -1:
            current.right = Node(arr[i])
            q.append(current.right)
        i += 1

    return root


def height(root):
    if root is None:
        return 0

    left = height(root.left)
    right = height(root.right)

    return max(left, right) + 1


# Input
n = int(input())
arr = list(map(int, input().split()))

root = build_tree(arr)

print(height(root))