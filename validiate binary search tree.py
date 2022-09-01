# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # def isValidBST(self, root):
    def isValidBST(self, root, left = float('-inf'), right = float('inf')):
        return not root or left < root.val < right and self.isValidBST(root.left, left, root.val) and self.isValidBST(root.right, root.val, right)
        """
        :type root: TreeNode
        :rtype: bool
        """
        