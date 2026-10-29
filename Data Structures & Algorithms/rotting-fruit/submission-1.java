class Solution {
    int EMPTY = 0;
    int FRESH = 1;
    int ROTTEN = 2;
    int[][] DIRECTIONS = new int[][] {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    public int orangesRotting(int[][] grid) {
        // Multi-source BFS
        // Count all fresh oranges
        // Expand each minutes
        Queue<int[]> q = new ArrayDeque<>();
        int minutes = 0;
        int freshOrangesCount = 0;

        // Register rotten oranges and count all fresh oranges
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == ROTTEN)
                    q.offer(new int[] {i, j});
                else if (grid[i][j] == FRESH)
                    freshOrangesCount++;
            }
        }

        // Multi-source BFS
        while (!q.isEmpty() && freshOrangesCount > 0) {
            // Process the queue one level at a time
            int size =  q.size();
            for (int k = 0; k < size; k++) {
                int[] cell = q.poll();
                int r = cell[0], c = cell[1];

                // Explore all directions and mark fresh as rotten, add to queue
                for (int[] d : DIRECTIONS) {
                    int nr = r + d[0];
                    int nc = c + d[1];

                    // Verify bounds
                    if (nr < 0 || nr >= grid.length || nc < 0 || nc >= grid[0].length)
                        continue;
                    // Verify fresh
                    if (grid[nr][nc] != FRESH)
                        continue;

                    freshOrangesCount--;
                    grid[nr][nc] = ROTTEN;

                    q.offer(new int[] {nr, nc});
                }
            }
            minutes++;
        }

        return freshOrangesCount == 0 ? minutes : -1;
    }
}
