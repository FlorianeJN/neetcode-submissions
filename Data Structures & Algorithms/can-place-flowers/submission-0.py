class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if len(flowerbed) == 1 and flowerbed[0] == 1:
            return True if n == 0 else False

        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return True if n == 1 or n == 0 else False

        i = 0
        while i < len(flowerbed) and n > 0:
            if flowerbed[i] == 0:
                # we are at the beginning
                if i == 0 and flowerbed[i + 1] == 0:
                    n -= 1
                    flowerbed[i] = 1

                # we are at the end
                elif i == len(flowerbed) - 1 and flowerbed[i - 1] == 0:
                    n -= 1

                else:
                    if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                        n -= 1
                        flowerbed[i] = 1
            i += 1

        return n == 0
