from collections import Counter
s="cbaebabacd"
ptr="abc"
k=len(ptr)
d=Counter(ptr)
#print(d)
i=0
j=0
count=len(d)
ans=0
#print(count)
while j<len(s):
    if s[j] in d:
        d[s[j]]-=1
        if d[s[j]]==0:
            count-=1
    
    if j-i+1<k:
        j+=1
    elif j-i+1==k:
        if count==0:
            print(i,j)
            ans+=1
            
        if s[i] in d:
            d[s[i]]+=1
            if d[s[i]]==1:
                count+=1
        
        i+=1
        j+=1
print(ans)
print(chr(20))
        
