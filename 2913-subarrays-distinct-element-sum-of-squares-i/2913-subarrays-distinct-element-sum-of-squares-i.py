class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total_sum = 0
        n = len(nums)
        
        # Generate all possible subarrays using nested loops
        for i in range(n):
            seen = set()
            for j in range(i, n):
                seen.add(nums[j])
                # Add the square of the distinct count of the current subarray
                total_sum += len(seen) ** 2
                
        return total_sum