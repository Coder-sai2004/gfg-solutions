class Solution:
    def rotateMatrix(self, mat):
        # code here
        res=[[0]*len(mat[0]) for _ in range(len(mat))]
        k=len(mat[0])-1
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                res[i][j]=mat[j][k]
            k-=1
        mat[:]=res