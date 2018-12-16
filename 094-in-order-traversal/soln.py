# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]

        # Recursive solution is trivial. Want another solution.
        if root == None:
            return []
        else:
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        """

        # Any recursive code can be written into iterative solutions
        if root == None:
            return []
        st = [root]
        ans = []
        while len(st) > 0:
            curr = st.pop()

            if curr.left != None:
                ncurr = TreeNode(curr.val)
                ncurr.right = curr.right
                st.append(ncurr)
                st.append(curr.left)
                continue
            else:
                ans.append(curr.val)
                if curr.right != None:
                    st.append(curr.right)
        return ans
