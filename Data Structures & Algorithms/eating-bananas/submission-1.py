class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Example:
            piles = [1,4,3,2], h = 9
            range of possibilities -> 1 to max(piles)
            min_time = max(piles) -> 4 bph -> 4 hrs
            max_time = 1 bph -> 1 + 4 + 3 + 2 = 10 hrs 

        Brute force:
            - Test every bph possibility.
            Time Complexity: O(l * n) if n is the length of piles and l is the max value of piles
            Space Complexity: O(1)

        Binary search approach:
            - We have a range of possibilies
            - Start from the middle and adjust each time
            - Compute the hours it takes to eat all bananas given mid rate
            - if the hours is too high -> rate is too low so make the rate bigger
            - else if the hours is too low -> rate is too high so make the rate lower
            - else we found to perfect rate to reach h hours

            Time Complexity: O(log l * n)
            Space Complexity: O(1)
        """

        low = 1 
        high = max(piles)

        while low <= high:
            mid = low + ((high - low) // 2)

            hours_taken = self.get_hours_taken(mid, piles)
            # hours taken too low so rate is too high
            if hours_taken <= h:
                high = mid - 1
            # hours taken is too high so rate is too low
            else:
                low = mid + 1
        return low
                
    def get_hours_taken(self, rate: int, piles: List[int]):
        hours_taken = 0
        for pile in piles:
            # 1 / 2 = 0,5 -> 1
            hours_taken += math.ceil(pile / rate)
        return hours_taken
