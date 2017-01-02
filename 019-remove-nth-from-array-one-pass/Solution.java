/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {

        int i = 0;
        ListNode prev = head;
        ListNode rem = head;
        boolean flag = true;
        for (ListNode curr = head; curr != null; curr = curr.next) {

            if (i < n) {
                i++;
                continue;
                // just moving the curr node
            } else {
                flag = false;
                // Now move curr and rem simultaneously

                prev = rem;
                rem = rem.next;
            }
        }
        if (flag) { // Remove the first element
            return head.next;
        }

        // Now curr points to one after the last, rem is the nth node counting from the last
        prev.next = rem.next;
        return head;
    }
}
