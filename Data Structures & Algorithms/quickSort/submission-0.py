# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        """
        Divide and Conquer algorith
        Approach:   - Choose pivot as right most value
                    - Go through array and make sure that less than or
                        equals values to the pivot are on the left
                    - Recursively call method again for left and right parts
        """

        self.quickSortRecursive(pairs, 0, len(pairs) - 1)
        return pairs

    def quickSortRecursive(self, pairs: List[Pair], start: int, end: int) -> None:
        # Base case: One element
        if end - start + 1 <= 1:
            return

        pivot = pairs[end]
        write_idx = start

        # Go from beginning to before pivot
        for read_idx in range(start, end):
            # Move everything < pivot to the left side
            if pairs[read_idx].key < pivot.key:
                pairs[read_idx], pairs[write_idx] = pairs[write_idx], pairs[read_idx]
                write_idx += 1

        # Place pivot in its final position
        pairs[write_idx], pairs[end] = pairs[end], pairs[write_idx]

        # Recursive calls to treat left and right parts
        self.quickSortRecursive(pairs, start, write_idx - 1)
        self.quickSortRecursive(pairs, write_idx + 1, end)
