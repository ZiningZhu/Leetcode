# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.generateTreesHelper(1, n+1)

    def generateTreesHelper(self, start, end):
        results = []
        for i in range(start, end):
            left_choices = self.generateTreesHelper(start, i)
            right_choices = self.generateTreesHelper(i+1, end)
            if len(left_choices) == 0:
                left_choices = [None]
            if len(right_choices) == 0:
                right_choices = [None]
            for l in left_choices:
                for r in right_choices:
                    tree = TreeNode(i)
                    tree.left = l
                    tree.right = r
                    results.append(tree)
        return results
