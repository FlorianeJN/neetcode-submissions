# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Input:  Head of a singly linked-list
        We want to reorder the nodes such as [0, n-1, 1, n-2, 2, n-3, ...]
        Output: Head of the reordered list

        These numbers represent node positions, not the values stored in the nodes.

        You may not modify the values in the list's nodes, but instead you must 
        reorder the nodes themselves.

        Example:
        Input: head = [2,4,6,8]

        Output: [2,8,4,6]

        Brute force:
            - Go through list each time to get the end and append it. 
            - Keep track of where to append it next
            - So for example take first node. Then append last node.
            - Then increment pointer and go the last node once again
            Time Complexity -> we treat n times and have to go to the end n times so O(n2)?
        
        Optimal approach:
            - We can cut the list in half in the middle and reverse the second half of the list
            - Then merge the two lists
            - So let's take this example : [1,2,3,4]
            - We cut to have two lists: [1,2] and [3,4]
            - Then reverse [3,4] -> [4,3]
            - Then merge the two -> [1,4,2,3]
            Time Complexity -> O(n) multiple passes
            1 2 3 4
        """
        
        # Find the middle using two pointers
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # By this point slow is in the middle
        first = head
        second = slow.next
        slow.next = None

        # Reverse the second list
        reversed_list = reverse_list(second)

        # Merge the two lists
        merge_lists(first,reversed_list)

def merge_lists(list1, list2):
    dummy = ListNode()
    curr = dummy
    i = 0

    while list1 and list2:
        if i % 2 == 0:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next

        i += 1
        curr = curr.next

    curr.next = list1 or list2

def reverse_list(head):
    if not head or not head.next:
        return head
    
    new_head = reverse_list(head.next)

    head.next.next = head
    head.next = None

    return new_head
            

# def reverse_list(head):
#     prev = None
#     curr = head
#     while curr:
#         next = curr.next
#         curr.next = prev
#         prev = curr
#         curr = next
#     return prev
