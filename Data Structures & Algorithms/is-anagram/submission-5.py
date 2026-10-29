class Solution:
    """
        Different approaches:   - Remove each matched character and make sure both are empty -> O(n2)
                                - Count per character using set -> O(n2)
                                - Sort and compare both strings -> O(n log n)
                                - Hashmap to count frequencies and compare maps -> O(n)
                                - Count frequency in array since only 26 characters possible -> O(n)
    """
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        # Time Complexity -> O(n), Space Complexity -> O(1)
        count_s = [0] * 26    
        count_t = [0] * 26  

        for ch in s:
            count_s[ord(ch) - ord('a')] += 1
        
        for ch in t:
            count_t[ord(ch) - ord('a')] += 1
        
        return count_s == count_t
        
