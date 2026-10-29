class Solution {
    int CHEST = 0;
    int INF = 2147483647;
    int WATER = -1;
    int[][] DIRECTIONS = new int[][] {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    public void islandsAndTreasure(int[][] grid) {
        // Multi-Source BFS
        // Register all chest
        // Expand chests

        Queue<int[]> q = new ArrayDeque<>();
        int rows = grid.length;
        int cols = grid[0].length;

        // Register all chests
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == CHEST)
                    q.offer(new int[] {i, j});
            }
        }

        // Multi-source BFS
        while (!q.isEmpty()) {
            int[] cell = q.poll();
            int r = cell[0], c = cell[1];

            for(int[] d : DIRECTIONS){
                // Verify if its within bounds
                int nr = r + d[0];
                int nc = c + d[1];
                boolean rowWithinBounds = nr >= 0 && nr < grid.length;
                boolean colWithinBounds = nc >= 0 && nc < grid[0].length;

                if (!rowWithinBounds || !colWithinBounds) continue;

                // Make sure we are on land
                if (grid[nr][nc] != INF) continue;

                // Update value
                grid[nr][nc] = grid[r][c] + 1;

                // Add to queue
                q.offer(new int[]{nr,nc});
            }
        }
    }
}
