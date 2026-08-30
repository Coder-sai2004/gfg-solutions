class Solution:

    def getMarks(self, l, r, rank):
        res=sorted(l+r)
        temp=[]
        for i in range(0,len(res)-1,2):
            left=res[i]
            right=res[i+1]
            for j in range(left,right+1):
                temp.append(j)
        ans=[]
        for r in rank:
            ans.append(temp[r-1])
        return ans