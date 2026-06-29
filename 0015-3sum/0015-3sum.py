class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res=[]
        n=len(nums)
        for i in range (n-2):
            left= i+1
            right=n-1
            base=-1*nums[i]
            if(i>0 and nums[i]==nums[i-1]):
                continue
            while left<right :
                sum=nums[left]+nums[right]
                if sum==base:
                    res.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left<n and nums[left]==nums[left-1]:
                        left+=1
                    while right>=0 and nums[right]==nums[right+1]:
                        right-=1
                elif sum<base:
                    left+=1
                else:
                    right-=1
        return res

