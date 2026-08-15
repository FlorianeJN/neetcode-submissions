class Solution {
    public boolean isAnagram(String s, String t) {

        // If lengths are not the same, they can't be anagrams
        if (s.length() != t.length()) {
            return false;
        }

        // Convert strings to character arrays
        char[] charS = s.toCharArray();
        char[] charT = t.toCharArray();

        // Use a list of Characters, not char
        List<Character> listeCharS = new LinkedList<>();

        // Add characters from the first string to the list
        for (char c : charS) {
            listeCharS.add(c);
        }

        // Check if all characters from the second string are present in the list
        for (char c : charT) {
            if (listeCharS.contains(c)) {
                listeCharS.remove((Character) c); // Cast to avoid ambiguity
            } else {
                return false; // Return immediately if a character is missing
            }
        }

        // If all characters matched, it's an anagram
        return listeCharS.isEmpty();
    }
}
