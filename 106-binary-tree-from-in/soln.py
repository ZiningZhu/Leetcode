# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0 or len(postorder) == 0:
            return None
        p = postorder[-1]
        inorder_sentinel = inorder.index(p)
        postorder_sentinel = inorder_sentinel

        root = TreeNode(p)
        root.left = self.buildTree(inorder[:inorder_sentinel], postorder[:postorder_sentinel])
        root.right = self.buildTree(inorder[inorder_sentinel+1:], postorder[postorder_sentinel:-1])
        return root
