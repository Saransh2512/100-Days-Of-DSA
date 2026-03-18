# Implement the solution for this problem.

from collections import deque

# Definition for a binary tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def levelOrder(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level = []
        size = len(queue)

        for _ in range(size):
            node = queue.popleft()
            level.append(node.data)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result


# Example usage
if __name__ == "__main__":
    # Creating a sample tree:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(levelOrder(root))