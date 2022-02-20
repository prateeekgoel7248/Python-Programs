def pattern(ip,op,res):
    if len(ip)==0:
        #print("Output : ",op)
        res.append(op)
        return res
    if ip[0].isdigit():
        op1=op
        op1+=ip[0]
        pattern(ip[1:],op1,res)
        
        return
    
    op1=op
    op2=op
    
    op1+=ip[0].lower()
    op2+=ip[0].upper()
    pattern(ip[1:],op1,res)
    pattern(ip[1:],op2,res)
    return

patt = "a1b3"
op=""
res=[]
pattern(patt,op,res)
print(res)
