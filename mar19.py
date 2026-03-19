# Height of Binary Tree

from collections import deque

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def height(root):   # ✅ define first
    if root is None:
        return 0

    q = deque([root])
    h = 0

    while q:
        for _ in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        h += 1

    return h


# Create tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Call function
print("Height:", height(root))   # ✅ works