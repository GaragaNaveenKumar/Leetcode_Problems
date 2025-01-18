class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        dirs=[[0,1],[0,-1],[1,0],[-1,0]]
        queue=deque([(0,0,0)])
        visited=set()

        while queue:
            i,j,cost=queue.popleft()
            if (i,j) in visited:
                continue
            visited.add((i,j))

            if i==rows-1 and j==cols-1:
                return cost
            for k,(di,dj) in enumerate(dirs,1):
                ni,nj=i+di,j+dj
                if 0<=ni <rows and 0<=nj<cols:
                    if k==grid[i][j]:
                        queue.appendleft((ni,nj,cost))
                    else:

                        queue.append((ni,nj,cost+1))
        return -1


        

        