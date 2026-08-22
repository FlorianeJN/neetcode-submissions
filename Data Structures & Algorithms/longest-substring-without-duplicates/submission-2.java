class Solution {
    public int lengthOfLongestSubstring(String s) {
        int maxLength = 0 , start = 0;
        Map<Character,Integer> lastSeen = new HashMap<>();

        for(int end = 0 ; end < s.length() ; end++){
            char c = s.charAt(end);

            if(lastSeen.containsKey(c) && lastSeen.get(c) >= start) start = lastSeen.get(c) + 1;

            lastSeen.put(c,end);
            maxLength = Math.max(end - start + 1 , maxLength);
        }

        return maxLength;
    }
}
