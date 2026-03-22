# BST Search

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def search(root, key):
    if root is None or root.key == key:
        return root
    if key < root.key:
        return search(root.left, key)
    return search(root.right, key)

# Build tree
root = Node(10)
root.left = Node(5)
root.right = Node(15)

# Search
result = search(root, 5)

# Output
if result:
    print("Found:", result.key)
else:
    print("Not Found")