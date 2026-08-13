class Solution:
    def totalElements(self, arr):
        freq = {}
        left = 0
        right = 0
        size = 0
        unique = 0
        res = 0
        k = 2
        
        while right < len(arr):
            if unique <= k:
                res = max(res, size)
            
            if arr[right] in freq:
                freq[arr[right]] += 1
            else:
                freq[arr[right]] = 1
                unique += 1
                
            size += 1
                
            while unique > k:
                if freq[arr[left]] == 1:
                    del freq[arr[left]]
                    unique -= 1
                else:
                    freq[arr[left]] -= 1
                    
                size -= 1
                left += 1
            
            right += 1
        
        if unique <= k:
            res = max(res, size)
            
        return res