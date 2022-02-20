import heapq
#from heapq import headpush,headpop
arr=[7,10,4,3,20,15]
k=3
heap=[]
for i in range(len(arr)):
    heapq.heappush(heap,arr[i])
    if len(heap)>k:
        heapq.heappop(heap)
#print(heap)
print(heap[0])
