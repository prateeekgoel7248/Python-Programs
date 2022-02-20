def solve(op,n,ones,zeros):
    if n==0:
        ans.append(op)
        return
    if ones<=zeros:
        solve(op+"1",n-1,ones+1,zeros)
    else:
        solve(op+"0",n-1,ones,zeros+1)
        solve(op+"1",n-1,ones+1,zeros) #for all the combination of the string having more ones compare to zeros or both are equal

n=5
ans=[]
solve("",n,0,0)
print(ans)
