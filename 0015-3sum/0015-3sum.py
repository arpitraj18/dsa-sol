class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res=[]
        n=len(nums)
        for i in range (n-2): #this is importatn and in this question, all (i, left,right) shouldnt be equal to each thus if it goes to n-1, only one element will remian in the end , in that case let would be equal to right 
            left= i+1
            right=n-1
            base=-1*nums[i]# as if a+b+c=0 -> a+b=-c
            if(i>0 and nums[i]==nums[i-1]):#should consider i values aswell, we are taking acre of similar left and right values below
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

