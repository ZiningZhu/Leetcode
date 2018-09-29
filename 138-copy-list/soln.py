# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        # My solution
        # This is an ugly solution TBH, but AC'ed beating 78% Python solution.
        # First pass to instantiate the new nodes, and save in L.
        # Second pass to fulfill in the "next" links. (The first two passes could be combined to be less ugly)
        # Third pass is to fulfill the "random" link, using the "original node -> index" dictionary.

        if head == None:  # Edge case
            return None
        L = []
        indices = {}  # original node -> index
        # Why not new node -> index? The newly instantiated "random" field might change the hashing.
        # This makes it necessary to keep an L (so I can find the location of new nodes)
        head_ptr = head
        pos = 0
        while head != None:
            nn = RandomListNode(head.label)
            L.append(nn)
            indices[head] = pos
            pos += 1
            head = head.next

        for i in range(len(L)-1):
            L[i].next = L[i+1]

        head = head_ptr
        pos = 0
        while head != None:
            if head.random != None:
                p = indices[head.random]
                L[pos].random = L[p]
            head = head.next
            pos += 1
        return L[0]
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        # Official solution 2
        # If the next node exists (check with a dictionary: old -> new mapping), attach; otherwise create.
        if head == None:
            return None

        nh = RandomListNode(head.label)
        nh_ptr = nh
        head_ptr = head
        D = {}
        while head != None:
            nh.next = self.getNode(D, head.next)
            nh.random = self.getNode(D, head.random)
            head = head.next
            nh = nh.next
        return nh_ptr

    def getNode(self, D, old):
        if old == None:
            return None
        if old in D:
            return D[old]
        else:
            nn = RandomListNode(old.label)
            return nn
