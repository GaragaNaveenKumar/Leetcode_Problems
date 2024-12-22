class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        st=[]
        ma=0
        for i in range(len(h)):
            if not st:
                st.append(i)
            else:
                if h[st[-1]] <h[i]:
                    st.append(i)
                else:
                    print(1)
                    while st and h[st[-1]]>h[i]:
                        k=st.pop()
                        
                        p=-1 if not st else st[-1]
                        ma=max(ma,h[k]*((i-1)-p))
                    st.append(i)
        while st:
            n=len(h)
            k=st.pop()
                        
            p=-1 if not st else st[-1]
            ma=max(ma,h[k]*((n-1)-p))
        return ma