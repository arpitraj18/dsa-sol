class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        low=0
        high=1
        k=1
        occurence=1
        while high<len(nums):
            if nums[high]==nums[high-1]:
                occurence+=1
            else:
                occurence=1
            if occurence<=2:
                    nums[low+1]=nums[high]
                    low+=1
                    k+=1
            high+=1
        return k

