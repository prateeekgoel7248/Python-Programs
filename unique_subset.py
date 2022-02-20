
def solve(ip,op,res):
    if len(ip)==0:
        res.append(op)
        #print("output : ",op)
        return
    op1 = op
    op2 = op
    op2=op2 + ip[0]
    
    ip=ip[1:]
    solve(ip,op1,res)
    solve(ip,op2,res)
    return
strin = "aac"
res=[]
solve(strin,"",res)
res = sorted(res)
#print(res)
print(set((res)))
    
