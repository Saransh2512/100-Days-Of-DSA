# Given a queue of integers, reverse the queue using a stack.

from collections import deque

def reverse_queue(q):
    stack = []

    # Step 1: Dequeue all elements and push into stack
    while q:
        stack.append(q.popleft())

    # Step 2: Pop from stack and enqueue back
    while stack:
        q.append(stack.pop())

    return q


# Example usage
queue = deque([1, 2, 3, 4, 5])

print("Original Queue:", list(queue))

reverse_queue(queue)

print("Reversed Queue:", list(queue))