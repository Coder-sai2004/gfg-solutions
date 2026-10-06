class Solution:
    def  doesRepresentBST(self, arr):
        return arr == sorted(arr)