class Solution {
    public boolean isPalindrome(String s) {
        int right = 0;
        int left = s.length() - 1;

        while(right < left){
            while(right < left && !isValidCharacter(s.charAt(right))) right++;
            while(right < left && !isValidCharacter(s.charAt(left))) left--;

            char rightC = s.charAt(right);
            char leftC = s.charAt(left);

            if(Character.toLowerCase(rightC) != Character.toLowerCase(leftC)) return false;
            right++;
            left--;
        }

        return true;
    }

    private static boolean isValidCharacter(char c) {
        boolean betweenAZ = c >= 'a' && c <= 'z' || c >= 'A' && c <= 'Z';
        boolean between09 = c >= '0' && c <= '9';

        if (betweenAZ || between09)
            return true;
        return false;
    }
}
