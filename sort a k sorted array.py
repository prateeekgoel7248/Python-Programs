import heapq
from heapq import heappush,heappop
arr=[6,5,3,2,8,10,9]
#it will not work for this because it is not k sorted [1,2,3,4,5,0,5,4,3]
k=3
heap=[]
res=[]
for i in range(len(arr)):
    heapq.heappush(heap,arr[i])
    if len(heap)>k:
        res.append(heappop(heap))
while len(heap)>0:
    res.append(heappop(heap))
#print(heap)
print(res)
