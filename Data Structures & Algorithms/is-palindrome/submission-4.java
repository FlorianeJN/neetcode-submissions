class Solution {
    public boolean isPalindrome(String s) {
        char[] arr = s.toCharArray();

        int i = 0, j = arr.length - 1;

        while (i < j) {
            if (!isAlphaNumeric(arr[i])) {
                i++;
                continue;
            }

            if (!isAlphaNumeric(arr[j])) {
                j--;
                continue;
            }

            if (Character.toLowerCase(arr[i]) != Character.toLowerCase(arr[j]))
                return false;

            i++;
            j--;
        }

        return true;
    }

    public boolean isAlphaNumeric(char c) {
        return c >= 'A' && c <= 'Z' || c >= 'a' && c <= 'z' || c >= '0' && c <= '9';
    }
}
