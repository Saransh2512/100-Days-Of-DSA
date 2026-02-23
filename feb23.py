# Merge Two Sorted Linked Lists - Implement using linked list with dynamic memory allocation.

# Define Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Function to merge two sorted linked lists
def merge_lists(head1, head2):
    merged_head = None
    merged_tail = None

    while head1 and head2:
        if head1.data <= head2.data:
            value = head1.data
            head1 = head1.next
        else:
            value = head2.data
            head2 = head2.next

        new_node = Node(value)

        if merged_head is None:
            merged_head = new_node
            merged_tail = new_node
        else:
            merged_tail.next = new_node
            merged_tail = new_node

    # Add remaining nodes from list1
    while head1:
        new_node = Node(head1.data)
        merged_tail.next = new_node
        merged_tail = new_node
        head1 = head1.next

    # Add remaining nodes from list2
    while head2:
        new_node = Node(head2.data)
        merged_tail.next = new_node
        merged_tail = new_node
        head2 = head2.next

    return merged_head


# Helper function to insert at end
def insert_end(head, data):
    new_node = Node(data)
    if head is None:
        return new_node

    temp = head
    while temp.next:
        temp = temp.next
    temp.next = new_node
    return head


# Function to print linked list
def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")


# Example usage
if __name__ == "__main__":
    list1 = None
    list2 = None

    # Create first sorted list: 1 -> 3 -> 5
    list1 = insert_end(list1, 1)
    list1 = insert_end(list1, 3)
    list1 = insert_end(list1, 5)

    # Create second sorted list: 2 -> 4 -> 6
    list2 = insert_end(list2, 2)
    list2 = insert_end(list2, 4)
    list2 = insert_end(list2, 6)

    print("List 1:")
    print_list(list1)

    print("List 2:")
    print_list(list2)

    merged = merge_lists(list1, list2)

    print("Merged List:")
    print_list(merged)