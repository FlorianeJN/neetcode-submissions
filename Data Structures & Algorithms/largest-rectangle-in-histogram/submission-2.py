class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Each position tries to make a rectangle using its own height

        Brute force: Try to compute the max rectangle using heights[i] going left and right
        Time complexity: O(n2)
        Space complexity: O(1)

        Optimal approach: Use a non decreasing monotonic stack
        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        stack = []
        largest_rectangle = 0
        n = len(heights)

        for i in range(n + 1):
            current_height = heights[i] if i < n else 0

            while stack and current_height < heights[stack[-1]]:
                popped_height = heights[stack.pop()]
                left = stack[-1] if stack else -1
                right = i

                width = right - left - 1
                largest_rectangle = max(largest_rectangle, popped_height * width)
            
            stack.append(i)

        return largest_rectangle
            


        # largest_rectangle = 0

        # for i,height in enumerate(heights):
        #     current_rectangle = height
        #     left_idx = i - 1
        #     right_idx = i + 1

        #     # Go left
        #     while left_idx >= 0 and heights[left_idx] >= height:
        #         current_rectangle += height
        #         left_idx -= 1

        #     # Go right
        #     while right_idx < len(heights) and heights[right_idx] >= height:
        #         current_rectangle += height
        #         right_idx += 1

        #     largest_rectangle = max(largest_rectangle, current_rectangle)
        # return largest_rectangle
        