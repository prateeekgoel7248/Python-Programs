# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode],left = float('-inf'), right = float('inf')) -> bool:
        return not root or left < root.val < right and self.isValidBST(root.left, left, root.val) and self.isValidBST(root.right, root.val, right)    