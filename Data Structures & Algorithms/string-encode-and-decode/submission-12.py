class Solution:

    def encode(self, strs: List[str]) -> str:
        """
            Create a single string from a list of strings
            Use delimiter that says how long is the next word
            [Hello, World] -> 6#Hello5#World
        """
        output = ""
        for s in strs:
            output += f"{len(s)}#{s}"
        return output

    def decode(self, s: str) -> List[str]:
        """
        Use the delimiter to retrieve each word
        6#Hello
        """
        output = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            size = int(s[i:j])
            output.append(s[j + 1 : j + 1 + size])
            i = j + 1 + size
        
        return output
        
