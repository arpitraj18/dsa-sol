from collections import Counter
import heapq
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        count=Counter(tasks)
        max_heap=[-freq for freq in count.values()]
        heapq.heapify(max_heap)
        time=0
        while max_heap:
            temp=[]
            for _ in range(n+1):
                if max_heap:
                    freq=heapq.heappop(max_heap)
                    temp.append(freq+1)#decrementing as it is in negative
            for freq in temp:
                if freq<0:
                    heapq.heappush(max_heap,freq)
            if not max_heap:
                time+=len(temp)#if heap is empty we only add actual tasks processed
            else:
                time+=n+1#if heap not empty, we add full cycle of (n+1) to include the idle time
        return time
                

        