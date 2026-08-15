class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // List to store the final groups of anagrams
        List<List<String>> anagrams = new ArrayList<>();

        // Convert the array to a modifiable list for easier removal of elements
        List<String> wordList = new ArrayList<>(Arrays.asList(strs));

        // Iterate while the list still has elements
        while (!wordList.isEmpty()) {
            // Create a new list to store anagrams for the current word
            List<String> currentAnagrams = new ArrayList<>();

            // Get the first word from the list and sort it
            String s = wordList.get(0);
            String sortedString1 = sortString(s);

            // Use an iterator to find all anagrams and remove them from the list
            Iterator<String> iterator = wordList.iterator();
            while (iterator.hasNext()) {
                String t = iterator.next();
                if (sortedString1.equals(sortString(t))) {
                    currentAnagrams.add(t);
                    iterator.remove();  // Remove the word from the list
                }
            }

            // Add the group of anagrams to the result
            anagrams.add(currentAnagrams);
        }

        return anagrams;
    }

    // Helper method to sort the characters in a string alphabetically
    public static String sortString(String str) {
        char[] charArray = str.toCharArray();
        Arrays.sort(charArray);
        return new String(charArray);
    }
}