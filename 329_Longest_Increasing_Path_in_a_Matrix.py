class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        res=0
        rows=len(matrix)
        cols=len(matrix[0])
        dp={}
        def dfs(i,j,prev):
            if i<0 or i>=rows or j<0 or j>=cols or prev>=matrix[i][j]:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            dp[(i,j)]=max(dfs(i-1,j,matrix[i][j]),dfs(i,j-1,matrix[i][j]),dfs(i,j+1,matrix[i][j]),dfs(i+1,j,matrix[i][j]))+1
            return dp[(i,j)]
        for i in range(rows):
            for j in range(cols):
                res=max(res,dfs(i,j,float("-inf")))
        return res