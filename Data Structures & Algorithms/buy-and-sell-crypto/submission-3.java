class Solution {
    public int maxProfit(int[] prices) {
        int start = 0 , maxProfit = 0;

        for (int end = 0 ; end < prices.length ; end++){
            if (prices[end] < prices[start]) start = end;

            maxProfit = Math.max(prices[end] - prices[start], maxProfit);
        }

        return maxProfit;
    }
}
