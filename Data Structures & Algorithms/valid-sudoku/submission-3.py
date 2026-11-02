class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        [      0 1 2     3 4 5     6 7 8
          0  [ 1 2 x ] [ x 3 x ] [ x x x ]
          1  [ 4 x x ] [ 5 x x ] [ x x x ]
          2  [ x 9 8 ] [ x 3 x ] [ x x 3 ]

          3  [ 5 x x ] [ x 6 x ] [ x x 4 ]
          4  [ x x x ] [ 8 x 3 ] [ x x 5 ]
          5  [ 7 x x ] [ x 2 x ] [ x x 6 ]

          6  [ x x x ] [ x x x ] [ 2 x x ]
          7  [ x x x ] [ 4 1 9 ] [ x x 8 ]
          8  [ x x x ] [ x 8 x ] [ x 7 9 ]
        ]

        [
            0,0 0,1 0,2
            1,0 1,1 1,2
            2,0 2,1 2,2
        ]

        need 3 sets -> row , col, subbox

        enter values as tuples
        row => (r,v)
        col => (c,v)
        subbox =>  (sr,sc,v)
                    - Could use a hashmap for correspondance?
                    - Integer division ( // 3)

        Valid sudoku has:
        - no duplicate 1-9 for each row
        - no duplicate 1-9 for each column
        - no duplicate 1-9 for each sub-box

        """

        row_set = set()
        col_set = set()
        sub_box_set = set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                val = board[i][j]

                if val == ".":
                    continue

                if (
                    (i, val) in row_set
                    or (j, val) in col_set
                    or (i // 3, j // 3, val) in sub_box_set
                ):
                    return False

                row_set.add((i, val))
                col_set.add((j, val))
                sub_box_set.add((i // 3, j // 3, val))
        return True
