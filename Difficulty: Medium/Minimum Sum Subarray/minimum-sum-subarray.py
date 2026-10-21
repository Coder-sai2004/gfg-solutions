class Solution:
    def minSubarraySum(self, arr: list[int]) -> int:
        min_global= arr[0]
        min_curr = arr[0]
        
        for i in range(1,len(arr)):
            
            min_curr = min(arr[i],min_curr + arr[i])
            
            if min_curr < min_global:
                min_global = min_curr
                
        
        return min_global