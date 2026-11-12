class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Input: 2D grid of size m x n and an integer target
        Output: boolean indicating if the target exists whithin the grid
        
        Constraints:
            - Each row in the grid is sorted in NON-DECREASING order
            - The first integer of every row is greater than the last integer of the previous row

        Example:
        Input: matrix = 
        [   [ 1  2  4  8 ]
            [ 10 11 12 13 ] 
            [ 14 20 30 40 ]
        ], target = 10
         3 x 4
         3 rows
         4 cols
            first_range_low = 0
            first_range_high = rows - 1 = 2

        Brute force approach:
            - Go through each cell of the grid and check if it equals to target
            Time Complexity: O(m*n)
            Space Complexity: O(1)

        Binary search approach:
        m = row
        n = cols
        First, we want to know in which row the target is by eliminating half of the rows each time
        first range -> between 0 and rows - 1
        Then when we have the right row, do the same process INSIDE the row
        second range -> between 0 and cols - 1
        Time Complexity: O(log(m*n))
        """

        rows = len(matrix)
        cols = len(matrix[0])

        # Find the right row
        low = 0
        high = rows - 1
        row_idx = None

        while low <= high and row_idx is None:
            # Compare target and edge of row
            mid = low + ((high - low) // 2)

            mid_row = matrix[mid]
            first_value_row = mid_row[0]
            last_value_row = mid_row[cols - 1]

            if first_value_row <= target <= last_value_row:
                row_idx = mid
            # the current row is too low
            elif last_value_row < target:
                low = mid + 1
            # the current row is too high
            else:
                high = mid - 1

        if row_idx is None:
            return False

        # Find the right col
        low = 0
        high = cols - 1

        while low <= high:
            mid = low + ((high - low) // 2)
            value = matrix[row_idx][mid]
            if value == target:
                return True
            if value < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False
        