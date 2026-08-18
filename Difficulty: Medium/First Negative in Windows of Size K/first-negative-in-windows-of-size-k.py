from collections import deque
class Solution:
    def firstNegInt(self, arr, k): 
        ans=[]
        st=deque([])
        
        for i in range(k):
            if arr[i]<0:
                st.append(arr[i])
        
        if len(st)!=0:
            ans.append(st[0])
        else:
            ans.append(0)
            
        for i in range(k,len(arr)):
           if arr[i-k]<0 and arr[i-k]==st[0]:
                st.popleft()
                
           if arr[i]<0:
               st.append(arr[i])
               
           if len(st)!=0:
               ans.append(st[0])
           else:
               ans.append(0)
           
        return ans