class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Input -> list of integers
        Treatment -> Move all 0s to the end wile maintaining the relative order
        Output -> array after moving all zeros to the end

                write -> keep track of where to write next
                read -> look for non-zeros

                when read reached the end, write 0s start w + 1

                              w
                                 r
        Example:        0 1 0 3 12
                        1 3 12 0 0

        Approach:
        - Brute force:  Use a nested loop and whenever we detect a zero, swap with the next non-zero value
                        Outer loop used to detect zero. Inner loop used to detect next non-zero
                        Time Complexity -> O(n2)

        - Two pointer:  - Use two pointers read and write.
                        - Write is keep track of where to write next
                        - Read looks for the next non-zero value
                        - When read finds the next non-zero value, overwrite the value at write. Keep going
                        - When read reached the end, write 0s starting write
                        Time Complexity -> O(n)
        """
        write = 0

        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write] = nums[read]
                write += 1

        for i in range(write, len(nums)):
            nums[i] = 0

        return nums
