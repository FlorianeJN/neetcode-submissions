class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Input: two strings word1 and word2
        We need to construct a new string by merging them in alternating order

        Question: The order is always w1 -> w2?
        Can one of them (or both) be empty?
        """

        i = 0
        output = []

        while i < len(word1) and i < len(word2):
            output.append(word1[i])
            output.append(word2[i])
            i += 1

        while i < len(word1):
            output.append(word1[i])
            i += 1

        while i < len(word2):
            output.append(word2[i])
            i += 1

        return "".join(output)


        