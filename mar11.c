//Implement a Min Heap using an array where the smallest element is always at the root.
//Supported Operations:
//- insert x
//- extractMin
//- peek

#include <stdio.h>
#include <limits.h>

#define MAX 100

int heap[MAX];
int size = 0;

// Swap function
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Heapify Up
void heapifyUp(int index) {
    int parent = (index - 1) / 2;

    while (index > 0 && heap[parent] > heap[index]) {
        swap(&heap[parent], &heap[index]);
        index = parent;
        parent = (index - 1) / 2;
    }
}

// Heapify Down
void heapifyDown(int index) {
    int smallest = index;
    int left = 2 * index + 1;
    int right = 2 * index + 2;

    if (left < size && heap[left] < heap[smallest])
        smallest = left;

    if (right < size && heap[right] < heap[smallest])
        smallest = right;

    if (smallest != index) {
        swap(&heap[index], &heap[smallest]);
        heapifyDown(smallest);
    }
}

// Insert element
void insert(int value) {
    if (size == MAX) {
        printf("Heap Overflow\n");
        return;
    }

    heap[size] = value;
    heapifyUp(size);
    size++;
}

// Peek minimum
int peek() {
    if (size == 0) {
        printf("Heap is empty\n");
        return -1;
    }
    return heap[0];
}

// Extract minimum
int extractMin() {
    if (size == 0) {
        printf("Heap is empty\n");
        return INT_MIN;
    }

    int min = heap[0];
    heap[0] = heap[size - 1];
    size--;

    heapifyDown(0);

    return min;
}

// Display heap
void display() {
    for (int i = 0; i < size; i++)
        printf("%d ", heap[i]);
    printf("\n");
}

int main() {

    insert(10);
    insert(4);
    insert(15);
    insert(20);
    insert(0);

    printf("Heap elements: ");
    display();

    printf("Min element (peek): %d\n", peek());

    printf("Extracted Min: %d\n", extractMin());

    printf("Heap after extraction: ");
    display();

    return 0;
}