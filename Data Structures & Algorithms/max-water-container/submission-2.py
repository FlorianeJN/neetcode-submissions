class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
          0 1 2 3 4 5 6 7 <- index
        [ 1 7 2 5 4 7 3 6 ]
            ^           ^

        area = width * height
        height is the min height
        width is the diff between indices

        after computing move minimum height because
        its capping the height (we always use the min height)

        heights[i] is the height

        choose two bars to form a container
        return max AMOUNT of water

        Brute force approach -> Compute every possible area using
        nested loops: O(n2)

        Two pointer approach -> O(n)
        """

        max_area = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            width = r - l
            height = min(heights[l],heights[r])
            current_area = width * height

            max_area = max(current_area, max_area)

            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1

        return max_area
        