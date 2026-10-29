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
        
        count_s = {}
        count_t = {}

        for ch in s:
            count_s[ch] = count_s.get(ch,0) + 1

        for ch in t:
            count_t[ch] = count_t.get(ch,0) + 1
        
        return count_t == count_s
        
