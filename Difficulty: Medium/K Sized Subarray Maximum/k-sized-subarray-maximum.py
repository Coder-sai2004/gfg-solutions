from collections import deque
class Solution:
    def maxOfSubarrays(self, arr, k):
        st=deque([])
        ans=[]
        
        for i in range(k):
            while st and arr[i]>st[-1]:
                st.pop()
            st.append(arr[i])
        
        ans.append(st[0])
        
        for i in range(k,len(arr)):
            if arr[i-k]==st[0]:
                st.popleft()
                
            while st and arr[i]>st[-1]:
                st.pop()
                
            st.append(arr[i])
            
            ans.append(st[0])
        
        return ans