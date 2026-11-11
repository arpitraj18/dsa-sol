from collections import Counter
from typing import List
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequency_map=Counter(nums)
        #creating a frequency bucket where the index reporenets the frequency count
        n=len(nums)
        buckets=[[] for _ in range(n+1)]
        for number, freq in frequency_map.items():
            buckets[freq].append(number)#appends the number at index freq
        result=[]
        #iterating backwards from highest possible
        for freq in range(n,0,-1):
            for number in buckets[freq]:
                result.append(number)
                if len(result)==k:
                    return result
        return result
        