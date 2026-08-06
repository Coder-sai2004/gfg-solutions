class Solution:
    def subarraySum(self, arr, target):
        i=0
        j=0
        s=0
        while s!=target and j<len(arr):
            # print(arr[i],'j:',arr[j],end=' ')
            if i>j:
                return [-1]
                
            if s>target:
                s-=arr[i]
                i+=1
                
            elif s<target:
                s+=arr[j]
                
                if s>target:
                    s-=arr[i]
                    i+=1
                elif s==target:
                    return [i+1,j+1]
                j+=1
            
            if s==target:
                return [i+1,j]
        
        while s>target:
            if i>=j:
                break
            s-=arr[i]
            i+=1
            if s==target:
                return [i+1,j]
                
            # print('sum:',s)
        return [-1]