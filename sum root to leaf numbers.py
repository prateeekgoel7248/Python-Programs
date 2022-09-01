# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        allSubs = []
        
        def dfs(node, subset):
            if not (node.left or node.right):
                subset.append(node.val)
                allSubs.append(subset[:])
                return
            
            subset.append(node.val)
            if node.left:
                dfs(node.left, subset[:])
            if node.right:
                dfs(node.right, subset[:])
                
        dfs(root, [])
        # print(allSubs)
        
        retval = 0
        for i in range(len(allSubs)):
            # create int
            retval += int(''.join([str(i) for i in allSubs[i]]))
            
        return retval
        