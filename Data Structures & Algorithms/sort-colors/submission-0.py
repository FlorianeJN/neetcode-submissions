class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Using bucket sort
        """

        buckets = [0] * 3

        # Fill the buckets
        for n in nums:
            buckets[n] += 1

        write = 0
        for i,count in enumerate(buckets):
            for _ in range(count):
                nums[write] = i
                write += 1


        