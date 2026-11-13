class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Input: integers array nums that has been rotated between 1 and n times. integer target
        Output: index of target if within nums, -1 otherwise

        Example:
            Input: nums = [3,4,5,6,1,2], target = 1
            Output: 4

        Brute force:
            - Go through the array when if the value is the target we return the index
            - If the loop finishes without returning the index then we can return -1 as the value is not within the array
            Time Complexity: O(n)
            Space Complexity: O(1)

        Binary search:
            First get two arrays sorted in ascending order -> find minimum index
            Do binary search for value in the right array
            Time Complexity: O(log n)
            Space Complexity: O(1)
        """

        # Get two sorted arrays by finding the minimum value using binary search
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = low + ((high - low) // 2)
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        # check if my low is at 0 -> handle it
        if low == 0:
            indices = (0, len(nums) - 1)
        elif low != 0 and nums[0] <= target <= nums[low - 1]:
            indices = (0, low - 1)
        else:
            indices = (low, len(nums) - 1)

        # Binary search for value
        low = indices[0]
        high = indices[1]

        while low <= high:
            mid = low + ((high - low) // 2)

            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1
