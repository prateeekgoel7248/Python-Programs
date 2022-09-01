# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # print("goel")
        if not root:
            return ""
        s=""
        q=[root]
        while q:
            # print(q)
            node = q.pop(0)
            if not node:
                s+="#,"
            else:
                s+=str(node.val)+','
            if node:
                q.append(node.left)
                q.append(node.right)
        # print("Hello")
        return s
            
                
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data)==0:
            return None
        # s=""
        lis = data.split(',')
        root = TreeNode(int(lis[0]))
        i=1
        q=[root]
        while q:
            node=q.pop(0)
            ele = lis[i]
            i+=1
            if ele =='#':
                node.left = None
            else:
                left = TreeNode(int(ele))
                node.left = left
                q.append(left)
            ele = lis[i]
            i+=1
            if ele =='#':
                node.right = None
            else:
                right = TreeNode(int(ele))
                node.right = right
                q.append(right)
        return root
            
            
        
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans