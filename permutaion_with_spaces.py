def pattern(ip,op):
    if len(ip)==0:
        print("output",op)
        return
    op1=op
    op2=op
    op1+=ip[0]
    op2+=" "
    op2+=ip[0]
    pattern(ip[1:],op1)
    pattern(ip[1:],op2)
    return 


pattern_input = "ABC"
op=pattern_input[0]
pattern(pattern_input[1:],op)
    
