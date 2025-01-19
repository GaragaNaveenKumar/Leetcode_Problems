class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        counter={}
        for i in nums:
            count=counter.get(i,0)
            if count==2:
                return False
            counter[i]=count+1
        return True
        