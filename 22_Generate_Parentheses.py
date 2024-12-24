class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def backtrack(s,o,c):
            if c==0 and o==0:
                res.append(s)
                return
            if c>o:
                backtrack(s+")",o,c-1)
            if o>0:
                backtrack(s+"(",o-1,c)
        backtrack("",n,n)
        return res