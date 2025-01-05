class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0] * (len(s)+1)
        for shift in shifts:
            if shift[2] == 0:
                prefix[shift[0]] += -1
                prefix[shift[1]+1] += 1
            else:
                prefix[shift[0]] += 1
                prefix[shift[1]+1] += -1
        res=""
        shift=0
        for i in range(len(s)):
            shift+=prefix[i]
            res+=chr((ord(s[i])-97+shift)%26+97)
        return res
        