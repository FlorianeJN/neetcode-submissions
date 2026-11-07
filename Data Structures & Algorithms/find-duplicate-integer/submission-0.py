class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            value = abs(nums[i])
            if nums[value] < 0:
                return value
            nums[value] *= -1
        
        return -1
        