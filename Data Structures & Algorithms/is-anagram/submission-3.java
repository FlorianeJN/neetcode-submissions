class Solution {
    public boolean isAnagram(String s, String t) {

        if(s.length() != t.length()) return false;

        // Using character count array instead of hashmap
        int[] array = new int[26];

        for(int i = 0 ; i < s.length() ; i++){
            array[s.charAt(i) - 'a']++;
            array[t.charAt(i) - 'a']--;
        }

        for(int value : array){
            if(value != 0) return false;
        }

        return true;
    }
}
