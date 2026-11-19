class Solution:
    def compress(self, chars: list[str]) -> int:
        """
        Use read and right pointers
        O(n) time
        O(1) space
        """
        read = write = 0
        while read < len(chars):
            count = 0
            cur_char = chars[read]
            # count consecutive repeating characters
            while read < len(chars) and chars[read] == cur_char:
                read += 1
                count += 1

            # write the character
            chars[write] = cur_char
            write += 1
            if count > 1:
                # write the count
                for ch in str(count):
                    chars[write] = ch
                    write += 1
        return write
