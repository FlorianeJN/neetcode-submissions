class Solution {
    public int search(int[] nums, int target) {
        int low = 0;
        int high = nums.length - 1;

        while (low <= high){
            int mid = low + (high - low)/ 2;

            int num = nums[mid];

            if(num == target) return mid;

            if( num < target) low = mid + 1;
            else high = mid - 1;
        }

        return -1;
    }
}
