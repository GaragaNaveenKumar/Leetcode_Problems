class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n=len(graph)
        res=[]
        def dfs(i,path):
            if i==n-1:
                res.append(path[:])
                return
            for j in graph[i]:
                dfs(j,path+[j])
        dfs(0,[0])
        return res
            

            

            
        