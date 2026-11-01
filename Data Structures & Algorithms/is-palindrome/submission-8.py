class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Not case sensitive and ignore all non-alphanumeric char

        Brute force approach: Reverse the string and compare to original string : O(n) but space complexity O(n)

        Optimal approach: Two pointers, one at beginning, one at end: O(n) and O(1) space complexity
        
        """
        i = 0
        j = len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
        
        