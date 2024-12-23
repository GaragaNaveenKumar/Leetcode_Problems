# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res=[]
        x=[]
        def dfs(root):
            
            x.append(str(root.val))
            if not root.left and not root.right:
                res.append("->".join(x))
                x.pop()
                return 
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
            x.pop()
            return
        dfs(root)
        return res