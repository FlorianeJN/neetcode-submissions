class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) return 0;

        // O(n log n)

        int max = 0;
        int currentMax = 0;

        Arrays.sort(nums);

        for (int i = 1; i < nums.length; i++) {
            int diff = nums[i] - nums[i-1];
            if (diff == 1) {
                currentMax++;
            } else if (diff == 0) {} 
            else {
                if (currentMax > max) max = currentMax;
                currentMax = 0;
            }
        }

        if (currentMax > max) max = currentMax;

        return max + 1;
    }
}