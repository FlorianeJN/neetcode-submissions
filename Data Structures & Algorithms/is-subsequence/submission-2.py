class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Input -> Two string t and s
        Output -> Boolean indicating wheter s is a subsequence of t

        Brute force approach:   - Use nested loops to find each for
                                    a character in s. Make sure to check bounds 
                                    (to keep relative order)
                                Time Complexity -> O(n2)

        Two pointer approach:   - Go through t
                                - Look for the next character in s
                                - Increment i whenever we find and incr i
                                - By the end, i should be len(s)
                                Time Complexity -> O(n)
        """

        i = 0

        for ch in t:
            if i < len(s) and ch == s[i]:
                i += 1

        return i == len(s)
