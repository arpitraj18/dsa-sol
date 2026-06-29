class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n=len(nums)
        closest=float('inf')
        result_sum=0
        for i in range (n-2):
            left=i+1
            right=n-1
            while left<right:
                sum=nums[i]+nums[left]+nums[right]
                diff=abs(target-sum)

                if sum==target:
                    sum
                if diff<closest :
                    closest=diff
                    result_sum=sum
                if sum<target:
                    left+=1
                else:
                    right-=1
        return result_sum


