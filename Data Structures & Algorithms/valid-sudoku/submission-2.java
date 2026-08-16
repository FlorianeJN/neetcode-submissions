class Solution {
    public boolean isValidSudoku(char[][] board) {
        // To verify the conditions, gonna keep a set for row, col and grid. easy to detect duplicates

        Map<Integer,Set<Character>> cols = new HashMap<>();
        Map<Integer,Set<Character>> rows = new HashMap<>();
        Map<String,Set<Character>> grid = new HashMap<>();

        for(int i = 0 ; i < 9 ; i++){
            for(int j = 0 ; j < 9 ; j++){
                char c = board[i][j];
                if(board[i][j] == '.') continue;
                
                String key = (i/3) + "," + (j/3);

                rows.putIfAbsent(i, new HashSet<>());
                cols.putIfAbsent(j, new HashSet<>());
                grid.putIfAbsent(key, new HashSet<>());

                if(rows.get(i).contains(c) || cols.get(j).contains(c) || grid.get(key).contains(c)) return false;

                rows.get(i).add(c);
                cols.get(j).add(c);
                grid.get(key).add(c);
            }
        }

        return true;
    }
}
