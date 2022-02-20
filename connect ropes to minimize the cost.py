from heapq import heappop,heappush
heap=[]
cost=0
arr=[1,2,3,4,5]
for i in range(len(arr)):
    heappush(heap,arr[i])
while len(heap)>1:
    f=heap[0]
    heappop(heap)
    s=heappop(heap)
    cost+=f+s
    heappush(heap,f+s)
print(cost)
