class Solution:
    def reverses(self, s):
        res = []
        
        for ch in s:
            res.append(ch)
        
        
        i = len(s) -1
        j = 0
        
        while i > -1:
            if s[i] == " ":
                i -= 1
                continue
            elif res[j] == " ":
                j += 1
                continue
                
            
            res[j] = s[i]
            
            i -= 1
            j += 1
            
        return "".join(res)