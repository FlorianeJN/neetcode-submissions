class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // Use a hashmap to store the "code" and the list of anagrams
        Map<String,List<String>> map = new HashMap<>();

        for(String str : strs){
            char[] arrayStr = str.toCharArray();
            Arrays.sort(arrayStr);
            String sortedArray = new String(arrayStr);

            List<String> list = map.getOrDefault(sortedArray, new ArrayList<String>());
            list.add(str);
            map.put(sortedArray,list);
        }

        return new ArrayList<>(map.values());
    }
}
