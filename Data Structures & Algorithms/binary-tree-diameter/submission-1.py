# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diam = 0
        def height(root):
            nonlocal max_diam #reference the parent function variable, work on it
            if root == None:
                return 0
            d_l = height(root.left)
            d_r = height(root.right)
            max_diam = max(max_diam, d_l + d_r)
            return 1 + max(d_l, d_r)
        height(root)
        return max_diam