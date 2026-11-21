class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        i,j = 0 , len(height) - 1

        while i < j:
            w = j - i
            left, right = height[i],height[j]
            h = min(left,right)
            max_area = max(w * h, max_area)
            if left < right:
                i += 1
            else:
                j -= 1

        return max_area