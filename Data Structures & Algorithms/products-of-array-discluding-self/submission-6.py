class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Brute force solution -> Use nested loop to multiply except 
        when i == j : O(n)

        Approach using / -> Multiply everything and divide by nums[i]. 
        Need to handle 0s: O(n)

        Approach using prefix and suffix -> Do the passes to calculate
        prefix and suffix : O(n)

        [1,2,4,6] -> Prefix : [1,1,2,8]
                     Suffix : [48,24,6,1]
                     Output : [48,24,12,8]
        """

        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        output = [0] * len(nums)
        prefix[0] = 1
        suffix[len(nums) - 1] = 1

        for i in range(1,len(nums)):
            prefix[i] = nums[i - 1] * prefix[i - 1]

        for i in range(len(nums) - 2 , -1 , -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        for i in range(len(nums)):
            output[i] = prefix[i] * suffix[i]

        return output




        