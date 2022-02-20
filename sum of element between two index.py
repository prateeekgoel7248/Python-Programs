from heapq import heappop,heappush
def minh(arr,k):
    heap=[]
    for i in range(len(arr)):
        heappush(heap,-arr[i])
        if len(heap)>k:
            heappop(heap)
    return -heap[0]







arr=[1,3,12,5,15,11]
k1=3
k2=6
f=minh(arr,k1)
s=minh(arr,k2)
print(f,s)
summ=0
for i in arr:
    if i>f and i<s:
        summ+=i
print(summ)
