# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        elif len(preorder) == 1:
            return TreeNode(preorder[0])
        else:
            head = TreeNode(preorder[0])
            i = 1
            while i < len(preorder) and preorder[i] < preorder[0]:
                i += 1
            head.left = self.bstFromPreorder(preorder[1: i])
            head.right = self.bstFromPreorder(preorder[i: ])
            return head

                    
