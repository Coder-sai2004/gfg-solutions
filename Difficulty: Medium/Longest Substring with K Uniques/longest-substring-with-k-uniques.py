class Solution:
    def longestKSubstr(self, s, k):
        d={}
        i=0
        j=0
        c=0
        mx=0
        ans=-1
        while j<len(s):
            if c==k:
                ans=max(ans,mx)
            
            if s[j] not in d and c==k:
                while c==k:
                    if d[s[i]]==1:
                        del d[s[i]]
                        c-=1
                    else:
                        d[s[i]]-=1
                        
                    mx-=1
                    i+=1
                    
                d[s[j]]=1
                c+=1
            
            elif s[j] in d:
                d[s[j]]+=1
            else:
                d[s[j]]=1
                c+=1
                
            mx+=1
            j+=1
            
        if c==k:
            ans=max(ans,mx)
        
        return ans