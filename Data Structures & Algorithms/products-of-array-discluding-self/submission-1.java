class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] output = new int[nums.length];
        
        int maxProduct = 1;
        int zeroCount = 0;

        // Calculate the product of all non-zero numbers and count zeros
        for (int num : nums) {
            if (num == 0) {
                zeroCount++;
            } else {
                maxProduct *= num;
            }
        }

        // Case 1: If there are more than one zero, all elements in output should be zero
        if (zeroCount > 1) {
            return output; // All elements are already initialized to zero
        }

        // Case 2: If there is exactly one zero, only the position with zero should have maxProduct, others zero
        if (zeroCount == 1) {
            for (int i = 0; i < nums.length; i++) {
                output[i] = (nums[i] == 0) ? maxProduct : 0;
            }
        } 
        // Case 3: If there are no zeros, calculate the product by dividing maxProduct by each element
        else {
            for (int i = 0; i < nums.length; i++) {
                output[i] = maxProduct / nums[i];
            }
        }

        return output;
    }
}
