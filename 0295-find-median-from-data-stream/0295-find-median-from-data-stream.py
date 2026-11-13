class MedianFinder:

    def __init__(self):
        #two heaps, maxheap will store values smaller than median and the median and min will sotre values greater than median
        self.mx=[]
        self.mn=[]
        

    def addNum(self, num: int) -> None:
        #if first element of number < top of max heap will go into max heap
        if not self.mx or num<= -self.mx[0]:
            heapq.heappush(self.mx,-num)
        else:
            heapq.heappush(self.mn,num)
        #now we will have to balance out the two heaps
        #we can have an extra element in the lower half as the median we go into it, so it have have atmost 1 more than higher half
        if len(self.mx)>len(self.mn)+1:
            heapq.heappush(self.mn,-heapq.heappop(self.mx))
        elif len(self.mx)<len(self.mn):
            heapq.heappush(self.mx,-heapq.heappop(self.mn))
        

    def findMedian(self) -> float:
        if len(self.mx)==len(self.mn):
            return(-self.mx[0]+self.mn[0])/2
        
        return -self.mx[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()