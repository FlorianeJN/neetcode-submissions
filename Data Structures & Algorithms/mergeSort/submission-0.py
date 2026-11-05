# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        self.mergeSortRecursive(pairs, 0, len(pairs) - 1)
        return pairs

    def mergeSortRecursive(self, pairs: List[Pair], start: int, end: int) ->  List[Pair]:
        # Base case: one element
        if end - start + 1 <= 1:
            return pairs

        mid = (start + end) // 2

        # Recursive calls -> Divide
        self.mergeSortRecursive(pairs, start, mid)
        self.mergeSortRecursive(pairs, mid + 1, end)

        # Merge results -> Conquer
        self.merge(pairs, start, end, mid)

    def merge(self, pairs: List[Pair], start: int, end: int, mid: int) -> None:

        # Copies because values will be overwritten
        left_copy = pairs[start : mid + 1]
        right_copy = pairs[mid + 1 : end + 1]

        i = start
        left_idx = 0
        right_idx = 0

        # Merge values by comparing both arrays
        while left_idx < len(left_copy) and right_idx < len(right_copy):
            left_value = left_copy[left_idx].key
            right_value = right_copy[right_idx].key

            if left_value <= right_value:
                pairs[i] = left_copy[left_idx]
                left_idx += 1
            else:
                pairs[i] = right_copy[right_idx]
                right_idx += 1
            i += 1

        # Merge the rest
        while left_idx < len(left_copy):
            pairs[i] = left_copy[left_idx]
            i += 1
            left_idx += 1

        while right_idx < len(right_copy):
            pairs[i] = right_copy[right_idx]
            i += 1
            right_idx += 1
