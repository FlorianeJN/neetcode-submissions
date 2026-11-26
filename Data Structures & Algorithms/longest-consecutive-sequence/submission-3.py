class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0

        for n in s:
            # start of a new sequence
            if not n - 1 in s:
                cur = 0
                while n + cur in s:
                    cur += 1
                longest = max(longest,cur)
        
        return longest



        