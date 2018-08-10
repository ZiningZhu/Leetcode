# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # Codes for removing duplicates
        """
        prev = head
        curr = prev
        while curr.next != None:
            curr = curr.next
            if curr.val != prev.val:
                prev.next = curr
                prev = curr
            else:
                prev.next = None
        return head
        """
        # Delete duplicates. Beat 100% solutions.
        dummy_head = ListNode("sth")
        dummy_head.next = head
        prev = dummy_head
        curr = dummy_head
        nxt_ = dummy_head.next

        while nxt_ != None:
            if nxt_.val == curr.val:
                nxt_ = nxt_.next
                prev.next = None
            else:
                # nxt_ is the first "new" value
                if curr.next == nxt_:
                    prev = curr
                    curr = nxt_
                    nxt_ = nxt_.next
                else:
                    prev.next = nxt_
                    curr = nxt_
                    nxt_ = nxt_.next

        return dummy_head.next




                
