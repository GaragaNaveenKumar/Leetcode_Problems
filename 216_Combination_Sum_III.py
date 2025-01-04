class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        def dfs(t,arr,s,start):
            if s==0 and t==0:
                res.append(arr[:])
                return
            for i in range(start,10):
                if i+s<=0 and t!=0:
                    return
                dfs(t-1,arr+[i],s-i,i+1)
        dfs(k,[],n,1)
        return res
        