class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        low = 0
        high = 0
        res = float("-inf")
        f = {}

        while high < n:
            f[s[high]] = f.get(s[high], 0) + 1
            length = high - low + 1

            while len(f) < length:
                f[s[low]] -= 1
                if f[s[low]] == 0:
                    del f[s[low]]
                low += 1
                length = high - low + 1

            # now equal
            length = high - low + 1
            res = max(res, length)
            high += 1

        if res == float("-inf"):
            return 0
        return res