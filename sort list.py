# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # def sortList(self, head):
    def findMid(self, node):
        slow = fast = node
        
	'''
		Here the condition is till fast.next.next. 
		Because, we need to should stop at first mid in case of even length, else we won't be breaking the array equally.
		
		Example: 1->2->3->4, here we have to break at 2 so that the list will become 1 -> 2 and 3 -> 4 
		if we break at 3 the list will become 1 -> 2 -> 3 and 4 which is incorrect 
		'''
        while(fast.next and fast.next.next):
            fast = fast.next.next
            slow = slow.next
        
        return slow
    
    def merge(self, node1, node2):
        dummy = cur = ListNode()
        intMax = float('inf')
        
        while(node1 or node2):
            value1, value2 = node1.val if(node1) else intMax, node2.val if(node2) else intMax
            if(value1 < value2):
                cur.next = node1
                node1 = node1.next
            else:
                cur.next = node2
                node2 = node2.next
            cur = cur.next
            
        return dummy.next
            
    def mergeSort(self, node):
		# Incase of single node or empty node we don't have to do anything.
        if(node is None or node.next is None):  return node
        
        mid = self.findMid(node) #Find the mid
        nextNode = mid.next #Get the start of second half 
        mid.next = None #Break at mid
        
        firstHalf = self.mergeSort(node)
        secondHalf = self.mergeSort(nextNode)
        
        return self.merge(firstHalf, secondHalf)
        
    
    def sortList(self, head):
        return self.mergeSort(head)
        """
        :type head: ListNode
        :rtype: ListNode
        """
        