def count_diff(arr,n,d):
    s1=(sum(arr)+d)//2
    print(s1)
    li=arr
    w=s1
    #return subset_sum(arr,len(arr),s1)
    t=[]
    for i in range(n+1):
        res=[]
        for j in range(w+1):
            res.append(10)
            #that value 10 does not do any change , it is only the initial value whichwill chnage in next loop automatically so dont think about it and put any value like 0,1,2,435
            
        t.append(res)
    for i in range(n+1):        
        for j in range(w+1):
            if i==0:
                t[i][j]=0
            if j==0:
                t[i][j]=1
    for i in range(1,n+1):
        for j in range(1,w+1):
            if li[i-1]<=j:
                t[i][j]=t[i-1][j-li[i-1]] + t[i-1][j]
            else:
                t[i][j]=t[i-1][j]
    return t[n][w]
    
arr=[1,1,2,3]
diff=1
print(count_diff(arr,len(arr),diff))
