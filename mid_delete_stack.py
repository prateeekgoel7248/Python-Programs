def d(arr,m):
    if m==1:
        arr.pop()
        return
    temp = arr.pop()
    d(arr,m-1)
    arr.append(temp)
    return arr
stack=[1,2,3,4,5]
print(d(stack,3))
    
    
