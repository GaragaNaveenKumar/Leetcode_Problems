class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(path:list,rem:list):
            if len(rem)==0:
                
                res.append(path[:])
                return
            for i in range(len(rem)):
                
                path.append(rem[i])
                dfs(path,rem[:i]+rem[i+1:])
                path.pop()
        res=[]
        dfs([],nums)
        return res