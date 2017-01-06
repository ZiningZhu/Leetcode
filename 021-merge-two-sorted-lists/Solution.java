/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode res, cr;
        ListNode c1 = l1, c2 = l2;

        // The first node
        if (l1 == null) {
            if (l2 == null) return l1;
            else return l2;
        } else if (l2==null) {
            return l1;
        } else {
            if (l1.val < l2.val) {
                res = l1;
                c1 = l1.next;
            } else {
                res = l2;
                c2 = l2.next;
            }
            cr = res;
        }

        // When neither of l1 and l2 traversal ends
        while (c1 != null && c2 != null) {
            if (c1.val < c2.val) {
                cr.next = c1;
                c1 = c1.next;
                cr = cr.next;
            } else {
                cr.next = c2;
                c2 = c2.next;
                cr = cr.next;
            }

        }

        // After one of the LL traversal ends
        if (c1 == null && c2 == null) {
            return res;
        } else if (c1 != null) {
            cr.next = c1;
            return res;
        } else {
            cr.next = c2;
            return res;
        }
    }
}
