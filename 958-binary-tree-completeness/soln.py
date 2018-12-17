# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # Count the number of nodes in this tree as N
        N = self.bfs_count(root, 0)

        # For each node, if the level-order-traversal-index >= N, then not complete.
        return self.bfs_check(root, 0, N)

    def bfs_count(self, root, n):
        if root == None:
            return n
        return self.bfs_count(root.left, 0) + 1 + self.bfs_count(root.right, 0)

    def bfs_check(self, root, i, N):
        if root == None:
            return True
        if i >= N:
            return False
        return self.bfs_check(root.left, 2*i+1, N) and self.bfs_check(root.right, 2*i+2, N)
