class Solution {
    public int[] twoSum(int[] numbers, int target) {
        // We need to return the indices (the index starts at 1)
        // Time complexity: O(n)
        // Space complexity: O(1)
        
        int left = 0 ; 
        int right = numbers.length - 1;

        while(left < right){
            int value = numbers[left] + numbers[right];

            if(value == target) return new int[] {left + 1, right + 1};

            if(value > target) right--;
            else if(value < target ) left++;
        }

        return new int[]{};
    }
}
