# BST Insert

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.data:
        root.left = insert(root.left, key)
    elif key > root.data:
        root.right = insert(root.right, key)

    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

root = None
values = [5, 3, 7, 2, 4]

for v in values:
    root = insert(root, v)

inorder(root)  