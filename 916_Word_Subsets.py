class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        occ={l:max(b.count(l) for b in words2) for l in set("".join(words2))}
        res=[]
        for a in words1:
            acc=True
            for l,t in occ.items():
                if t>a.count(l):
                    acc=False
                    break
            if acc:
                res.append(a)
        return res
        