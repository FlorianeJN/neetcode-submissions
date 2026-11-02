class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        return true if S2 contains a permutation of S1
        We want to find s1 inside s2
        Both strings only contain lowercase letters
        the letters are contiguous

         Exemple:
            s1 = abc            s2 = lecabee
                 ___                   ___

        Thought process:
            - Count s1 (frequency array or counter)
            - go through s2. check substring if ch in s1.
            - for substring use counter or freq array and compare to s1
            - Question about complexity: if i use python counter then more like O(n2) no?
            - Because if every character in s1 then counter for every ch in loop so O(n) * O(len(s1))?
            Basically Brute Force approach

            - So we are going to use a freq array for s1
            - Go though s2 using a window of size s1. adjust and compare freq arrays as we go.
            - When both frequency arrays are the same, permutation found!
            Optimal Sliding Window approach -> Time Complexity: O(n)
        """
        if len(s1) > len(s2):
            return False

        count_s1 = [0] * 26
        count_s2 = [0] * 26

        for ch in s1:
            count_s1[ord(ch) - ord("a")] += 1

        # Add the first characters
        for i in range(len(s1)):
            ch = s2[i]
            count_s2[ord(ch) - ord("a")] += 1

        if count_s2 == count_s1:
            return True

        # Slide the window as we go
        for i in range(len(s1), len(s2)):
            last_ch = s2[i - len(s1)]
            new_ch = s2[i]

            count_s2[ord(last_ch) - ord("a")] -= 1
            count_s2[ord(new_ch) - ord("a")] += 1

            if count_s2 == count_s1:
                return True

        return False
