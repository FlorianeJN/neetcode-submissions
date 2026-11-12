# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        return self.divide(lists, 0 , len(lists) - 1)

    def divide(self, lists, start, end):
        if start == end:
            return lists[start]

        mid = (start + end) // 2
        left = self.divide(lists, start, mid)
        right = self.divide(lists, mid + 1, end)
        return self.merge(left,right)
    
    def merge(self, a, b):
        dummy = tail = ListNode(-1)

        while a and b:
            if a.val <= b.val:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next

        tail.next = a or b
        return dummy.next


        