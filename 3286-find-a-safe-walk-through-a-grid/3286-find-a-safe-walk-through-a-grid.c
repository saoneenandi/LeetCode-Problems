#include <stdbool.h>
#include <stdlib.h>

// Structure to represent a cell in our queue
typedef struct {
    int r;
    int c;
} Point;

bool findSafeWalk(int** grid, int gridSize, int* gridColSize, int health) {
    int m = gridSize;
    int n = gridColSize[0];
    
    // max_health[i][j] will store the maximum health we can have when reaching cell (i, j)
    // Initialize all cells to -1 (unvisited/unreachable)
    int** max_health = (int**)malloc(m * sizeof(int*));
    for (int i = 0; i < m; i++) {
        max_health[i] = (int*)malloc(n * sizeof(int));
        for (int j = 0; j < n; j++) {
            max_health[i][j] = -1;
        }
    }
    
    // Direction vectors for moving up, down, left, right
    int dr[] = {-1, 1, 0, 0};
    int dc[] = {0, 0, -1, 1};
    
    // Simple Queue for BFS (Max possible elements in queue is m * n * 4 in worst case)
    Point* queue = (Point*)malloc(m * n * 10 * sizeof(Point));
    int head = 0;
    int tail = 0;
    
    // Starting point (0, 0)
    int starting_health = health - grid[0][0];
    if (starting_health <= 0) {
        // If starting cell drops health to 0 or less, we can't move
        // Free allocated memory before returning
        for (int i = 0; i < m; i++) free(max_health[i]);
        free(max_health);
        free(queue);
        return false;
    }
    
    max_health[0][0] = starting_health;
    queue[tail++] = (Point){0, 0};
    
    // BFS Loop
    while (head < tail) {
        Point curr = queue[head++];
        int r = curr.r;
        int c = curr.c;
        int curr_h = max_health[r][c];
        
        // If we reached the destination with valid health, we can safely stop early
        if (r == m - 1 && c == n - 1 && curr_h >= 1) {
            // Free memory
            for (int i = 0; i < m; i++) free(max_health[i]);
            free(max_health);
            free(queue);
            return true;
        }
        
        // Explore neighbors
        for (int i = 0; i < 4; i++) {
            int nr = r + dr[i];
            int nc = c + dc[i];
            
            // Check boundaries
            if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                int next_h = curr_h - grid[nr][nc];
                
                // We only proceed if next health is positive and strictly better 
                // than any previous path found to this cell
                if (next_h >= 1 && next_h > max_health[nr][nc]) {
                    max_health[nr][nc] = next_h;
                    queue[tail++] = (Point){nr, nc};
                }
            }
        }
    }
    
    // Check if destination was reached with at least 1 health
    bool result = max_health[m - 1][n - 1] >= 1;
    
    // Cleanup Memory
    for (int i = 0; i < m; i++) {
        free(max_health[i]);
    }
    free(max_health);
    free(queue);
    
    return result;
}