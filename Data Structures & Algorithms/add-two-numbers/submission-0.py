# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Brute Force: convert each list to an integer, add, convert the sum back to a list.
                    O(N + M), but huge integers can overflow in fixed-size languages.

        Optimal :   walk both lists at once, adding digits plus a carry (digits are already
                    least-significant first). Append each result digit as we go.
                    O(max(N, M)) time.
        """

        dummy = ListNode()
        curr = dummy
        carryover = 0

        while l1 or l2 or carryover != 0:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            val = l1_val + l2_val + carryover

            new_node = ListNode(val % 10)
            carryover = val // 10

            curr.next = new_node
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
