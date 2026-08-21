from collections import defaultdict
class Solution:
    def getLastDigit(self, a, b):
        if b=="0":
            return 1
        
        res=[[0,0,0,0],[1,1,1,1],[2,4,8,6],[3,9,7,1],[4,6,4,6],[5,5,5,5],[6,6,6,6],[7,9,3,1],[8,4,2,6],[9,1,9,1]]
        x=int(a[-1])
        y=int(b)%4
        if y==0:
            y=3
        else:
            y-=1
        
        ans=res[x][y]
        return ans