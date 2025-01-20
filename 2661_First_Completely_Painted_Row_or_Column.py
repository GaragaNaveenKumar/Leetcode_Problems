class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:

        rows=len(mat)
        cols=len(mat[0])

        positions={}
        for i in range(rows):
            for j in range(cols):
                positions[mat[i][j]]=(i,j)
        
        paintedrows={i:0 for i in range(rows)}

        paintedcols={i:0 for i in range(cols)}

        
        for ind,i in enumerate(arr):
            paintedrows[positions[i][0]]+=1
            if paintedrows[positions[i][0]]==cols:
                return ind

            paintedcols[positions[i][1]]+=1
            if paintedcols[positions[i][1]]==rows:
                return ind
        
        

            
        