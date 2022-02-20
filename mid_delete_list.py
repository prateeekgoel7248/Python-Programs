def d(arr,m):
    if m==1:
        arr.pop()
        return
    temp = arr.pop()
    d(arr,m-1)
    arr.append(temp)
    return arr
arr=[1,2,3,4,5]
print(d(arr,4))
    
    
