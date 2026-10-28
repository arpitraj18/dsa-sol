class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        # Count the number of even and odd numbers
        evens = sum(1 for x in nums if x % 2 == 0)
        odds = len(nums) - evens
        
        # All even numbers become 0, and all odd numbers become 1.
        # Since we sort in non-decreasing order, all 0s come first, followed by 1s.
        return [0] * evens + [1] * odds