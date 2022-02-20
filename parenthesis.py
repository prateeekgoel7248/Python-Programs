def pattern(op,cl,out,res):
    if (op==0 and cl ==0):
        res.append(out)
        return
    if op!=0:
        op1=out
        op1+="("
        pattern(op-1,cl,op1,res)
        return
    if cl>op:
        op3=out
        op3+=")"
        pattern(op,cl-1,op3,res)
        return
            






res=[]
out=""
n=3

#without "(" and n-1 will also be run.
pattern(n,n,out,res)
print(res)
