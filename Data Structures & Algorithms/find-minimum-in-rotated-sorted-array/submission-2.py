class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Input: arrays nums that has been rotated between 1 and n times (n is the length of the array)
        Output: Return the minimum element of the array

        Constraints:
            The array was originally sorted in ASCENDING order
            All the elements in the array are unique

        Example:
            Input: nums = [3,4,5,6,1,2]
            Output: 1

        Brute force: 
            Go through every element of the array and record the minimum seen yet.
            At the end, return that minimum
        
        Time Complexity: O(n)
        Space Complexity: O(1)

        Binary search: What rule can i follow to remove half of the array each time?


        Input: nums = [3,4,5,6,1,2]

        [ 3 4 5 6 7 8 1 2 ]
          ^             ^
                  ^
        [ 3 4 5 6 7 8 1 2 ]
                    ^   ^
                      ^

        low = 3
        high = 2
        mid = 7

        here i can see that my higher bound is LOWER than my lower bound so i must go towards it
        i know that i found my value when nums[mid - 1] > nums[mid].

        [ 1 2 3 4 5 6 7 8 ]
          ^             ^
                  ^

        [ 1 2 3 4 5 6 7 8 ]
          ^

        Rules:
        evalute mid lower and higher and move towards the smallest value
        if nums[i - 1] > nums[i] => value has been found (nums[i])

        Time Complexity: O(log n)
        """
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = low + ((high - low) // 2)
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        return nums[low]
        