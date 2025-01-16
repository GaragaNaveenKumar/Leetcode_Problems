class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        m=len(nums1)
        n=len(nums2)

        if m%2==0 and n%2==0:
            return 0
        if n%2==0:
            m,n=n,m
            nums1,nums2=nums2,nums1
        
        res=0
        if m%2!=0:
            for i in nums2:
                res^=i
        for i in nums1:
            res^=i
        return res
        