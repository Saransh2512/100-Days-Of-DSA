#A Deque is a linear data structure that allows insertion and deletion of elements from both the front and the rear. It provides more flexibility than a standard queue or stack.

from collections import deque

# Create a deque
dq = deque()

# push_back (insert at rear)
dq.append(10)
dq.append(20)

# push_front (insert at front)
dq.appendleft(5)

print("Deque after insertions:", dq)

# front element
print("Front element:", dq[0])

# back element
print("Back element:", dq[-1])

# pop_front
dq.popleft()
print("After pop_front:", dq)

# pop_back
dq.pop()
print("After pop_back:", dq)

# size
print("Size of deque:", len(dq))

# check empty
if len(dq) == 0:
    print("Deque is empty")
else:
    print("Deque is not empty")