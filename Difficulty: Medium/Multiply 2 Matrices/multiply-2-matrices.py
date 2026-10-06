class Solution:
	def multiply(self, mat1, mat2):
	    n = len(mat1)
		res = [[0]*n for _ in range(n)]
		
		for row in range(n):
		    for col in range(n):
		        for i in range(n):
		            res[row][col] += mat1[row][i] * mat2[i][col]
		return res