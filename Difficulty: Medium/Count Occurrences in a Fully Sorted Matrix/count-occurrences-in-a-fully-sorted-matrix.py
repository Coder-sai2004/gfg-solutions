class Solution:
    def countOccurrences(self, mat, x): 
    	res = []
    	for sub in mat:
    	    res.extend(sub)
    	    
    	return res.count(x)