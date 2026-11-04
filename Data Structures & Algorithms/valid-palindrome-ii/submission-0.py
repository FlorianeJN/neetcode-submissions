class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        Input ->    string
        Output ->   boolean indicating whether or not the string can become a palindrome
                    after deleting at most one character

        Constraints ->  - The string only has lowercase English letters
                        - An empty string is a palindrome

        Brute force approach: Try every possible deletion and check each result

        Two pointer approach: Use two pointers. When a mismatch occurs, check if either
                              substring (removing each character) is a palindrome.
        """

        if is_palindrome(s):
            return True

        start = 0
        end = len(s) - 1

        while start < end:
            if s[start] != s[end]:
                break

            start += 1
            end -= 1

        first_substring = s[start:end]
        second_substring = s[start + 1 : end + 1]

        return is_palindrome(first_substring) or is_palindrome(second_substring)


def is_palindrome(s: str) -> bool:
    start = 0
    end = len(s) - 1

    while start < end:
        if s[start] != s[end]:
            return False

        start += 1
        end -= 1

    return True
