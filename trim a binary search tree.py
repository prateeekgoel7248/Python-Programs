# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def trimBST(self, root, low, high):
        # def trim(r,l,h):
  		if(root == None) : 
  			return None;    
  		root.left =  self.trimBST(root.left,low,high)
  		root.right = self.trimBST(root.right,low,high)
  		if( low <= root.val and root.val <= high ) :
  			return root;
  		if root.left != None :
  			return root.left;
  		else:
  			return root.right
        
        