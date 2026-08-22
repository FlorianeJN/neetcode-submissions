class Solution {
    public int maxProfit(int[] prices) {
        int start = 0, end = 1, maxProfit = 0;

        while (end < prices.length) {
            if (prices[end] < prices[start])
                start = end;

            maxProfit = Math.max(prices[end] - prices[start], maxProfit);
            end++;
        }

        return maxProfit;
    }
}
