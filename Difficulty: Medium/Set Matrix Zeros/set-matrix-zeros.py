class Solution:
    def setMatrixZeroes(self, mat):
        row = set()
        col = set()
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    row.add(i)
                    col.add(j)
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i in row or j in col:
                    mat[i][j] = 0
                    
        return mat