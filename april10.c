//// Given weighted graph with non-negative edges, compute shortest path from source using priority queue.

#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define MAX 100

// Structure for adjacency list
typedef struct Node {
    int vertex;
    int weight;
    struct Node* next;
} Node;

// Structure for graph
typedef struct Graph {
    int V;
    Node* adj[MAX];
} Graph;

// Min Heap Node
typedef struct MinHeapNode {
    int vertex;
    int dist;
} MinHeapNode;

// Min Heap
typedef struct MinHeap {
    int size;
    MinHeapNode heap[MAX];
} MinHeap;

// Create new node
Node* createNode(int v, int w) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->vertex = v;
    newNode->weight = w;
    newNode->next = NULL;
    return newNode;
}

// Create graph
Graph* createGraph(int V) {
    Graph* graph = (Graph*)malloc(sizeof(Graph));
    graph->V = V;

    for (int i = 0; i < V; i++)
        graph->adj[i] = NULL;

    return graph;
}

// Add edge
void addEdge(Graph* graph, int u, int v, int w) {
    Node* newNode = createNode(v, w);
    newNode->next = graph->adj[u];
    graph->adj[u] = newNode;
}

// Swap heap nodes
void swap(MinHeapNode* a, MinHeapNode* b) {
    MinHeapNode temp = *a;
    *a = *b;
    *b = temp;
}

// Heapify
void heapify(MinHeap* h, int i) {
    int smallest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < h->size && h->heap[left].dist < h->heap[smallest].dist)
        smallest = left;

    if (right < h->size && h->heap[right].dist < h->heap[smallest].dist)
        smallest = right;

    if (smallest != i) {
        swap(&h->heap[i], &h->heap[smallest]);
        heapify(h, smallest);
    }
}

// Extract min
MinHeapNode extractMin(MinHeap* h) {
    MinHeapNode root = h->heap[0];
    h->heap[0] = h->heap[h->size - 1];
    h->size--;
    heapify(h, 0);
    return root;
}

// Insert into heap
void insertHeap(MinHeap* h, int v, int dist) {
    int i = h->size++;
    h->heap[i].vertex = v;
    h->heap[i].dist = dist;

    while (i && h->heap[i].dist < h->heap[(i - 1) / 2].dist) {
        swap(&h->heap[i], &h->heap[(i - 1) / 2]);
        i = (i - 1) / 2;
    }
}

// Dijkstra Algorithm
void dijkstra(Graph* graph, int src) {
    int V = graph->V;
    int dist[MAX];

    MinHeap heap;
    heap.size = 0;

    // Initialize distances
    for (int i = 0; i < V; i++)
        dist[i] = INT_MAX;

    dist[src] = 0;
    insertHeap(&heap, src, 0);

    while (heap.size > 0) {
        MinHeapNode minNode = extractMin(&heap);
        int u = minNode.vertex;

        Node* temp = graph->adj[u];

        while (temp != NULL) {
            int v = temp->vertex;
            int weight = temp->weight;

            if (dist[u] != INT_MAX && dist[u] + weight < dist[v]) {
                dist[v] = dist[u] + weight;
                insertHeap(&heap, v, dist[v]);
            }

            temp = temp->next;
        }
    }

    // Print result
    printf("Vertex\tDistance from Source\n");
    for (int i = 0; i < V; i++)
        printf("%d\t%d\n", i, dist[i]);
}

// Main function
int main() {
    Graph* graph = createGraph(5);

    addEdge(graph, 0, 1, 10);
    addEdge(graph, 0, 4, 5);
    addEdge(graph, 1, 2, 1);
    addEdge(graph, 4, 1, 3);
    addEdge(graph, 4, 2, 9);
    addEdge(graph, 4, 3, 2);
    addEdge(graph, 3, 2, 4);

    dijkstra(graph, 0);

    return 0;
}