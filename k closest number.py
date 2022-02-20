import heapq
from heapq import heappop , heappush
heap=[]
res=[]
arr=[5,6,7,8,9]
k=3
x=7
for i in range(len(arr)):
    heappush(heap,(-abs(x-arr[i]),arr[i]))
    if len(heap)>k:
        heappop(heap)
#print(heap)
while len(heap)>0:
    
    res.append(heap[0][1])
    #print(res)
    heappop(heap)
print(res)
