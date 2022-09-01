# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        
        def dfs(root):
            if root:
                if root.left and not root.left.left and not root.left.right:
                    self.sum += root.left.val
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        return self.sum