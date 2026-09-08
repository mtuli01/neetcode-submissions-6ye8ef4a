# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs (root, p, q):
            if root == None: 
                return
            if root.val == p or root.val == q:
                return root
            if p < root.val and q > root.val:
                return root
            elif p < root.val and q < root.val:
                return dfs(root.left, p, q)
            else:
                return dfs(root.right, p, q)
        
        return dfs(root, min(p.val,q.val), max(p.val,q.val))
        