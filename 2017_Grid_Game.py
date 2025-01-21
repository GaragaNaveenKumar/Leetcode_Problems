class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        top_sum=sum(grid[0][1:])
        bottom_sum=0
        result=max(top_sum,bottom_sum)
        for i in range(len(grid[0])-1):
            top_sum-=grid[0][i+1]
            bottom_sum+=grid[1][i]
            temp_result=max(top_sum,bottom_sum)
            result=min(result,temp_result)
        return result


        



        