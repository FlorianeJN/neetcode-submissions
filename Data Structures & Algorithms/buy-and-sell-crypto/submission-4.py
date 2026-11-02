class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Must choose on day to but and one day to sell
        we want to lowest day to buy, and the higher day to sell
        Sliding window approach -> O(n)
        """

        max_profit = 0

        current_min = prices[0]
        i = 0
        j = i + 1

        while j < len(prices):
            if prices[j] < current_min:
                current_min = prices[j]
                i = j
                j = i + 1
            else :
                max_profit = max(max_profit,prices[j] - prices[i])
                j += 1
        return max_profit
            
            
        