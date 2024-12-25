class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res=False
        r=len(board)
        c=len(board[0])
        v=set()
        def backtrack(i,j,ind):
            nonlocal r,c,res
            
            if ind==len(word):
                res=True
                return
            if i<0 or i>r-1 or j<0 or j>c-1 or board[i][j]!=word[ind] or (i,j) in v :
                return
            
            v.add((i,j))
            
            backtrack(i-1,j,ind+1)
        
            backtrack(i,j+1,ind+1)
            backtrack(i,j-1,ind+1)
            
            backtrack(i+1,j,ind+1)
            v.discard((i,j))
            
        for i in range(r):
            for j in range(c):
                if board[i][j]==word[0]:
                    backtrack(i,j,0)
        return res