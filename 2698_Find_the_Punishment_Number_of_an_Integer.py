class Solution:
    def punishmentNumber(self, n: int) -> int:

        def dfs(index,csum,n,s,i):
            if index==n:
                return csum==i
            
            num=0
            for j in range(index,n):
                num=num*10+int(s[j])
                if dfs(j+1,csum+num,n,s,i):
                    return True
            return False

        res=0

        for i in range(1,n+1):
            s=str(i*i)
            if dfs(0,0,len(s),s,i):
                res+=i*i
        return res
        