class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Input -> non-negative integers representing an elevation map
        Output -> How much water it can trap after raining

        Approach:
                for each spot, the formula is = min(max_height_left , max_height_right) - height[i]
                so for each spot compute max_height_left and and max_height_right in arrays
                then apply formula

        Time Complexity -> O(n)
        Space Complexity -> O(n)
        """

        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        max_left_so_far = 0
        max_right_so_far = 0
        total = 0

        # Compute max_left
        for i in range(len(height)):
            max_left[i] = max_left_so_far
            max_left_so_far = max(max_left_so_far, height[i])

        # Compute max_right
        for i in range(len(height) - 1, -1, -1):
            max_right[i] = max_right_so_far
            max_right_so_far = max(max_right_so_far, height[i])

        for left, right, h in zip(max_left, max_right, height):
            value = min(left, right) - h
            if value > 0:
                total += value

        return total
