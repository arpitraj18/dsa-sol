class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        return sum(val if i % 2 == 0 else -val for i, val in enumerate(nums))