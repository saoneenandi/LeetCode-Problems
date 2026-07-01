#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define INF 1000000000

// Structure to hold coordinates for BFS Queue and Priority Queue
typedef struct {
    int r, c;
    int safeness;
} Cell;

// --- Queue Implementation for Multi-Source BFS ---
typedef struct {
    Cell* data;
    int front;
    int rear;
    int capacity;
} Queue;

Queue* createQueue(int capacity) {
    Queue* q = (Queue*)malloc(sizeof(Queue));
    q->data = (Cell*)malloc(sizeof(Cell) * capacity);
    q->front = 0;
    q->rear = 0;
    q->capacity = capacity;
    return q;
}

void enqueue(Queue* q, int r, int c) {
    q->data[q->rear++] = (Cell){r, c, 0};
}

Cell dequeue(Queue* q) {
    return q->data[q->front++];
}

bool isQueueEmpty(Queue* q) {
    return q->front == q->rear;
}

void freeQueue(Queue* q) {
    free(q->data);
    free(q);
}

// --- Max-Heap (Priority Queue) Implementation for Dijkstra ---
typedef struct {
    Cell* data;
    int size;
    int capacity;
} MaxHeap;

MaxHeap* createMaxHeap(int capacity) {
    MaxHeap* heap = (MaxHeap*)malloc(sizeof(MaxHeap));
    heap->data = (Cell*)malloc(sizeof(Cell) * capacity);
    heap->size = 0;
    heap->capacity = capacity;
    return heap;
}

void swap(Cell* a, Cell* b) {
    Cell temp = *a;
    *a = *b;
    *b = temp;
}

void pushHeap(MaxHeap* heap, int r, int c, int safeness) {
    heap->data[heap->size] = (Cell){r, c, safeness};
    int i = heap->size;
    heap->size++;
    
    // Up-heapify
    while (i > 0) {
        int parent = (i - 1) / 2;
        if (heap->data[i].safeness > heap->data[parent].safeness) {
            swap(&heap->data[i], &heap->data[parent]);
            i = parent;
        } else {
            break;
        }
    }
}

Cell popHeap(MaxHeap* heap) {
    Cell top = heap->data[0];
    heap->size--;
    heap->data[0] = heap->data[heap->size];
    
    int i = 0;
    // Down-heapify
    while (2 * i + 1 < heap->size) {
        int left = 2 * i + 1;
        int right = 2 * i + 2;
        int largest = left;
        
        if (right < heap->size && heap->data[right].safeness > heap->data[left].safeness) {
            largest = right;
        }
        
        if (heap->data[largest].safeness > heap->data[i].safeness) {
            swap(&heap->data[i], &heap->data[largest]);
            i = largest;
        } else {
            break;
        }
    }
    return top;
}

bool isHeapEmpty(MaxHeap* heap) {
    return heap->size == 0;
}

void freeHeap(MaxHeap* heap) {
    free(heap->data);
    free(heap);
}

// --- Main Solution Function ---
int maximumSafenessFactor(int** grid, int gridSize, int* gridColSize) {
    int n = gridSize;

    // Quick exit if start or end has a thief
    if (grid[0][0] == 1 || grid[n - 1][n - 1] == 1) {
        return 0;
    }

    // Allocate memory for the distance matrix
    int** dist = (int**)malloc(sizeof(int*) * n);
    for (int i = 0; i < n; i++) {
        dist[i] = (int*)malloc(sizeof(int) * n);
        for (int j = 0; j < n; j++) {
            dist[i][j] = INF;
        }
    }

    // Multi-source BFS Queue initialization
    Queue* q = createQueue(n * n);

    for (int r = 0; r < n; r++) {
        for (int c = 0; c < n; c++) {
            if (grid[r][c] == 1) {
                dist[r][c] = 0;
                enqueue(q, r, c);
            }
        }
    }

    int dr[] = {0, 0, 1, -1};
    int dc[] = {1, -1, 0, 0};

    // Step 1: Multi-source BFS to calculate proximity to closest thief
    while (!isQueueEmpty(q)) {
        Cell curr = dequeue(q);
        for (int i = 0; i < 4; i++) {
            int nr = curr.r + dr[i];
            int nc = curr.c + dc[i];
            
            if (nr >= 0 && nr < n && nc >= 0 && nc < n && dist[nr][nc] == INF) {
                dist[nr][nc] = dist[curr.r][curr.c] + 1;
                enqueue(q, nr, nc);
            }
        }
    }
    freeQueue(q);

    // Step 2: Modified Dijkstra using Max-Heap
    MaxHeap* heap = createMaxHeap(n * n);
    
    // Visited table tracking
    bool** visited = (bool**)malloc(sizeof(bool*) * n);
    for (int i = 0; i < n; i++) {
        visited[i] = (bool*)calloc(n, sizeof(bool));
    }

    pushHeap(heap, 0, 0, dist[0][0]);
    visited[0][0] = true;

    int ans = 0;

    while (!isHeapEmpty(heap)) {
        Cell curr = popHeap(heap);
        
        // If we reached the bottom-right corner, we have found our answer
        if (curr.r == n - 1 && curr.c == n - 1) {
            ans = curr.safeness;
            break;
        }

        for (int i = 0; i < 4; i++) {
            int nr = curr.r + dr[i];
            int nc = curr.c + dc[i];

            if (nr >= 0 && nr < n && nc >= 0 && nc < n && !visited[nr][nc]) {
                visited[nr][nc] = true;
                // The minimum safeness metric bottleneck down the line
                int next_safeness = (curr.safeness < dist[nr][nc]) ? curr.safeness : dist[nr][nc];
                pushHeap(heap, nr, nc, next_safeness);
            }
        }
    }

    // Free all dynamically allocated memory
    freeHeap(heap);
    for (int i = 0; i < n; i++) {
        free(dist[i]);
        free(visited[i]);
    }
    free(dist);
    free(visited);

    return ans;
}