class Solution:
    def maxScore(self, s: str) -> int:
        n=len(s)
        prefixzeroes=[0]*n
        sufixones=[0]*n
        prefixzeroes[0]=1 if s[0]=="0" else 0
        sufixones[-1]=1 if s[-1]=="1" else 0
        for i in range(1,n):
            if s[i]=="0":
                prefixzeroes[i]=prefixzeroes[i-1]+1
            else:
                prefixzeroes[i]=prefixzeroes[i-1]
        for i in range(n-2,-1,-1):
            if s[i]=="1":
                sufixones[i]=sufixones[i+1]+1
            else:
                sufixones[i]=sufixones[i+1]
        
        mx=float("-inf")
        for i in range(1,n):
            mx=max(mx,prefixzeroes[i-1]+sufixones[i])
        return mx
        