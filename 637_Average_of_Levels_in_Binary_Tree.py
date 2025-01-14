# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:


        d=deque()
        d.append(root)
        res=[]
        if not root:
            return res
        while d:
            n=len(d)
            total=0
            for i in range(n):
                k=d.popleft()
                
                total+=k.val
                if k.left:
                    d.append(k.left)
                if k.right:
                    d.append(k.right)
            res.append(total/n)
        return res

        