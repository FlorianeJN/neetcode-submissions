class Solution {
    public int[] productExceptSelf(int[] nums) {
        // Will use two arrays : prefix array and suffix array
        int length = nums.length;

        int[] prefix = new int[length];
        int[] suffix = new int[length];
        int[] result = new int[length];

        prefix[0] = 1;
        suffix[length - 1] = 1;

        // Fill prefix
        for(int i = 1 ; i < nums.length ; i++){
            prefix[i] = prefix[i - 1] * nums[i - 1];
        }

        // Fill suffix
        for(int i = nums.length - 2 ; i >= 0 ; i--){
            suffix[i] = suffix[i + 1] * nums[i + 1];
        }

        // Fill result
        for(int i = 0 ; i < nums.length ; i++){
            result[i] = prefix[i] * suffix[i];
        }

        return result;
    }
}  
