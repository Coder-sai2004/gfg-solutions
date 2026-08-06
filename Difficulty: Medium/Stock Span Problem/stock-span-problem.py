class Solution:
    def calculateSpan(self, arr):
        st=[]
        res=[]
        st2=[]
        
        for i in range(len(arr)):
            val=1
            x=-1
            while st and (-x)<=len(st) and arr[i]>=st[x]: 
                st.pop()
                idx=st2.pop()
                val+=idx
            res.append(val)
            st.append(arr[i])
            st2.append(val)
        return res