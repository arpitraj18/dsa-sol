class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i, char in enumerate(s):
            # i + 1 is the 1-indexed position in the string
            # 26 - (ord(char) - ord('a')) is the position in the reversed alphabet ('a' = 26, 'z' = 1)
            rev_alphabet_pos = 26 - (ord(char) - ord('a'))
            total += rev_alphabet_pos * (i + 1)
        return total