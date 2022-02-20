k=3
arr=[12,-1,-7,8,-15,30,16,28]
i=j=0
res=[]
temp=[]
while j<len(arr):
    if arr[j]<0:
        temp.append(arr[j])
    if j-i+1<k:
        j+=1
    elif j-i+1==k:
        if len(temp)>0:
            res.append(temp[0])
            if arr[i]<0:
                temp.pop(0)
            #temp=temp[1:]
        else:
            res.append(0)
        i+=1
        j+=1
print(res)
            
#print(temp)
