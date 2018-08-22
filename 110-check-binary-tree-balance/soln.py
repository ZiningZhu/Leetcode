# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        height, balanced = self.compute_height_and_balance(root)
        return balanced

    def compute_height_and_balance(self, root):
        if root == None:
            return 0, True
        lheight, lbalanced = self.compute_height_and_balance(root.left)
        rheight, rbalanced = self.compute_height_and_balance(root.right)
        curr_height = max(lheight, rheight) + 1
        if (not lbalanced) or (not rbalanced) or abs(lheight - rheight) > 1:
            return curr_height, False
        else:
            return curr_height, True

        
