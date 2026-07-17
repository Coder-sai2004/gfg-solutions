from collections import Counter
class Solution:
	def singleNum(self, arr):
		x=Counter(arr)
		res=[]
		for i,j in x.items():
		    if j==1:
		        res.append(i)
		res.sort()
		return res