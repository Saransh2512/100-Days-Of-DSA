//Perform BFS from a given source using queue.

#include <stdio.h>
#include <stdbool.h>

#define MAX 100

// Queue implementation
int queue[MAX];
int front = 0, rear = 0;

void enqueue(int x) {
    queue[rear++] = x;
}

int dequeue() {
    return queue[front++];
}

bool isEmpty() {
    return front == rear;
}

// BFS function
void bfs(int n, int adj[MAX][MAX], int s) {
    bool visited[MAX] = {false};

    enqueue(s);
    visited[s] = true;

    while (!isEmpty()) {
        int node = dequeue();
        printf("%d ", node);

        for (int i = 0; i < n; i++) {
            if (adj[node][i] == 1 && !visited[i]) {
                enqueue(i);
                visited[i] = true;
            }
        }
    }
}

int main() {
    int n = 5;
    
    // Adjacency matrix
    int adj[MAX][MAX] = {
        {0, 1, 1, 0, 0},
        {1, 0, 0, 1, 0},
        {1, 0, 0, 0, 1},
        {0, 1, 0, 0, 0},
        {0, 0, 1, 0, 0}
    };

    int source = 0;

    printf("BFS Traversal: ");
    bfs(n, adj, source);

    return 0;
}