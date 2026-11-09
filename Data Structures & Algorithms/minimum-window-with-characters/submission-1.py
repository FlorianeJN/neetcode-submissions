class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
            Brute force: Test every possible substring of length t minimum -> O(n3)

            optimal approach:
            - build frequency map for character in t
            - create frequency map for current window counts
            - need is the count of how many distinct characters are needed
            - have is we the current window actually has
        """

        if len(t) > len(s):
            return ""

        count_t = defaultdict(int)
        window = defaultdict(int)

        for ch in t:
            count_t[ch] += 1
        
        need = len(count_t) # count distinct characters

        start = 0
        have = 0
        min_window = (-1,-1)
        min_window_length = float("inf")

        for end in range(len(s)):
            ch = s[end]
            window[ch] += 1

            if ch in count_t and window[ch] == count_t[ch]:
                have += 1
            
            # valid window so we want to shrink as much as possible
            while have == need:
                # save min_window
                if end - start + 1 < min_window_length:
                    min_window = (start,end)
                    min_window_length = end - start + 1

                # shrink window
                start_ch = s[start]
                window[start_ch] -= 1
                if start_ch in count_t and window[start_ch] < count_t[start_ch]:
                    have -= 1
                start += 1
            
            window_start,window_end = min_window
        return s[window_start:window_end + 1] if min_window_length != float("inf") else ""
            
