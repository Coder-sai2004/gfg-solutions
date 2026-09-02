class Solution:
    def solve(self, n, s):
        ans=0
        temp=set()
        t=set()
        c=0
        
        for i in s:
            if (i not in temp and c<n) and (i not in t):
                temp.add(i)
                c+=1
                
            elif i in temp:
                c-=1
            
            elif (c==n and i not in temp) or (i in t):
                t.add(i)
                ans+=1
                
        return ans//2