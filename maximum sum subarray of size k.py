import sys
k=3
arr=[1,2,3,4,5,6]
i=0
j=0
s=0
mx=-sys.maxsize
while j<len(arr):
    s+=arr[j]
    if j-i+1<k:
        j+=1
    elif j-i+1 == k:
        mx=max(mx,s)
        s=s-arr[i]
        i+=1
        j+=1
print(mx)
