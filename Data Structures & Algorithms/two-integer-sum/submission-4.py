class Solution:
    """
        - Use nested to look for target - nums[i] in remaining subarray -> O(n2)
        - Use a hashmap to memorize number and index -> O(n)
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute force approach
        for i in range(len(nums)):
            for j in range(i + 1 , len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

        return [-1,-1]
        