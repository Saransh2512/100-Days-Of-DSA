# Doubly Linked List Insertion and Traversal - Implement using linked list with dynamic memory allocation.

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# Doubly Linked List class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    # Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    # Insert at specific position (1-based index)
    def insert_at_position(self, data, position):
        if position == 1:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)
        temp = self.head

        for _ in range(position - 2):
            if temp is None:
                print("Position out of range")
                return
            temp = temp.next

        if temp is None:
            print("Position out of range")
            return

        new_node.next = temp.next
        new_node.prev = temp

        if temp.next:
            temp.next.prev = new_node

        temp.next = new_node

    # Traverse forward
    def traverse_forward(self):
        temp = self.head
        print("Forward Traversal:", end=" ")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    # Traverse backward
    def traverse_backward(self):
        temp = self.head

        if temp is None:
            print("List is empty")
            return

        while temp.next:
            temp = temp.next

        print("Backward Traversal:", end=" ")
        while temp:
            print(temp.data, end=" ")
            temp = temp.prev
        print()


# Example usage
dll = DoublyLinkedList()

dll.insert_at_beginning(10)
dll.insert_at_beginning(5)
dll.insert_at_end(20)
dll.insert_at_position(15, 3)

dll.traverse_forward()
dll.traverse_backward()