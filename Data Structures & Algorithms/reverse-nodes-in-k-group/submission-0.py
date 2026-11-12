class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Count nodes to know how many full groups exist
        count_nodes = 0
        node = head
        while node:
            count_nodes += 1
            node = node.next

        count_groups = count_nodes // k

        dummy = ListNode(0, head)
        group_prev = dummy          # node just before the current group

        for _ in range(count_groups):
            group_start = group_prev.next   # becomes the tail after reversing

            # Reverse k nodes. Initializing prev to the node after the group
            # means the old head automatically links to the next group.
            prev = self.find_kth_next(group_start, k)
            curr = group_start
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # prev is now the new head of the reversed group
            group_prev.next = prev
            group_prev = group_start        # old head is now the tail

        return dummy.next

    def find_kth_next(self, node, k):
        # Returns the node that comes right after k nodes starting at `node`
        for _ in range(k):
            node = node.next
        return node