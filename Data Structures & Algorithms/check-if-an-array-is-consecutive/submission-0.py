class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        cur = min(nums)
        s = set(nums)

        for _ in range(len(nums)):
            if cur not in s:
                return False
            cur += 1

        return len(s) == len(nums)