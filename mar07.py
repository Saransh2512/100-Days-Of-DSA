#Queue Using Array - Implement using linked list with dynamic memory allocation.
#Input:
#- First line: integer n (number of elements)
#- Second line: n space-separated integers
#Output:
#- Print queue elements from front to rear, space-separated

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new = Node(value)
        if self.rear is None:
            self.front = self.rear = new
        else:
            self.rear.next = new
            self.rear = new

    def display(self):
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

try:
    n = int(input().strip())
    arr = list(map(int, input().split()))

    q = Queue()
    for i in arr:
        q.enqueue(i)

    q.display()

except:
    print("Invalid input")