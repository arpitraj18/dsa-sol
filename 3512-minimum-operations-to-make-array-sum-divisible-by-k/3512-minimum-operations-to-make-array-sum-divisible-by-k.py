class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        current_sum = sum(nums)
        remainder = current_sum % k
        return remainder