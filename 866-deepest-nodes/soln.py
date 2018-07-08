# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    depth = 0
    ret = None
    need_collect = 1

    def count_deepest(self, root):
        depth = 0
        need_collect = 0
        queue = [(0, root)]
        while len(queue) > 0:
            ch, curr = queue.pop(0)
            if ch == depth:
                need_collect += 1
            if ch > depth:
                depth = ch
                need_collect = 1
            if curr.left:
                queue.append((ch+1, curr.left))
            if curr.right:
                queue.append((ch+1, curr.right))
        return need_collect, depth

    def collect(self, curr, ch):
        # DFS can achieve "the deepest one is returned before its parents"
        if not curr:
            return 0
        can_recall = 0
        if ch == self.depth:
            can_recall += 1
            # Detail: why not directly return here? Edge case: input [1].
            # It is possible that the deepest leaf needs to be returned.

        can_recall += self.collect(curr.left, ch+1)
        can_recall += self.collect(curr.right, ch+1)
        if can_recall == self.need_collect and not self.ret:
            self.ret = curr
        return can_recall

    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # Count the number of deepest nodes.
        # Then collect. (Needs some backtracking)

        self.need_collect, self.depth = self.count_deepest(root)
        self.ret = None
        self.collect(root, 0)
        return self.ret
