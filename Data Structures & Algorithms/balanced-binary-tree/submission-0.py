# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def tree_bal(root):
            if root == None:
                return 0

            d_l = tree_bal(root.left)
            d_r = tree_bal(root.right)

            if d_l is False or d_r is False:
                return False
                                
            if abs(d_l - d_r) > 1:
                return False
            return 1 + max(d_l, d_r)
        return tree_bal(root) is not False