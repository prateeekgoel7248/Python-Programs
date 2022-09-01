class Solution(object):
    def trap(self, height):
        #optimal Approach
        
        left=0
        right=len(height)-1
        mxl=0
        mxr=0
        res=0
        while left<=right:
            if height[left]<=height[right]:
                if height[left]>=mxl:
                    mxl=height[left]
                else:
                    res+=mxl-height[left]
                left+=1
            else:
                if height[right]>=mxr:
                    mxr=height[right]
                else:
                    res+=mxr-height[right]
                right-=1
        return res
        
        
        
        
#         #better Approach
#         s=0
#         mxl=[]
#         mxr=[]
#         n=len(height)-1
#         mxl.append(height[0])
#         for i in range(1,len(height)):
#             m = max(mxl[i-1],height[i])
#             mxl.append(m)
#         mxr = [0 for i in range(n+1)]
#         mxr[n]=height[n]
#         for i in range(n-1,0,-1):
#             mxr[i] = max(height[i],mxr[i+1])
#         water = [0 for i in range(len(height))]
#         for i in range(len(height)):
            
#             cal = min(mxl[i],mxr[i])-height[i]
#             water[i]= cal if cal>=0 else 0
#         return sum(water)