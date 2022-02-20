def pattern(ip,op):
    if len(ip)==0:
        print("Output : ",op)
        return
    op1=op
    op2=op
    op1+=ip[0]
    op2+= chr(ord(ip[0])-32)
    pattern(ip[1:],op1)
    pattern(ip[1:],op2)
    return

patt = "ab"
op=""
pattern(patt,op)
