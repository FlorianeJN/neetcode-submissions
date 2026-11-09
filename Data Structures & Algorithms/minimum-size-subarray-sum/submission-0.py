class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = l = 0
        min_sub = float("inf")

        for r in range(len(nums)):
            total += nums[r]

            # valid window
            while total >= target:
                min_sub = min(min_sub, r - l + 1)
                total -= nums[l]
                l += 1

        return 0 if min_sub == float("inf") else min_sub
        