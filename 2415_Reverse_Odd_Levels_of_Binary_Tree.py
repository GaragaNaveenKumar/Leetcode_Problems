# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # d=deque()
        # d.append(root)
        # c=1
        # while len(d):
        #     print(c)
            
        #     for i in range(len(d)):
        #         k=d.popleft()
        #         if k.left:
        #             d.append(k.left)
        #         if k.right:
        #             d.append(k.right)
        #     c+=1
                
        #     if c==2:
        #         l=deque()
        #         for i in range(len(d)):
        #             l.append(d[i].val)
                
        #         for i in range(len(d)):
        #             d[i].val=l.pop()
        #         c=0
        # return root
        def helper(lef,righ,l):
            if lef==None and righ==None:
                return
            if l%2!=0:
                lef.val,righ.val=righ.val,lef.val
            helper(lef.left,righ.right,l+1)
            helper(lef.right,righ.left,l+1)
        helper(root.left,root.right,1)
        return root