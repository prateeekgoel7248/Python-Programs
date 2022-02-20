def pattern(op,cl,out,res):
    if (op==0 and cl ==0):
        res.append(out)
        return
    if op==cl:
        op1=out
        op1+="("
        pattern(op-1,cl,op1,res)
        return
    if cl>op:
        if op>0:
            op2=out
            op2+="("
            pattern(op-1,cl,op2,res)
            
        if cl>0:
            op3=out
            op3+=")"
            pattern(op,cl-1,op3,res)
        return
    
    else:
        #this else is not needed here 
        if op>0:
            op4=out
            op4+="("
            pattern(op-1,cl,op4,res)
        return





res=[]
out=""
n=3
#out="("
#without "(" and n-1 will also be run.
pattern(n,n,out,res)
print(res)
