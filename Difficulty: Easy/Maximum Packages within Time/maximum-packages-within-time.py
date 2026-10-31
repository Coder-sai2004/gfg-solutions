class Solution:
    def maxPackages(self, arr: list[int], totalTime: int) -> int:
        pre = [arr[0]]
        for i in range(1,len(arr)):
            pre.append(pre[i - 1] + arr[i])
            
        if totalTime > len(pre):
            return pre[-1]
        
        ans = 0
        i = -1
        j = totalTime - 1
        
        while j < len(pre):
            if i == -1:
                ans = max(ans,pre[j])
            else:
                ans = max(ans, (pre[j] - pre[i]))
            
            i += 1
            j += 1
        
        return ans