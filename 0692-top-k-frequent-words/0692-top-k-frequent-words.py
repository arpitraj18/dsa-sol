from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        f = Counter(words)
        max_heap = []
        for word, count in f.items():
            heapq.heappush(max_heap, (-count, word))
            
        op = []
        while max_heap and k > 0:
            count, word = heapq.heappop(max_heap)
            op.append(word)
            k -= 1  
            
        return op