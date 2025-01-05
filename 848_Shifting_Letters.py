class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        prefix=[0]*len(s)
        prefix[-1]=shifts[-1]
        for i in range(len(s)-2,-1,-1):
            prefix[i]=shifts[i]+prefix[i+1]
        res=""
        for i in range(len(s)):
            res+=chr((ord(s[i])-97+prefix[i])%26+97)
        return res
        