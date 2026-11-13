class MedianFinder:

    def __init__(self):
        self.mx = []  # Max-heap (stores the smaller half of numbers, inverted with negatives)
        self.mn = []  # Min-heap (stores the larger half of numbers)

    def addNum(self, num: int) -> None:
        # 1. Always push to max-heap first
        heapq.heappush(self.mx, -num)
        
        # 2. Move the largest from max-heap to min-heap to keep order correct
        heapq.heappush(self.mn, -heapq.heappop(self.mx))
        
        # 3. Balance sizes if min-heap has more elements than max-heap
        if len(self.mn) > len(self.mx):
            heapq.heappush(self.mx, -heapq.heappop(self.mn))

    def findMedian(self) -> float:
        if len(self.mx) > len(self.mn):
            return -self.mx[0]
        return (-self.mx[0] + self.mn[0]) / 2