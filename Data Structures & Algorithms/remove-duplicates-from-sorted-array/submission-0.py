class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = read = 0
        k = 0

        while read < len(nums):
            nums[write] = nums[read]
            write += 1
            k += 1
            read += 1
            # Skip duplicates
            while read < len(nums) and nums[read] == nums[read - 1]:
                read += 1
        return k
        
        