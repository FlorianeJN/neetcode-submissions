class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer,Integer> mapValueCount = new HashMap<>();
        for(int num : nums){
            mapValueCount.put(num,mapValueCount.getOrDefault(num,0)+1);
        }

        int[] topRecurences =  new int[k];
        for(int i = 0 ; i < k ; i++){
            //Obtenir la valeur ayant le plus gros compte et la retirer
            int maxElement = -1;
            int maxCount = 0;

            for (Map.Entry<Integer, Integer> entry : mapValueCount.entrySet()) {
                if (entry.getValue() > maxCount) {
                    maxElement = entry.getKey();
                    maxCount = entry.getValue();
                }
            }
            topRecurences[i] = maxElement;
            mapValueCount.remove(maxElement);
        }
        return topRecurences;
    }
}
