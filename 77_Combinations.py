class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def backtrack(path,start):
            if len(path)==k:
                res.append(path[:])
            for i in range(start,n+1):
                backtrack(path+[i],i+1)
        backtrack([],1)
        return res