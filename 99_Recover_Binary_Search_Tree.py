# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder(root):
            if root:
                inorder(root.left)
                l.append(root)
                inorder(root.right)
        # l=[]
        # inorder(root)
        # p=sorted(n.val for n in l)
        # for i in range(len(p)):
        #     l[i].val=p[i]
        # return root
        f=p=s=None
        def inorder(root):
            nonlocal p,f,s
            if root:
                inorder(root.left)
                if p and p.val>root.val:
                    if not f:
                        f=p
                    s=root
                p=root
                inorder(root.right)
        inorder(root)
        if f and s:
            f.val,s.val=s.val,f.val
        return root

        