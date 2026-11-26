class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Special cases:
        I before V and X
        X before L and C
        C before D and M
        """
        conversion = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        output = 0

        for i in range(len(s)):
            if i > 0 and (
                ((s[i] == "V" or s[i] == "X") and s[i - 1] == "I")
                or ((s[i] == "L" or s[i] == "C") and s[i - 1] == "X")
                or ((s[i] == "D" or s[i] == "M") and s[i - 1] == "C")
            ):
                output -= conversion[s[i - 1]]
                output += conversion[s[i]] - conversion[s[i - 1]]
            else:
                output += conversion[s[i]]

        return output
