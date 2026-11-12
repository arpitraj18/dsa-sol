from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        n=len(s)
        count=Counter(s)
        for char, freq in count.items():
            if freq>(n+1)//2:
                return ""
        max_heap=[[-freq,char] for char,freq in count.items()]
        heapq.heapify(max_heap)
        result=[]

#as we will have atleast 2 elemts for the solution to be there otherise there would be cases like aaaa, bbb etc
        while len(max_heap)>=2:
            freq1,char1=heapq.heappop(max_heap)
            freq2,char2=heapq.heappop(max_heap)
            #popping out 2 elements as we have already checked that atleast 2 elements and python takes care of lexicgraphical thing
            result.append(char1)
            result.append(char2)

            #decreasing the frequency, we wouldve donce freq-=1 but here they are store in negative thus we do +
            freq1+=1
            freq2+=1
            #pushing them back inside heap if still freq available
            if freq1<0:
                heapq.heappush(max_heap,[freq1,char1])
            if freq2<0:
                heapq.heappush(max_heap,[freq2,char2])
        #handling last singualar remaining charcter(in case odd number in n then after 2 pop sequence 1 would be remaining)
        if max_heap:
            result.append(max_heap[0][1])
        return "".join(result)


        