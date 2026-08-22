class Solution {
    public int characterReplacement(String s, int k) {
        Map<Character, Integer> count = new HashMap<>();
        int res = 0;
        int start = 0, maxf = 0;

        for (int end = 0; end < s.length(); end++) {
            // Update count and get max frequency
            count.put(s.charAt(end), count.getOrDefault(s.charAt(end), 0) + 1);
            maxf = Math.max(maxf, count.get(s.charAt(end)));

            // invalid window , readjust 
            while ((end - start + 1) - maxf > k) {
                count.put(s.charAt(start), count.get(s.charAt(start)) - 1);
                start++;
            }
            res = Math.max(res, end - start + 1);
        }
        return res;
    }
}
