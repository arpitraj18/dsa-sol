import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        n = len(profits)
        
        # Pair up capital requirements with their respective profits
        projects = []
        for i in range(n):
            projects.append((capital[i], profits[i]))
            
        # Sort projects by required capital in ascending order
        projects.sort()
        
        i = 0
        max_heap = []
        
        while k > 0:
            k -= 1
            # Push all affordable projects into the max-heap
            while i < n and projects[i][0] <= w:
                # heapq is a min-heap, so negate the profit to simulate a max-heap
                heapq.heappush(max_heap, -projects[i][1])
                i += 1
                
            # If no projects can be afforded, we stop early
            if not max_heap:
                break
                
            # Greedily pick the project with the maximum profit
            w += -heapq.heappop(max_heap)
            
        return w