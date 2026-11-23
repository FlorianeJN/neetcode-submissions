# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeInBetween(self, list1: Optional[ListNode], a: int, b: int, list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        a = 1
        b = 3

        0    1    2    3    4
        
        2 -> 4 -> 6 -> 8 -> 10
        ^                   ^

            7 -> 9

        stop when i = a - 1 for first pointer
        stop when i = b + 1 for second pointer
        link list2

        2 -> 7 -> 9 -> 10
        """

        first_idx = 0
        second_idx = 0
        first_pointer = list1
        second_pointer = list1

        # node just before a
        while first_idx < a - 1 and first_pointer:
            first_pointer = first_pointer.next
            first_idx += 1

        # node right after b
        while second_idx < b + 1 and second_pointer:
            second_pointer = second_pointer.next
            second_idx += 1

        # tail of list2
        last_node_of_list2 = list2

        while last_node_of_list2.next:
            last_node_of_list2 = last_node_of_list2.next

        # Link
        first_pointer.next = list2
        last_node_of_list2.next = second_pointer

        return list1




        


        