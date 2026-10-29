class Solution {
    char water = '0';
    public int numIslands(char[][] grid) {
        int count = 0;
        boolean[][] visited = new boolean[grid.length][grid[0].length];

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (dfs(grid, visited, i, j))
                    count++;
            }
        }

        return count;
    }

    private boolean dfs(char[][] grid, boolean[][] visited, int i, int j) {
        // i must be between 0 and grid.length
        // j must be between 0 and grid[0].length
        boolean iIsWithinBounds = i >= 0 && i < grid.length;
        boolean jIsWithinBounds = j >= 0 && j < grid[0].length;

        if (!iIsWithinBounds || !jIsWithinBounds)
            return false;

        // if water -> return false
        if (grid[i][j] == water)
            return false;

        // if visited -> return false
        if (visited[i][j])
            return false;

        // Mark as visited
        visited[i][j] = true;

        // Visit neighbors
        dfs(grid, visited, i - 1, j);
        dfs(grid, visited, i + 1, j);
        dfs(grid, visited, i, j - 1);
        dfs(grid, visited, i, j + 1);

        return true;
    }
}
