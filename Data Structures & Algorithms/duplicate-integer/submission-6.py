class Solution:
    '''
        Approach: Use a set to detect duplicate
        Time complexity: O(n)
    '''
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()

        for num in nums:
            if num in s:
                return True
            s.add(num)

        return False
        