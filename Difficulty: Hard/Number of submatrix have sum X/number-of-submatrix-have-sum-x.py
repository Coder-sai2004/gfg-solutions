class Solution:
    def countSquare(self, mat, x):
        row=len(mat)
        col=len(mat[0])
        c=0
        pre=[[0]*col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                top=pre[i-1][j] if i>0 else 0
                left=pre[i][j-1] if j>0 else 0
                diag=pre[i-1][j-1] if i>0 and j>0 else 0
                curr=mat[i][j]+top+left-diag
                pre[i][j]=curr
        for size in range(min(row,col)):
            n=size+1
            for i in range(size,row):
                for j in range(size,col):
                    left_edge=pre[i][j-n] if j-n>=0 else 0
                    top_edge=pre[i-n][j] if i-n>=0 else 0
                    diag_edge=pre[i-n][j-n] if i-n>=0 and j-n>=0 else 0
                    curr=pre[i][j]-(left_edge+top_edge-diag_edge)
                    if curr==x:
                        c+=1
        return c