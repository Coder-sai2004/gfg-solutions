class Solution:
	def preGreaterEle(self, arr):
	    arr=arr[::-1]
	    st=[]
	    res=[-1]*len(arr)
	    for i in range(len(arr)):
	        while st and arr[i]>arr[st[-1]]:
	            idx=st.pop()
	            res[idx]=arr[i]
	        st.append(i)
	    return res[::-1]