# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        L = []
        curr = head
        while curr != None:
            L.append(curr.val)
            curr = curr.next
        return self.buildBST(L, 0, len(L))

    def buildBST(self, L, start, end):
        if start >= end:
            return None
        if end - start == 1:
            return TreeNode(L[start])
        mid = (start + end) // 2
        root = TreeNode(L[mid])
        root.left = self.buildBST(L, start, mid)
        root.right = self.buildBST(L, mid+1, end)
        return root
        
