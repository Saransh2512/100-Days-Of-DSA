# Given a binary tree, print its vertical order traversal. Nodes that lie on the same vertical line should be printed together from top to bottom and from left to right.

from collections import defaultdict, deque

class Node:
    def __init__(self, val):
        self.val = val
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
    
        if i < len(arr) and arr[i] != -1:
            curr.left = Node(arr[i])
            q.append(curr.left)
        i += 1
        
        if i < len(arr) and arr[i] != -1:
            curr.right = Node(arr[i])
            q.append(curr.right)
        i += 1
    
    return root

def vertical_order(root):
    if not root:
        return
    
    hd_map = defaultdict(list)
    q = deque([(root, 0)])
    
    while q:
        node, hd = q.popleft()
        hd_map[hd].append(node.val)
        
        if node.left:
            q.append((node.left, hd - 1))
        if node.right:
            q.append((node.right, hd + 1))
    
    for hd in sorted(hd_map):
        print(*hd_map[hd])

n = int(input())
arr = list(map(int, input().split()))

root = build_tree(arr)
vertical_order(root)