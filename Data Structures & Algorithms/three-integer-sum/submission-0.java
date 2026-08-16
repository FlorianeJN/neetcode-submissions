class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Map<Integer, Integer> indexMap = new HashMap<>();
        Set<List<Integer>> seen = new HashSet<>();
        List<List<Integer>> result = new ArrayList<>();

        // Fill the map with the indices
        for (int i = 0; i < nums.length; i++) {
            indexMap.put(nums[i], i);
        }

        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                int valueToLookFor = (nums[i] + nums[j]) * -1;

                if (indexMap.containsKey(valueToLookFor) && indexMap.get(valueToLookFor) != i
                    && indexMap.get(valueToLookFor) != j) {
                    List<Integer> list =
                        new ArrayList<>(Arrays.asList(nums[i], nums[j], valueToLookFor));
                    Collections.sort(list);
                    if (seen.add(list)) {
                        result.add(list);
                    }
                }
            }
        }

        return result;
    }
}
