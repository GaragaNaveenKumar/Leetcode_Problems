class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        
        respaths=0
        def dfs(i,j,rem):
            nonlocal rows,cols,respaths
            if i<0 or i>=rows or j<0 or j>=cols or grid[i][j]==-1:
                return

            if grid[i][j]==2:
                if rem==-1:
                    respaths+=1
                return
            
            temp=grid[i][j]
            grid[i][j]=-1
            for m,n in [(-1,0),(0,-1),(1,0),(0,1)]:
                dfs(i+m,j+n,rem-1)
            grid[i][j]=temp
    
        empty=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    
                    empty+=1
                elif grid[i][j]==1:
                    start=[i,j]
        dfs(start[0],start[1],empty)
        return respaths