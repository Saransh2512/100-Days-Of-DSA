# Implement a Queue using a linked list supporting enqueue and dequeue operations.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, x):
        new_node = Node(x)

        if self.rear is None:
            self.front = self.rear = new_node
            return

        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print(-1)
            return

        temp = self.front
        print(temp.data)
        self.front = self.front.next

        if self.front is None:
            self.rear = None


# Main program
q = Queue()

N = int(input())

for _ in range(N):
    operation = input().split()

    if operation[0] == "enqueue":
        q.enqueue(int(operation[1]))

    elif operation[0] == "dequeue":
        q.dequeue()