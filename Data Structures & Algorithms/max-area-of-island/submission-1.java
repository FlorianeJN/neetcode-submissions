class Solution {
    int water = 0;
    public int maxAreaOfIsland(int[][] grid) {
        int maxArea = 0;
        boolean[][] visited = new boolean[grid.length][grid[0].length];

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                int area = dfs(grid, visited, i, j);
                maxArea = Math.max(maxArea, area);
            }
        }

        return maxArea;
    }

    private int dfs(int[][] grid, boolean[][] visited, int i, int j) {
        // Make sure that i and j are within bounds
        boolean iIsWithinBounds = i >= 0 && i < grid.length;
        boolean jIsWithinBounds = j >= 0 && j < grid[0].length;
        if (!iIsWithinBounds || !jIsWithinBounds)
            return 0;

        // Make sure that we are on land
        if (grid[i][j] == water)
            return 0;

        
        // Make sure that land is not visited
        if (visited[i][j])
            return 0;

        visited[i][j] = true;

        // Get values from neighbors
        return 1 + dfs(grid, visited, i, j + 1) + dfs(grid, visited, i, j - 1)
            + dfs(grid, visited, i - 1, j) + dfs(grid, visited, i + 1, j);
    }
}
