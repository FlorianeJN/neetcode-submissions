class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        """
        Brute force: Use nested loops to evaluate windows of size k.
        Time complexity: O(n*k)
        Space complexity: O(1)

        Sliding window: Use sliding window technique to evaluate windows of size k
        Time complexity: O(n)
        Space complexity: O(1)

        To avoid division, we can compare window sum to threshold * k
        """

        count_subarrays = 0
        sum_values = 0

        # Load the first window
        for i in range(k):
            sum_values += arr[i]
        if sum_values >= threshold * k:
            count_subarrays += 1

        # Do the rest
        for i in range(k , len(arr)):
            sum_values += arr[i]
            sum_values -= arr[i - k]
            if sum_values >= threshold * k:
                count_subarrays += 1
        
        return count_subarrays




        