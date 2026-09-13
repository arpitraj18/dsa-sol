class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low=high=curr_sum=0
        res=float('inf')
        n=len(nums)
        while high<n:
            curr_sum=curr_sum+nums[high]
            while curr_sum>=target:
                length=high-low+1
                res=min(res,length)
                curr_sum-=nums[low]
                low+=1
            high+=1
        return res if res!= float('inf') else 0