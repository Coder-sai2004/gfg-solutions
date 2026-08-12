class Solution:
    def longestUniqueSubstr(self, s):
        d={}
        mx=0
        l=0
        r=0
        n=0
        res=0
        while r<len(s):
            if mx==1:
                res=max(res,n)
            
            if s[r] in d:
                d[s[r]]+=1
                mx=max(mx,d[s[r]])
            else:
                d[s[r]]=1
                mx=max(mx,d[s[r]])
            n+=1
            
            if mx>1:
                while d[s[r]]>1:
                    if d[s[l]]==1:
                        del d[s[l]]
                    else:
                        d[s[l]]-=1
                    
                    n-=1
                    l+=1
                    
                mx=d[s[r]]
            r+=1
        if mx==1:
            res=max(res,n)
        return res