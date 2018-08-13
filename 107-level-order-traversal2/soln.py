# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        ret = [[root.val]]
        q = [root]
        nq = []
        while len(q) > 0:
            c = q.pop(0)
            if c.left != None:
                nq.append(c.left)
            if c.right != None:
                nq.append(c.right)
            if len(q) == 0:
                if len(nq) > 0:
                    ret.append([elem.val for elem in nq])
                q = nq[:]
                nq = []
        return ret[::-1]
