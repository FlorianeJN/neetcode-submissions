class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        we have a string with only uppercase english characters
        replace k characters with any other uppercase english character
        return length of longest substring that has ONLY ONE DISTINCT CHARACTER

        XYYX k=2 => YYYY or XXXX

        AAABABB k=1

        Brute force => Use nested loops to find all substrings
        that has distinct characters. Append k times to the longest one

        Optimal approach => Sliding window to find longest and append to that
         0 1 2 3 4 5 6 7 8
         A B C D D E D F D G k=1
             _

        count_most_freq = 1
        k = 1
        len(window)= 2

        1 + 1 = 2 < 3

        INVALID WHEN count_most_freq + k < len(window)

        Thought process:
        - Use sliding window approach
        - window is invalid when count_most_freq + k < len(window)
        - when invalid window move left += 1?
        - when valid window move right += 1
        - stop when right reaches the end of string?
        - since we have 26 characters, we can track frequency with arr[26].
        - Get most frequent using max(arr) in python?

        """

        max_len = 0
        count = [0] * 26
        i, j = 0, 0

        while j < len(s):
            ch = s[j]
            count[ord(ch) - ord("A")] += 1
            current_window_len = j - i + 1

            count_most_freq = max(count)

            # Invalid window
            if count_most_freq + k < current_window_len:
                ch_at_i = s[i]
                count[ord(ch_at_i) - ord("A")] -= 1
                i += 1

            max_len = max(max_len, j - i + 1)
            j += 1

        return max_len
