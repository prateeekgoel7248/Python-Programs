from heapq import heappop,heappush
heap=[]
arr=[[1,3],[-2,2],[5,8],[0,1]]
k=2
for i in range(len(arr)):
    heappush(heap,(-(arr[i][0]*arr[i][0]+arr[i][1]*arr[i][1]),(arr[i])))
    if len(heap)>k:
        heappop(heap)
res=[]
while len(heap)>0:
    res.append(heap[0][1])
    heappop(heap)
print(res)
