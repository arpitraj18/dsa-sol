class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        def dfs(index: int, current_xor: int) -> int:
            # Base case: when we have considered all elements, return the current subset's XOR total
            if index == len(nums):
                return current_xor
            
            # Option 1: Include the current element in the subset
            include = dfs(index + 1, current_xor ^ nums[index])
            
            # Option 2: Exclude the current element from the subset
            exclude = dfs(index + 1, current_xor)
            
            # Return the sum of XOR totals from both branches
            return include + exclude

        return dfs(0, 0)