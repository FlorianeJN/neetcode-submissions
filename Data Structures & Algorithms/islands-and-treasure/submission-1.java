class Solution {
    int CHEST = 0;
    int LAND = 2147483647;
    int[][] DIRECTIONS = new int[][] {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    public void islandsAndTreasure(int[][] grid) {
        // Go through my grid and load all chests in q
        Queue<int[]> q = new ArrayDeque<>();
        int rows = grid.length;
        int cols = grid[0].length;

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

            // Look at neighbors
            for (int[] d : DIRECTIONS) {
                int nr = r + d[0];
                int nc = c + d[1];

                // Check bounds
                if (nr < 0 || nr >= rows || nc < 0 || nc >= cols)
                    continue;

                // make sure that we are on land
                if (grid[nr][nc] != LAND)
                    continue;

                // Update value and add to q
                grid[nr][nc] = grid[r][c] + 1;
                q.offer(new int[] {nr, nc});
            }
        }
    }
}
