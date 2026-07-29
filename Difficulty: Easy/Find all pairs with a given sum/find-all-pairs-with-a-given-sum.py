from collections import Counter
class Solution:
    def allPairs(self, target, arr1, arr2):
        s=Counter(arr2)
        res=[]
        ans=[]
        
        for i in arr1:
            x=target-i
            if x in s:
                t=[i,x]*s[x]
                res.extend(t)
        
        for i in range(0,len(res)-1,2):
            ans.append([res[i],res[i+1]])
            
        result=sorted(ans,key=lambda x:x[0])
        return result