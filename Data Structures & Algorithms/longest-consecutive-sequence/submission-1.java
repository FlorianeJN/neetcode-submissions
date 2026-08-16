class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();

        for(int num : nums){
            set.add(num);
        }

        int max = 0;

        // Only start counting if we are at the beginning
        for(int num : nums){
            if(!set.contains(num - 1)){
                int length = 1;

                while(set.contains(num + length)){
                    length++;
                }

                max = Math.max(length,max);
            }
        }

        return max;
    }
}
