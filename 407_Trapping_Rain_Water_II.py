class Solution:
    def trapRainWater(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows=len(grid)
        cols=len(grid[0])

        visited=[[False] *cols for i in range(rows)]

        heap=[]

        for i in range(rows):
            for j in range(cols):
                if i==0 or j==0 or i==rows-1 or j==cols-1:
                    heapq.heappush(heap,(grid[i][j],i,j))
                    visited[i][j]=True


        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        result=0

        while heap:
            h,i,j=heapq.heappop(heap)
            for x,y in directions:
                ni,nj=x+i,y+j
                if 0<=ni<rows and 0<=nj<cols and not visited[ni][nj]:
                    visited[ni][nj]=True
                    result+=max(0,h-grid[ni][nj])
                    heapq.heappush(heap,(max(h,grid[ni][nj]),ni,nj))
        return result


        
        
        