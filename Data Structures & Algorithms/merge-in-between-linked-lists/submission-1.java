/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode mergeInBetween(ListNode list1, int a, int b, ListNode list2) {
        int firstIndex = 0;
        int secondIndex = 0;

        ListNode firstPointer = list1;
        ListNode secondPointer = list1;
        ListNode lastNodeOfList2 = list2;

        while (firstPointer != null && firstIndex < (a - 1)) {
            firstPointer = firstPointer.next;
            firstIndex++;
        }

        while (secondPointer != null && secondIndex < (b + 1)) {
            secondPointer = secondPointer.next;
            secondIndex++;
        }

        while (lastNodeOfList2.next != null) {
            lastNodeOfList2 = lastNodeOfList2.next;
        }

        firstPointer.next = list2;
        lastNodeOfList2.next = secondPointer;

        return list1;
    }
}
