# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        q = [root]
        nq = []
        ret = [[root.val]]
        level = 1
        while len(q) > 0:
            c = q.pop(0)
            if c.left != None:
                nq.append(c.left)
            if c.right != None:
                nq.append(c.right)
            if len(q) == 0 and len(nq) > 0:
                q = nq[:]
                if level % 2 == 1:
                    ret.append([elem.val for elem in nq[::-1]])
                else:
                    ret.append([elem.val for elem in nq])
                nq = []
                level += 1
        return ret
        
