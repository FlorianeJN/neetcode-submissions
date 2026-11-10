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

        Deque approach:
        - use deque kinda like as a monotonic stack. push (value,index)
        - front of the queue will have the max value
        - When we treat a new value pop as long as nv is greater than back
        - check for front expiry
        """
        output = []
        q = deque()
        
        for i,num in enumerate(nums):

            while q and num > q[-1][1]:
                q.pop()
            
            q.append((i,num))

            if i >= k - 1:
                window_start = i - k + 1

                if q[0][0] < window_start:
                    q.popleft()
                
                output.append(q[0][1])

        return output
            


        




        
        