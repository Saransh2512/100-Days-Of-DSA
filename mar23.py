# Find the Lowest Common Ancestor (LCA) of two nodes in a Binary Search Tree.

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root


def findLCA(root, p, q):
    while root:
        if p < root.val and q < root.val:
            root = root.left
        elif p > root.val and q > root.val:
            root = root.right
        else:
            return root.val

if __name__ == "__main__":
    n = int(input())
    values = list(map(int, input().split()))
    p, q = map(int, input().split())

    root = None
    for val in values:
        root = insert(root, val)

    result = findLCA(root, p, q)
    print(result)