class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Merge arrays (keep ascending order) and find middle (median)
        Time Complexity: O(n + m)
        Space Complexity: O(n + m)
        """
        merged =  []
        i = j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        
        while i < len(nums1):
            merged.append(nums1[i])
            i += 1
        
        while j < len(nums2):
            merged.append(nums2[j])
            j += 1
        
        n = len(merged)

        if n % 2 == 0:
            first = n // 2
            second = first - 1
            return (merged[first] + merged[second]) / 2
        
        return merged[n // 2]
        