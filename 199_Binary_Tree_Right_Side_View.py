# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        d=deque()
        d.append(root)
        res=[]
        if not root:
            return res
        
        while d:
            l=[]
            for i in range(len(d)):
                k=d.popleft()
                
                l.append(k.val)
                if k.left:
                    d.append(k.left)
                if k.right:
                    d.append(k.right)
            res.append(l[-1])
        return res
        