class Solution:
    def validStrings(self, n: int) -> List[str]:
        res=[]

        def dfs(s,i):

            if i==n:
                res.append(s)
                return
            if s=="" or s[-1]=="1":
                dfs(s+"1",i+1)
                dfs(s+"0",i+1)
            else:
                dfs(s+"1",i+1)
        dfs("",0)
        return res