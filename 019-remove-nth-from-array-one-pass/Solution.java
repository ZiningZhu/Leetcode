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

/** https://discuss.leetcode.com/topic/7031/simple-java-solution-in-one-pass/2
* (1) Uses a gap of n+1 instead of n, so that the slow pointer in the solution points to the "prev" position in my code
* (2) Uses a sentinel to add before the first element, to account for the irregularily of removing the first element. (My method of handling it is to set up a flag)
**/
