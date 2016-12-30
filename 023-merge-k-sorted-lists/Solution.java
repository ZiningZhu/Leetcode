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
		/** The online priority queue solution. Just cast everything into a priority queue, and then perform N ExtractMin() operations. O(NlogN) time and O(N) space. Note that this does not even need the k inputs to be sorted.
		**/
		// FIXME - memory limit exceeded when doing [[-2,-1,-1,-1],[]]
		if (lists.length == 0) {
			return null;
		}

		PriorityQueue<ListNode> pq = new PriorityQueue<ListNode>(new Comparator<ListNode>() {
			public int compare(ListNode o1, ListNode o2) {
				if (o1.val < o2.val) return -1;
				else if (o1.val == o2.val) return 1;
				else return 1;
			}
		});

		ListNode res = new ListNode(0);

		ListNode curr = lists[0];
		for (int i = 0; i < lists.length; i++) {
			curr = lists[i];
			if (curr == null) continue;
			while (curr.next != null) {
			    pq.offer(curr);
			    curr = curr.next;
			}
			pq.add(curr);


		}
        //System.out.println("Size of pq: " + pq.size());
        curr = res;
		while (pq.size() > 0) {
			ListNode p = pq.remove();
			curr.next = p;
			curr = curr.next;
			//System.out.println("Size of pq: " + pq.size());
		}
		res = res.next;
		return res;

	}
}
