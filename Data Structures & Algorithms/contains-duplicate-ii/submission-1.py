class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Brute force -> Use nested loop to find duplicates and verify indices condition
        Time Complexity: O(n2)
        Space Complexity: O(1)

        Hashmap ->  Push (value,index) into a map and use set to detect duplicates.
                When duplicate is found, verify indices condition
        Time Complexity: O(n)
        Space Complexity: O(n)

        Sorting -> Create an array that stores (value,index)
                        Sort that array
                        Verify adjacent pairs for duplicates
                        When duplicate, verify indices condition
        Time Complexity: O(n log n)
        Space Complexity: O(n)

        Sliding window ->   use a window + a set. window holds k elements so 
                            any duplicate found is automatically within distance k
        Time Complexity: O(n)
        Space Complexity: O(k)
        """

        elements = set()

        for i,n in enumerate(nums):
            if n in elements:
                return True

            elements.add(n)
            if len(elements) > k:
                elements.remove(nums[i - k])

        return False
            
        