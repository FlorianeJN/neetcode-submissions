# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        """
        We want to find a secret number
        Each time we try, the api tells us whether we are too low or too high
        Constraints:
        number can be between 1 and n inclusive

        Brute force: Test linearly every single number between 1 and n
        Time Complexity: O(n)
        Space Complexity: O(1)

        Binary search: start by guessing middle value
        Depending on guess result, adjust lower or higher bound
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        low = 1
        high = n
        
        while low < high:
            mid = (low + high) // 2
            # Guess is the number picked
            if guess(mid) == 0:
                return mid
            # Guess is higher than the number picked
            if guess(mid) < 0:
                high = mid - 1
            # Guess is lower than the number picked
            else:
                low = mid + 1
        return low

        