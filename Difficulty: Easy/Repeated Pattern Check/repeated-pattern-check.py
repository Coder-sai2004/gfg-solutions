class Solution:
    def findPattern(self, s):
        c1 = 0
        c2 = 0
        i = 0
        
        while i < len(s):
            
            if s[i] == 'y' and (i + 1) < len(s) and s[i + 1] == 'x':
                c2 += 1
                
                if c1 != c2:
                    return False
                    
                c1 = 0
                c2 = 0
                    
            elif s[i] == 'x':
                c1 += 1
                
            elif s[i] == 'y':
                c2 += 1
                
            i += 1
        
        if c1 != c2:
            return False
        return True