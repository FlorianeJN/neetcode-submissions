class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Brute force:
        Use sliding window approach
        fixed size k
        for each window of size k -> get the max (using max function for example)
        With this approach we recompute max from scratch for every window
        Time Complexity: O(n*k)
        Space Complexity: O(n)

        Max-heap approach:
        - keep a max-heap of (value,index) pairs.
        - the heap top is the max candidate for the current window
        - remove lazily: an expired entry stays until it reaches the top
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """

        heap = []
        output = []

        # Do first window
        for i in range(k):
            heapq.heappush_max(heap,(nums[i], i))

        output.append(heap[0][0])
        start = 1

        for i in range(k,len(nums)):
            heapq.heappush_max(heap,(nums[i],i))

            while heap and heap[0][1] < start:
                heapq.heappop_max(heap)
            
            output.append(heap[0][0])
            start += 1
        
        return output




        
        