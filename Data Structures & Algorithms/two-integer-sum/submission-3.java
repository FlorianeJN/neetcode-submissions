class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Using hashmap
        Map<Integer,Integer> map = new HashMap<Integer,Integer>();

        for(int i = 0 ; i < nums.length ; i++){
            int valueToLookFor = target - nums[i];

            if(map.containsKey(valueToLookFor)){
                return new int[] {map.get(valueToLookFor),i};
            }

            // Add the value and its index to the map
            map.put(nums[i],i);
        }

        return new int[]{};
    }
}
