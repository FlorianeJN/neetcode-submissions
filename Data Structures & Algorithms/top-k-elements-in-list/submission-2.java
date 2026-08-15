class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer,Integer> map = new HashMap<>();

        // Get counts (in hashmap)
        for(int num : nums) {
            map.put(num, map.getOrDefault(num,0) + 1);
        }

        // Put the elements in an array and sort
        List<int[]> array = new ArrayList<>();
        for(Map.Entry<Integer,Integer> entry : map.entrySet()){
            array.add(new int[]{entry.getValue(), entry.getKey()});
        }

        array.sort((a,b) -> b[0] - a[0]);
        int[] res = new int[k];

        // Get the most k frequent elements
        for(int i = 0 ; i < k ; i++){
            res[i] = array.get(i)[1];
        }

        return res;
    }
}
