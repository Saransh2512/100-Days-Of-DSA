# Find the Lowest Common Ancestor (LCA) of two nodes in a Binary Tree.

from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(arr):
    if not arr or arr[0] == -1:
        return None

    root = Node(arr[0])
    queue = deque([root])
    i = 1

    while queue and i < len(arr):
        curr = queue.popleft()

        if arr[i] != -1:
            curr.left = Node(arr[i])
            queue.append(curr.left)
        i += 1

        if i < len(arr) and arr[i] != -1:
            curr.right = Node(arr[i])
            queue.append(curr.right)
        i += 1

    return root

def find_lca(root, p, q):
    if not root:
        return None

    if root.val == p or root.val == q:
        return root

    left = find_lca(root.left, p, q)
    right = find_lca(root.right, p, q)

    if left and right:
        return root

    return left if left else right

n = int(input())
arr = list(map(int, input().split()))
p, q = map(int, input().split())

root = build_tree(arr)
lca_node = find_lca(root, p, q)

print(lca_node.val if lca_node else -1)