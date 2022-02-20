def solve(arr,k,index,res):
    if len(arr)==1:
        res = arr[0]
        print(res)
        return res
    
    index = (index+k)%len(arr)
    del(arr[index])
    res = solve(arr,k,index,res)
    return res
    
n=40
arr=[]
for i in range(n):
    arr.append(i+1)
k=7
res=0
index=0
res = solve(arr,k-1,index,res)
print(res)
