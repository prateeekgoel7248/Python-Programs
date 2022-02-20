def insert_in(arr,ele):
    if len(arr)==0 or arr[-1]<=ele:
        arr.append(ele)
        return arr
    temp = arr.pop()
    arr = insert_in(arr,ele)
    arr.append(temp)
    return arr
    
def sort(arr):
    if len(arr)==1:
        return arr
    ele = arr[len(arr)-1]
    arr.pop()
    arr = sort(arr)
    arr = insert_in(arr,ele)
    return arr
arr=[1,4,3,2,1,6,4,2]
print(sort(arr))
    
    
    
    
