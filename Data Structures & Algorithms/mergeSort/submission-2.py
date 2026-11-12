# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        self.merge_sort(pairs,0,len(pairs) - 1)
        return pairs

    def merge_sort(self, pairs: List[Pair], start: int, end: int):
        if end - start + 1 <= 1:
            return
        
        mid = (end + start) // 2

        # Divide -> split array in half
        self.merge_sort(pairs,start,mid)
        self.merge_sort(pairs,mid + 1 , end)

        # Conquer -> Merge sorted halves
        self.merge(pairs,start,end,mid)

    
    def merge(self, pairs: List[Pair], start: int, end: int, mid: int):
        first = pairs[start:mid + 1]
        second = pairs[mid + 1 : end + 1]
        idx = start
        i = 0
        j = 0

        while i < len(first) and j < len(second):
            if first[i].key <= second[j].key:
                pairs[idx] = first[i]
                i += 1
            else:
                pairs[idx] = second[j]
                j += 1
            idx += 1

        while i < len(first):
            pairs[idx] = first[i]
            idx += 1
            i += 1

        while j < len(second):
            pairs[idx] = second[j]
            idx += 1
            j += 1


