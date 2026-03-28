# Check whether a given binary tree is symmetric around its center.

from collections import deque

# Define Tree Node
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Build tree from level order
def build_tree(values):
    if not values or values[0] == -1:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        current = queue.popleft()

        # Left child
        if i < len(values) and values[i] != -1:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1

        # Right child
        if i < len(values) and values[i] != -1:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    return root

# Check symmetry
def is_mirror(t1, t2):
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False
    return (t1.val == t2.val and
            is_mirror(t1.left, t2.right) and
            is_mirror(t1.right, t2.left))

def is_symmetric(root):
    if not root:
        return True
    return is_mirror(root.left, root.right)

# -------- MAIN --------
n = int(input())
values = list(map(int, input().split()))

root = build_tree(values)

print("YES" if is_symmetric(root) else "NO")