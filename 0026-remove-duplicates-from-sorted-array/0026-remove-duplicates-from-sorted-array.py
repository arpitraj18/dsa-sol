class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        low=0
        k=1
        high=1
        while high<len(nums):
            if nums[high]==nums[high-1]:
                high+=1
            else:
                nums[low+1]=nums[high]
                high+=1
                low+=1
                k+=1
        return k