class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        freq = collections.defaultdict(int)
        n = len(nums)
        
        for i in range(n - k + 1):
            for val in set(nums[i:i + k]):
                freq[val] += 1
                
        ans = -1
        for val, count in freq.items():
            if count == 1:
                ans = max(ans, val)
                
        return ans