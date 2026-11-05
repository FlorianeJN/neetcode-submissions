class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Input -> two integer arrays (nums1 and nums2) sorted in non-decreasing order
                 m -> valid elements in nums1 
                 n -> number of elements in nums 2

        Ouput -> nums1 and nums2 merged into nums1 in non-decreasing order

        Example:
        input ->    nums1 = [10 20 20 40 0 0] m = 4, nums2 = [1 2] n = 2
        output ->   nums1 = [1 2 10 20 20 40]

        Approach:
                - Copy of nums1 since we are going to overwrite it
                - Go through and compare nums1_copy and nums2 and write
                    lowest element into nums1
                Time Complexity -> O(n + m)
        """

        copy_nums1 = nums1[:m]
        i = 0
        idx_n1 = 0;
        idx_n2 = 0

        while idx_n1 < m and idx_n2 < n:
            n1_value = copy_nums1[idx_n1]
            n2_value = nums2[idx_n2]

            if n1_value <= n2_value:
                nums1[i] = n1_value
                idx_n1 += 1
            else:
                nums1[i] = n2_value
                idx_n2 += 1
            i += 1

        while idx_n1 < m:
            nums1[i] = copy_nums1[idx_n1]
            idx_n1 += 1
            i += 1

        while idx_n2 < n:
            nums1[i] = nums2[idx_n2]
            idx_n2 += 1
            i += 1
        
