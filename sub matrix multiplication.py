# def anss(mat):
#     ans=1
#     for i in range(len(mat)):
#         for j in range(len(mat)):
#             ans=ans*mat[i][j]
#     return ans
def solve(n,arr,length):
    for i in range(1,len(array)+1):
        for j  in range(1,len(array[0])+1):
            t[i][j]=(t[i-1][j]*t[i][j-1]*arr[i-1][j-1])//t[i-1][j-1]
    result=[]
    temp_arr=0
    for i in range(1,len(arr)+1):
        for j in range(1,len(arr[0])+1):
            if i-length>=0 and j-length>=0:
                temp_arr = ((t[i][j])//(t[i-length][j]*t[i][j-length]))*t[i-length][j-length]
                result.append(temp_arr)
    # ansss=
    # result.append(anss(temp_arr))
    return result
    
# t=    
n=3
l=2
array=[[3,2,6],[2,3,4],[5,18,10]]
t=[]
for i in range(len(array)+1):
    res=[]
    for j in range(len(array[0])+1):
        res.append(1)
    t.append(res)
print(solve(n,array,l))
