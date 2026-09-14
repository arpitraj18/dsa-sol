class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        low=high=0
        n=len(s)
        freq={}
        res=0
        max_freq=0
        while high<n:
            freq[s[high]]=freq.get(s[high],0)+1
            max_freq=max(max_freq,freq[s[high]])
            while (high-low+1)-max_freq>k:
                freq[s[low]]-=1
                low+=1
            res=max(res,high-low+1)
            high+=1
        return res
