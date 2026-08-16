class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        // Two pointer approach
        // Time complexity: O(n2)
        // Space complexity: O(1)

        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);

        for (int i = 0; i < nums.length - 2; i++) {
            // skip duplicate values for i
            if (i > 0 && nums[i] == nums[i - 1])
                continue;

            int j = i + 1;
            int k = nums.length - 1;

            while (j < k) {
                int value = nums[i] + nums[j] + nums[k];

                if (value == 0) {
                    result.add(Arrays.asList(nums[i], nums[j], nums[k]));

                    j++;
                    k--;

                    // skip duplicate values for j and k
                    while (j < k && nums[j] == nums[j - 1]) j++;
                    while (j < k && nums[k] == nums[k + 1]) k--;
                } else if (value > 0) {
                    k--; // sum too high, shrink from the right
                } else {
                    j++; // sum too low, grow from the left
                }
            }
        }

        return result;
    }
}