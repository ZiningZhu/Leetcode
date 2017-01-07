/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {

    public ListNode mergeKLists(ListNode[] lists) {
		if (lists.length == 0) {
		    return null;
		}
		ListNode res = new ListNode(0);
		PriorityQueue<ListNode> pq = new PriorityQueue<ListNode>(new Comparator<ListNode>() {
		    public int compare(ListNode n1, ListNode n2) {
		        if (n1.val > n2.val) {
		            return 1;
		        } else if (n1.val == n2.val) {
		            return 0;
		        } else {
		            return -1;
		        }
		    }
		});


		int num = 0;
		for (ListNode l : lists) {
		    if (l == null) continue;
		    for (ListNode curr = l; curr != null; curr = curr.next) {
		        pq.offer(curr);
		        num++;
		    }
		}

		ListNode c = res;
		while (pq.size() != 0) {
		    c.next = pq.poll();
		    num--;
		    c = c.next;
		    c.next = null; // Important! Otherwise there may be time limitation exceed, since you can't guarantee that the last node of res list has null next attribute.
		}



		return res.next;

	}
}
