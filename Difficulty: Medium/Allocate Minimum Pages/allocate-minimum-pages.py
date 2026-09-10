class Solution:
    def checkpay(self,arr,mid):
        nostd=1
        load=0
        for page in arr:
            if page+load>mid:
                load=page
                nostd+=1
            else:
                load+=page
        return nostd
    def findPages(self, arr, k):
        if len(arr)<k:
            return -1 
        low=max(arr)
        high=sum(arr)
        while low<high:
            mid=(low+high)//2
            distd=self.checkpay(arr,mid)
            if distd<=k:
                high=mid
            else:
                low=mid+1
        return low