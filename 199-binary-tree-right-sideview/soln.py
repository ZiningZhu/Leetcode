# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        soln = []
        if root == None:
            return []
        queue = [(root, 1)]
        while len(queue) > 0:
            curr, depth = queue.pop(0)
            if depth > len(soln):
                soln.append(curr.val)
            if curr.right != None:
                queue.append((curr.right, depth+1))
            if curr.left != None:
                queue.append((curr.left, depth+1))
        return soln
