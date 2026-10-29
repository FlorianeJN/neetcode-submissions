class Solution {
    int FRESH = 1;
    int ROTTEN = 2;
    int[][] DIRECTIONS = new int[][] {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    public int orangesRotting(int[][] grid) {
        // Do one pass when you count fresh and register rotten
        int countFresh = 0;
        int minutes = 0;
        Queue<int[]> q = new ArrayDeque<>();
        int rows = grid.length;
        int cols = grid[0].length;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == FRESH)
                    countFresh++;
                else if (grid[i][j] == ROTTEN)
                    q.offer(new int[] {i, j});
            }
        }

        // Multi-source BFS
        while (!q.isEmpty() && countFresh > 0) {
            // Take a snapshot to go level by level
            int size = q.size();

            for (int k = 0; k < size; k++) {
                // Take the cell
                int[] cell = q.poll();
                int r = cell[0], c = cell[1];

                // Verify all adjacent ones
                for (int[] d : DIRECTIONS) {
                    int nr = r + d[0];
                    int nc = c + d[1];

                    // Verify bounds
                    if (nr < 0 || nr >= rows || nc < 0 || nc >= cols ) continue;

                    // Make sure that fresh otherwise continue
                    if (grid[nr][nc] != FRESH) continue;

                    // Process it -> Mark it as rotten and add to q
                    grid[nr][nc] = ROTTEN;
                    countFresh--;
                    q.offer(new int[]{nr,nc});
                }
            }
            minutes++;
        }

        // Verify if no more fresh remaining
        return countFresh == 0 ? minutes : -1;
    }
}
