class Solution:
    def water(self,arr,idx):
        left = 0
        right = 1
        val = 0
        trapped_water = 0
        
        while right <= idx:
            
            if arr[left] > arr[right]:
                
                val += arr[right]
            
            elif arr[left] <= arr[right]:
                
                width = right-left-1
                
                area = arr[left]*width
                
                trapped_water += area-val
                
                val = 0
                
                left = right
            
            
            right+=1
        
        return trapped_water
                
    def maxWater(self, arr):
        
        mx = max(arr)
        
        idx = arr.index(mx)
        
        r_idx = len(arr)-idx-1
        
        temp = arr[::-1]
        
        left_half = self.water(arr,idx)
        
        right_half = self.water(temp,r_idx)
        
        return left_half + right_half