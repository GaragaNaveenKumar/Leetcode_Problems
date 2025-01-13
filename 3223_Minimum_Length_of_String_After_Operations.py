class Solution:
    def minimumLength(self, s: str) -> int:
        c=Counter(s)
        res=0
        for i in c.values():
            if i%2==0:
                res+=2
            else:
                res+=1
        return res

        