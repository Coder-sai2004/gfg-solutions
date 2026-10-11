class Solution:
    def sortStack(self, st):
        temp = []
        res =[]
        
        for val in st:
            
            if res:
                while res and val < res[-1]:
                    temp.append(res.pop())
                res.append(val)
                
                while temp:
                    res.append(temp.pop())
                
            else:
                res.append(val)
                
        
        st[:] = res