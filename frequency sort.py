from collections import Counter
from heapq import heappop,heappush
arr=[1,1,1,3,3,3,2,2,4]
k=2
di=dict()
di=Counter(arr)
heap=[]
for i,j in di.items():
    
    heappush(heap,(-j,i))
   
res=[]
print(heap)
while len(heap)>0:
    res.append(heap[0][1])
    heappop(heap)
print(res)
