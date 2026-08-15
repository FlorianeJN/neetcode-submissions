class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // Use a hashmap to store the "code" and the list of anagrams
        Map<String,List<String>> map = new HashMap<String,List<String>>();

        for(String str : strs){
            char[] arrayStr = str.toCharArray();
            Arrays.sort(arrayStr);
            String sortedArray = new String(arrayStr);

            List<String> list = map.getOrDefault(sortedArray, new ArrayList<String>());
            list.add(str);
            map.put(sortedArray,list);
        }

        List<List<String>> result = new ArrayList<>();

        for(Map.Entry<String,List<String>> entry : map.entrySet()){
            result.add(entry.getValue());
        }

        return result;
    }
}
