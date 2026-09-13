class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        low=high=0
        freq={}
        res=float('-inf')
        n=len(fruits)
        while high<n:
            freq[fruits[high]]=freq.get(fruits[high],0)+1
            while len(freq)>2:
                freq[fruits[low]]-=1
                if freq[fruits[low]]==0:
                    del freq[fruits[low]]
                low+=1
            if len(freq)==2 or len(freq)<2:
                length=high-low+1
                res=max(length,res)
            high+=1
        return res