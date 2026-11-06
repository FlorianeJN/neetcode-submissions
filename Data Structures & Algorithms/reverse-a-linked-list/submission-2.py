# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Recursive approach -> O(n)
        """
        # Base cases
        if head is None or head.next is None:
            return head

        # Go to the end
        new_head = self.reverseList(head.next)

        # Reverse the links
        head.next.next = head
        head.next = None

        return new_head

        