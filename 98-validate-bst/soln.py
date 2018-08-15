# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    # Valid BST == its pre-order traversal is sorted. Beat 4% solution. Too slow
    '''
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        traversal = self.pre_order(root)
        # Check duplicates
        return len(traversal) == len(set(traversal)) and traversal == sorted(traversal)

    def pre_order(self, root):
        if root == None:
            return []
        else:
            return self.pre_order(root.left) + [root.val] + self.pre_order(root.right)
    '''
    # DFS solution: guaranteed that left first, so you can use a value to store max of current tree
    # Beat 100% Python solution.
    def isValidBST(self, root):
        self.s = None
        return self.check_valid_bst(root)

    def check_valid_bst(self, root):
        if root == None:
            return True

        if self.check_valid_bst(root.left) and root.val > self.s:
            self.s = root.val
            return self.check_valid_bst(root.right)
        else:
            return False
            
