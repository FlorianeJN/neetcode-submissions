class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            n_str = str(n)
            length = len(n_str)
            n = 0

            for i in range(length):
                n += int(n_str[i]) ** 2
                
            if n in seen:
                return False
            elif n == 1:
                return True
            else:
                seen.add(n)

        