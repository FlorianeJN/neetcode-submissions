class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        read = write = 0

        while read < len(nums):
            while read < len(nums) - 1 and nums[read] == 0:
                read += 1

            nums[read], nums[write] = nums[write], nums[read]
            write += 1
            read += 1
