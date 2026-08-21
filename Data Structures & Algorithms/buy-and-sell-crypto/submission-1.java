class Solution {
    public int maxProfit(int[] prices) {
        // Time Complexity : O(n)
        // Two pointer approach (Sliding window)

        int maxProfit = 0;
        int right = 1;
        int left = 0;

        while (right < prices.length) {
            // Possible profit
            if (prices[right] > prices[left]) {
                int profit = prices[right] - prices[left];
                maxProfit = Math.max(profit, maxProfit);
            } else
                left = right;
            right++;
        }

        return maxProfit;
    }
}
