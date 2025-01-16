class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:


        res=[]

        def dfs(ss,i,n):
            if i>=n:
                res.append(ss)
                return
            if  s[i].isdigit():
                dfs(ss+s[i],i+1,n)
            else:
                dfs(ss+s[i].upper(),i+1,n)
                dfs(ss+s[i].lower(),i+1,n)
        dfs('',0,len(s))
        return res

        