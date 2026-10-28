class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)
        min_val, max_val = min(nums), max(nums)
        
        # Check every integer in the range [min_val, max_val]
        return [i for i in range(min_val, max_val + 1) if i not in nums_set]