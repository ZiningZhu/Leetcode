# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if len(pre) == 0:
            return None
        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root

        i = 0
        while post[i] != pre[1]:
            i += 1
        i += 1
        # pre[1] is the root of left child.
        # Now i is the sentinel
        # This gives a bug-free possibility for the case [2,1,3], [3,1,2]
        # If we use index() to find sentinel, some errors might occur

        root.left = self.constructFromPrePost(pre[1: i+1], post[: i])
        root.right = self.constructFromPrePost(pre[i+1:], post[i:-1])
        return root
