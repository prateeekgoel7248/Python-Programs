class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        if len(A)%2==0:
            return 0
########


# first of all common as we know arrays size can be either even or odd: 

# even example: [a,b,c,d]
# subarrays: there will be total n(n+1)/2 subarrays.
# a
# a,b
# a,b,c
# a,b,c,d
# b
# b,c
# b,c,d
# c
# c,d
# d
# here we are asked to find XOR of all the sub-arrays.
# which means our ans will be: 
# a^a^b^a^b^c^a^b^c^d^b^b^c^b^c^d^c^c^d^d
# and as we know the property of XOR:  1^1 = 0;
# 1^1^1^1 also equals 0 because if you pair up them in 2 then they will make 2 pairs. which will eventually make the ans as 0.
# and 1^1^1 => (1^1)^1 =>(0)^1 = 1

# so in our ans occurrence of every element: 
# a=4
# b=4
# c=4
# d=4

# from this general example, we can say that if the size of the array is even then all subarrays XOR will eventually be 0.

# ODD example: [a,b,c,d,e] make subarrays by your self. :slight_smile:
# for the ODD example every element which is at ODD index will occur ODD times and the rest of the elements that are at EVEN index will occur EVEN times and from the XOR property every element which is occurring even times will eventually be 0. 
# so that why in the solution it is i=i+2 instead of i=i+1.
# i hope you understand
#######


    
        ans=0
        for i in range(0,len(A),2):
            ans^=A[i]
        return ans
