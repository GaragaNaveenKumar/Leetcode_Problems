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