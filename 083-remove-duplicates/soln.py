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
        prev = head
        curr = head
        if curr == None:  # Bang! WA'ed on this edge case
            return None
        while curr.next != None:
            curr = curr.next
            if curr.val != prev.val:
                prev.next = curr
                prev = curr
            else:
                prev.next = None
        return head

        
