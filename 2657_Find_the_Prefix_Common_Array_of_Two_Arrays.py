class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        m={}
        res=[0]*len(A)
        total=0
        for i in range(len(A)):
            c=m.get(A[i],0)+1
            m[A[i]]=c
            if c==2:
                total+=1
            c=m.get(B[i],0)+1
            m[B[i]]=c
            if c==2:
                total+=1
            res[i]=total
        return res


                    