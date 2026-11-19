class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        1 2 3 4 5 6 7
        5 6 7 1 2 3 4

        first = nums[:n-k]
        second = nums[n-k:n+1]

        """
        n = len(nums)
        first = nums[: n - k % n]
        second = nums[n - (k % n) : n + 1]

        for i in range(n):
            if i < len(second):
                nums[i] = second[i]
            else:
                nums[i] = first[i - len(second)]
