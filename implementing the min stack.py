ss=[]
def push(arr, ele):
    # if :
    arr.append(ele)
    if len(ss)==0 or ss[-1]>=arr[-1]:
        ss.append(ele)
    # return
            
    # Code here

# Function should pop an element from stack
def pop(arr):
    if isEmpty(arr):
        return -1
    ans=s.pop()
    if ans==ss[-1]:
        ss.pop()
    return ans
    # Code here

# function should return 1/0 or True/False
def isFull(n, arr):
    if len(arr)==n:
        return True
    else:
        return False
    # Code here

# function should return 1/0 or True/False
def isEmpty(arr):
    if len(arr)==0:
        return True
    else:
        return False
    #Code here

# function should return minimum element from the stack
def getMin(n, arr):
    if isEmpty(ss):
        return -1
    else:
        return ss[-1]
        
    # Code here
        

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        stack = []
        while(not isEmpty(stack)):
            pop(stack)
            
        for i in range(n):
            push(stack, arr[i])
        print(getMin(n, stack))
# contributed by: Harshit Sidhwa

# } Driver Code Ends
