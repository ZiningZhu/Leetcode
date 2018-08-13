# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    '''
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.min_depth = float("inf")
        if root == None:
            return 0
        self.dfs_visit(root, 1)
        return self.min_depth

    def dfs_visit(self, c, depth):
        if c.left == None and c.right == None:
            self.min_depth = min(self.min_depth, depth)
        else:
            if depth > self.min_depth:  # Give up on this branch
                return
            if c.left != None:
                self.dfs_visit(c.left, depth+1)
            if c.right != None:
                self.dfs_visit(c.right, depth+1)
    '''
    def minDepth(self, root):
        # BFS solution
        if root == None:
            return 0
        q = [root]
        nq = []
        level = 1
        while len(q) > 0:
            c = q.pop(0)
            if c.left == None and c.right == None:

            if c.left != None:
                nq.append(c.left)
            if c.right != None:
                nq.append(c.right)
            if len(q) > 0:
                q = nq[:]
        
