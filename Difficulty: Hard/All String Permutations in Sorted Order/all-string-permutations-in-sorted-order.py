class Solution:
    def permutation(self,s):
        result=[]
        nums=list(s)
        def backtrack(path,used):
            if len(s)==len(path):
                result.append(path.copy())
                return
            for i in range(len(s)):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i]=True
                backtrack(path,used)
                used[i]=False
                path.pop()
        backtrack([],[False]*len(nums))
        res=["".join(x) for x in result]
        final=sorted(res,key=tuple)
        return final