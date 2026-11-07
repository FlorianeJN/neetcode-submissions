# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Brute force -> go through the list and count how many nodes and then
        go once again with count - n and remove that node. O(n) two passes

        Another approach -> Recursively go to end and on the way back up remove 
        nth node. O(n) too?

        Another approach -> Use two pointers and keep a distance of n + 1 between 
        them so that when j ends,i is at the right spot. O(n) one pass
        """

        dummy = ListNode(0,head)
        left = right = dummy

        for _ in range(n + 1):
            right = right.next
        
        while right:
            right = right.next
            left = left.next

        left.next = left.next.next

        return dummy.next

        




        