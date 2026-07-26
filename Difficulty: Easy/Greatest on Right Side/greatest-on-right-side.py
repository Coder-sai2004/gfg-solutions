class Solution:

	def nextGreatest(self,arr):
	    arr=arr[::-1]
	    x=-1
	    res=[0]*len(arr)
	    for i in range(len(arr)):
	        res[i]=x
	        x=max(x,arr[i])
	    return res[::-1]