def insert_(stack,temp):
    if len(stack)==0:
        stack.append(temp)
        return stack
    ele = stack.pop()
    insert_(stack,temp)
    stack.append(ele)
    return stack

def revers(stack):
    if len(stack)==1:
        return stack
    temp = stack.pop()
    revers(stack)
    insert_(stack,temp)
    return stack
stack =[1,2,3,4,5]
print(revers(stack))
    
