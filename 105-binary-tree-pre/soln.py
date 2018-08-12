# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # The first element in preorder is root; everything before root in inorder traversal is left tree.
        # Now you have the preorder and inorder traversal for left & right tree respectively. Recurse this procesure.
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        p = preorder[0]

        inorder_sentinel = inorder.index(p)
        preorder_sentinel = 1 + inorder_sentinel

        root = TreeNode(p)
        root.left = self.buildTree(preorder[1:preorder_sentinel], inorder[:inorder_sentinel])
        root.right = self.buildTree(preorder[preorder_sentinel:], inorder[inorder_sentinel+1:])
        return root
                
