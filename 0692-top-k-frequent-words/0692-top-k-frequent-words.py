from collections import Counter
class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        count=Counter(words)
        buckets=[[] for _ in range(len(words)+1)]
        for word,freq in count.items():
            buckets[freq].append(word)
        res=[]
        for i in range(len(buckets)-1,0,-1):
            if buckets[i]:
                buckets[i].sort()
                for word in buckets[i]:
                    res.append(word)
                    if len(res)==k:
                        return res
        return res