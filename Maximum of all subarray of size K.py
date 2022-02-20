class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return a list of integers
	def slidingMaximum(self, A, B):
		from collections import Counter
		# d=
		res=[]
		ans=[]
		i=0
		j=0
		k=B
		while j<len(A):
			while len(ans)>0 and A[j]>ans[-1]:
				ans.pop()
			ans.append(A[j])
			if j-i+1<k:
				j+=1
			elif j-i+1==k:
				res.append(ans[0])
				if A[i]==ans[0]:
					ans.pop(0)
				i+=1
				j+=1
		return res


