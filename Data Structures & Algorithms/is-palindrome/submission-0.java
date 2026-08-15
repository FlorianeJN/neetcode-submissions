class Solution {
    public boolean isPalindrome(String s) {
        // Convert to lowercase and remove non-alphanumeric characters
        s = s.toLowerCase();
        s = s.replaceAll("[^a-z0-9]", "");
        
        // Convert string to character array
        char[] array = s.toCharArray();

        int p1 = 0;
        int p2 = array.length - 1;

        // Check for palindrome
        while (p1 < p2) {
            if (array[p1] != array[p2]) {
                return false;
            }
            p1++;
            p2--;
        }
        return true;
    }
}
