// Implement a hash table using quadratic probing with formula:

#include <stdio.h>
#include <string.h>

#define EMPTY -1

int table[100];  // assuming max size
int m;

// Insert using quadratic probing
void insert(int key) {
    int h = key % m;

    for (int i = 0; i < m; i++) {
        int index = (h + i * i) % m;

        if (table[index] == EMPTY) {
            table[index] = key;
            return;
        }
    }
}

// Search using quadratic probing
int search(int key) {
    int h = key % m;

    for (int i = 0; i < m; i++) {
        int index = (h + i * i) % m;

        if (table[index] == EMPTY)
            return 0;  // NOT FOUND

        if (table[index] == key)
            return 1;  // FOUND
    }
    return 0;
}

int main() {
    int q;
    scanf("%d", &m);
    scanf("%d", &q);

    // Initialize table
    for (int i = 0; i < m; i++)
        table[i] = EMPTY;

    while (q--) {
        char op[10];
        int x;
        scanf("%s %d", op, &x);

        if (strcmp(op, "INSERT") == 0) {
            insert(x);
        } 
        else if (strcmp(op, "SEARCH") == 0) {
            if (search(x))
                printf("FOUND\n");
            else
                printf("NOT FOUND\n");
        }
    }

    return 0;
}