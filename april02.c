// Build a graph with n vertices and m edges using adjacency matrix representation. The graph may be directed or undirected.

#include <stdio.h>

int main() {
    int n, m;
    
    // Input number of vertices and edges
    scanf("%d %d", &n, &m);

    // Create adjacency matrix and initialize with 0
    int adj[n][n];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            adj[i][j] = 0;
        }
    }

    int u, v;

    // Input edges
    for (int i = 0; i < m; i++) {
        scanf("%d %d", &u, &v);

        // For undirected graph
        adj[u][v] = 1;
        adj[v][u] = 1;

        // 👉 For directed graph, use ONLY:
        // adj[u][v] = 1;
    }

    // Print adjacency matrix
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("%d ", adj[i][j]);
        }
        printf("\n");
    }

    return 0;
}