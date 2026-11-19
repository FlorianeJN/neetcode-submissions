class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count = len(s)
        i = j = 0
        while count > 0 and i < len(s) and j < len(t):
            if s[i] == t[j]:
                count -= 1
                i += 1
            j += 1
        return count == 0
        