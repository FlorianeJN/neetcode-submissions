class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        count = [0] * 26
        longest = 0

        for end in range(len(s)):
            ch = s[end]

            count[ord(ch) - ord("A")] += 1

            window_is_invalid = max(count) + k < (end - start + 1)

            if window_is_invalid:
                count[ord(s[start]) - ord("A")] -= 1
                start += 1

            longest = max(longest, end - start + 1)

        return longest
