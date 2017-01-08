/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode swapPairs(ListNode head) {
        if (head == null || head.next == null)
            return head;
        ListNode prev = head;
        ListNode a = head;
        ListNode b = a.next;

        while (a != null && b != null) {
            if (prev == head) head = b;
            prev.next = b;
            prev = a;
            a.next = b.next;
            b.next = a;


            if (a.next == null) break;
            a = a.next;
            if (a.next == null) break;
            b = a.next;
        }



        return head;
    }
}
