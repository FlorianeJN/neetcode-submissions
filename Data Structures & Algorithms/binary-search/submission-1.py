class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Input:  Array of distinct integers sorted in ascending order and a target (int)
        Ouput:  The index of the target within the nums array
                if it doesnt exist return -1

        Constraints:  The algorithm must run in O(log n) time.

        Approach: Binary search

        [-1] target = -1
        low = 0
        high = 1 - 1 = 0

        """
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + ((high - low) // 2)
            value = nums[mid]

            if value == target:
                return mid
            if value < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1



        