class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        [2,20,4,10,3,4,5] -> [2,3,4,5] so length 4
         ^         ^
        Brute Force: Use two pointers and nested loop to look for 
        consecutive sequence elements : O(n2)

        Optimal approach: Use a set to easily know what is in the array.
        The elements do not have to be consecutive in the original array
        so a set works perfectly here because it gives us O(1) lookup time.
        Overall time complexity: O(n) because we add every element to the set
        """
        s = set(nums)
        longest = 0
        i = 0

        for n in nums:
            # Start of a sequence
            if n - 1 not in s:
                count = 0
                value = n

                while value in s:
                    count += 1
                    value += 1
                
                longest = max(longest,count)

        return longest

        