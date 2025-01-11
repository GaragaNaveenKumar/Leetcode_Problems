class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k>len(s):
            return False
        c=Counter(s)
        x=0
        for i in c.values():
            if i%2!=0:
                x+=1
        if x>k:
            return False
        return True
        