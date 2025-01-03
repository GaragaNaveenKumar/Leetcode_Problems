class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        res=0
        left=0
        right=(sum(nums)+1)//2
        for i in range(len(nums)-1):
            left+=nums[i]
            if left>=right:
                res+=1
        return res
        # ps=[0]*len(nums)
        # ss=[0]*len(nums)
        # ps[0]=nums[0]
        # ss[-1]=nums[-1]
        # for i in range(1,len(nums)):
        #     ps[i]=ps[i-1]+nums[i]
        # for i in range(len(nums)-2,-1,-1):
        #     ss[i]=ss[i+1]+nums[i]
        # res=0
        # for i in range(1,len(nums)):
        #     if ps[i-1]>=ss[i]:
        #         res+=1
        # return res
        